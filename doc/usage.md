
SIMULATOR:
ros2 launch turtlebot3_gazebo  turtlebot3_world.launch.py 
ros2 run turtlebot3_teleop teleop_keyboard

SLAM:
ros2 launch rtabmap_demos turtlebot3_rgbd.launch.py


NAV2:
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True
ros2 launch nav2_bringup rviz_launch.py
