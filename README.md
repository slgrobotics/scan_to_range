**Project Wiki:** https://github.com/slgrobotics/articubot_one/wiki

## *scan_to_range* ROS2 package

**A ROS2 LaserScan to Range topic relay to help with Sonars simulation in Gazebo**

See https://github.com/slgrobotics/articubot_one/blob/dev/launch/sonars_sim.launch.py

As the standard *topic_tools* package doesn't work since October 2025 update, I asked ChatGPT5 generate a helper relay package.

See:
- https://chatgpt.com/s/t_691cc863d70c81919fa279f4bcc2e06a
- https://chatgpt.com/s/t_691cc8351e648191a4cf0e7c5dd05428

### Installation - usually during [Desktop setup](https://github.com/slgrobotics/robots_bringup/blob/main/Docs/ROS-Jazzy/README.md)
```
mkdir -p ~/robot_ws/src
cd ~/robot_ws/src
git clone https://github.com/slgrobotics/scan_to_range.git
cd ~/robot_ws
colcon build
source ~/robot_ws/install/setup.bash
```
### Use

When running Dragger robot in sim:

https://github.com/slgrobotics/robots_bringup/blob/main/Docs/ROS-Jazzy/README.md#bringing-up-robot-simulation-in-gazebo

---------------------

**Project Wiki:** https://github.com/slgrobotics/articubot_one/wiki
