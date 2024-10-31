# Requirements:
#   A realsense D400 series
#   Install realsense2 ros2 package (make sure you have this patch: https://github.com/IntelRealSense/realsense-ros/issues/2564#issuecomment-1336288238)
# Example:
#   $ ros2 launch rtabmap_examples realsense_d400.launch.py

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node, SetParameter
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    parameters = [
        {
            "frame_id": "camera_link",
            "subscribe_depth": True,
            "subscribe_odom_info": False,
            "approx_sync": True,
            "approx_sync_max_interval": 0.05,
        }
    ]

    remappings = [
        ("rgb/image", "/camera/camera/color/image_raw"),
        ("rgb/camera_info", "/camera/camera/color/camera_info"),
        ("depth/image", "/camera/camera/depth/image_rect_raw"),
        # ("depth/image",  "/camera/camera/aligned_depth_to_color/image_raw")
    ]

    return LaunchDescription(
        [
            SetParameter(name="use_sim_time", value=False),
            Node(
                package="rtabmap_odom",
                executable="rgbd_odometry",
                output="screen",
                parameters=parameters,
                remappings=remappings,
            ),
            Node(
                package="rtabmap_slam",
                executable="rtabmap",
                output="screen",
                parameters=parameters,
                remappings=remappings,
                arguments=["-d"],
            ),
            Node(
                package="rtabmap_viz",
                executable="rtabmap_viz",
                output="screen",
                parameters=parameters,
                remappings=remappings,
            )
            
        ]
    )
