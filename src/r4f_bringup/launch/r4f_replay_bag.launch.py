from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


import os
from ament_index_python import get_package_share_directory





def generate_launch_description():
        
    # Launch Realsense camera launch file with aligned depth images publisher
    realsense = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory("realsense2_camera"), 'launch', 'rs_launch.py'
        )]), launch_arguments={#'align_depth.enable': 'false',
                            #    'camera_namespace': 'Camera',
                            #    'camera_name': 'D555_f',
                               'rosbag_filename': '/home/guilh/data_tese/vinha-11-07/run1_camera_f.bag'
                            # 'rosbag_filename': '/home/guilh/data_tese/camera/vinha-09-04/road1.bag'
                               }.items()
    )
    
    
    
    ld = LaunchDescription()
    
    ld.add_action(realsense)
    
    return ld
