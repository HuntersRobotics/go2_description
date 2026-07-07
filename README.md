# Unitree Go2 Description

[中文](#中文) | [English](#english)

---

## 中文

Unitree Go2 四足机器人 URDF 模型描述包，无需安装 ROS 2，在浏览器中即可可视化并调节关节。

### 使用方法

**1. 克隆仓库**

```bash
git clone https://partnergitlab.renesas.solutions/leggedrobot/unitree/go2_description.git
```

**2. 打开 RobotsFan Viewer**

👉 **[https://viewer.robotsfan.com/](https://viewer.robotsfan.com/)**

**3. 导入文件夹**

将克隆下来的 `go2_description` 文件夹整体拖入网页，网站自动识别加载。

**4. 打开模型**

在左侧文件树中双击 xacro 文件（如 `go2.xacro` 或 `robot.xacro`），3D 模型即在右侧显示。

**5. 调节关节角度**

右侧面板显示所有关节滑块，拖动或直接**输入数值**即可调整角度。例如：

| 关节 | 示例值 | 效果 |
|---|---|---|
| 四条腿的 calf_joint | `-1.5` | 蹲姿 |
| 四条腿的 hip_joint | `0.3` | 侧展 |
| FL_thigh + FR_thigh | `0.5` | 前腿前伸 |

> 直接在滑块旁的输入框里敲数字，比拖滑块更精确。

### 关节列表（共 12 个）

| 关节 | 所属腿 |
|---|---|
| `FL_hip_joint` / `FL_thigh_joint` / `FL_calf_joint` | 左前腿 |
| `FR_hip_joint` / `FR_thigh_joint` / `FR_calf_joint` | 右前腿 |
| `RL_hip_joint` / `RL_thigh_joint` / `RL_calf_joint` | 左后腿 |
| `RR_hip_joint` / `RR_thigh_joint` / `RR_calf_joint` | 右后腿 |

每条腿 3 个关节：髋 (hip)、大腿 (thigh)、小腿 (calf)，全部为 `revolute` 类型。

### 截图

![Go2 机器人在 RobotsFan Viewer 中](screenshots/20260707-141252.jpg)

### 文件结构

```
go2_description/
├── xacro/
│   ├── robot.xacro          # 主模型入口（含四条腿）
│   ├── go2.xacro            # 备选入口
│   ├── leg.xacro            # 单腿宏定义
│   ├── const.xacro          # 物理参数与关节限位
│   ├── materials.xacro      # 材质
│   └── transmission.xacro   # 传动
├── meshes/                  # 3D 网格 (.dae)
├── config/                  # 控制器配置
├── launch/                  # ROS 2 启动文件
└── rviz/                    # RViz 配置
```

---

## English

URDF model description for the Unitree Go2 quadruped robot. No ROS 2 required — visualize and adjust joints directly in the browser.

### Usage

**1. Clone**

```bash
git clone https://partnergitlab.renesas.solutions/leggedrobot/unitree/go2_description.git
```

**2. Open RobotsFan Viewer**

👉 **[https://viewer.robotsfan.com/](https://viewer.robotsfan.com/)**

**3. Import the Folder**

Drag the cloned `go2_description` folder into the browser window. The site auto-detects and loads the model.

**4. Open the Model**

Double-click a xacro file (e.g. `go2.xacro` or `robot.xacro`) in the left file tree. The 3D model appears on the right.

**5. Adjust Joint Angles**

The right panel shows sliders for all joints. Drag them or **type a value** directly. Examples:

| Joint(s) | Value | Result |
|---|---|---|
| All `calf_joint` | `-1.5` | Crouch pose |
| All `hip_joint` | `0.3` | Legs spread sideways |
| `FL_thigh` + `FR_thigh` | `0.5` | Front legs reach forward |

> Type into the input box next to each slider for precise angles.

### Joint List (12 total)

| Joint | Leg |
|---|---|
| `FL_hip_joint` / `FL_thigh_joint` / `FL_calf_joint` | Front-left |
| `FR_hip_joint` / `FR_thigh_joint` / `FR_calf_joint` | Front-right |
| `RL_hip_joint` / `RL_thigh_joint` / `RL_calf_joint` | Rear-left |
| `RR_hip_joint` / `RR_thigh_joint` / `RR_calf_joint` | Rear-right |

3 joints per leg: hip, thigh, calf — all `revolute`.

### Screenshots

![Go2 Robot in RobotsFan Viewer](screenshots/20260707-141252.jpg)

### File Structure

```
go2_description/
├── xacro/
│   ├── robot.xacro          # Main entry (4 legs)
│   ├── go2.xacro            # Alternate entry
│   ├── leg.xacro            # Single leg macro
│   ├── const.xacro          # Physics & joint limits
│   ├── materials.xacro      # Materials
│   └── transmission.xacro   # Transmissions
├── meshes/                  # 3D meshes (.dae)
├── config/                  # Controller config
├── launch/                  # ROS 2 launch files
└── rviz/                    # RViz config
```

---

## License

TBD
