from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch_ros.parameter_descriptions import ParameterValue
from launch.conditions import IfCondition, UnlessCondition


def generate_launch_description():
    # 定义参数
    user_debug_arg = DeclareLaunchArgument(
        'user_debug',
        default_value='false',
        description='Enable user debug mode'
    )

    gui_arg = DeclareLaunchArgument(
        name = 'gui',
        default_value = 'false',
        choices = ['false', 'true']
    )
    
    pkg_name = "go2_description"
    xacro_name = "go2.xacro"
    pkg_share = get_package_share_directory(pkg_name)
    xacro_path = os.path.join(pkg_share, 'xacro', xacro_name)
    robot_description = ParameterValue(Command(['xacro ', xacro_path]),
                                       value_type=str)

    # 创建节点
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        condition=UnlessCondition(LaunchConfiguration('gui'))
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        condition=IfCondition(LaunchConfiguration('gui'))
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {"robot_description": robot_description},
            # {'publish_frequency': 1000.0}
        ]
    )

    return LaunchDescription([
        user_debug_arg,
        joint_state_publisher_gui_node,
        joint_state_publisher_node,
        robot_state_publisher_node,
    ])