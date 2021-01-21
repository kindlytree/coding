# 

```
/path/to/apollo/modules/perception/production/dag/dag_streaming_perception_camera.dag

module_config {
  module_library : "/apollo/bazel-bin/modules/perception/onboard/component/libperception_component_camera.so"
  components {
    class_name : "FusionCameraDetectionComponent"
    config {
      name: "FusionCameraComponent"
      config_file_path: "/apollo/modules/perception/production/conf/perception/camera/fusion_camera_detection_component.pb.txt"
      flag_file_path: "/apollo/modules/perception/production/conf/perception/perception_common.flag"
    }
  }
}
```

```

/path/to/apollo/modules/perception/production/conf/perception/camera/fusion_camera_detection_component.pb.txt

camera_names: "front_6mm,front_12mm"
input_camera_channel_names : "/apollo/sensor/camera/front_6mm/image,/apollo/sensor/camera/front_12mm/image"
timestamp_offset : 0.0
camera_obstacle_perception_conf_dir : "/apollo/modules/perception/production/conf/perception/camera"
camera_obstacle_perception_conf_file : "obstacle.pt"
frame_capacity : 20
image_channel_num : 3
enable_undistortion : false
enable_visualization : false
output_final_obstacles : true
output_obstacles_channel_name : "/perception/obstacles"
camera_perception_viz_message_channel_name : "/perception/inner/camera_viz_msg"
prefused_channel_name : "/perception/inner/PrefusedObjects"
default_camera_pitch : 0.0
default_camera_height : 1.5
lane_calibration_working_sensor_name : "front_6mm"
calibrator_method : "LaneLineCalibrator"
calib_service_name : "OnlineCalibrationService"
run_calib_service : true
output_camera_debug_msg : false
camera_debug_channel_name : "/perception/camera_debug"
ts_diff : 0.1
visual_debug_folder : "/apollo/debug_output"
visual_camera : "front_6mm"
write_visual_img : false
enable_cipv : false
debug_level : 0
```

```
/apollo/modules/perception/production/conf/perception/camera/obstacle.pt

gpu_id : 0
detector_param {
  plugin_param{
    name : "YoloObstacleDetector"
    root_dir : "/apollo/modules/perception/production/data/perception/camera/models/yolo_obstacle_detector"
    config_file : "config.pt"
  }
  camera_name : "front_6mm"
  #camera_name : "spherical_left_forward"
}
detector_param {
  plugin_param{
    name : "YoloObstacleDetector"
    root_dir : "/apollo/modules/perception/production/data/perception/camera/models/yolo_obstacle_detector"
    config_file : "config.pt"
  }
  camera_name : "front_12mm"
}

tracker_param {
  plugin_param{
    name : "OMTObstacleTracker"
    root_dir : "/apollo/modules/perception/production/data/perception/camera/models/omt_obstacle_tracker"
    config_file : "config.pt"
  }
}
transformer_param {
  plugin_param{
    name : "MultiCueObstacleTransformer"
    root_dir : "/apollo/modules/perception/production/data/perception/camera/models/multicue_obstacle_transformer"
    config_file : "config.pt"
  }
}
postprocessor_param {
  plugin_param{
    name : "LocationRefinerObstaclePostprocessor"
    root_dir : "/apollo/modules/perception/production/data/perception/camera/models/location_refiner_obstacle_postprocessor"
    config_file : "config.pt"
  }
}

lane_param {
  lane_detector_param {
    plugin_param {
      name : "DenselineLaneDetector"
      root_dir : "/apollo/modules/perception/production/data/perception/camera/models/lane_detector/"
      config_file : "config.pt"
    }
    camera_name : "front_6mm"
  }
  lane_postprocessor_param {
    name : "DenselineLanePostprocessor"
    root_dir : "/apollo/modules/perception/production/data/perception/camera/models/lane_postprocessor/denseline/"
    config_file : "config.pt"
  }
}

lane_param {
  lane_detector_param {
    plugin_param {
      name : "DenselineLaneDetector"
      root_dir : "/apollo/modules/perception/production/data/perception/camera/models/lane_detector/"
      config_file : "config.pt"
    }
    camera_name : "front_12mm"
  }
  lane_postprocessor_param {
    name : "DenselineLanePostprocessor"
    root_dir : "/apollo/modules/perception/production/data/perception/camera/models/lane_postprocessor/denseline/"
    config_file : "config.pt"
  }
}


calibration_service_param {
  plugin_param {
    name : "OnlineCalibrationService"
    root_dir : ""
    config_file : ""
  }
  calibrator_method : "LaneLineCalibrator"
}

object_template_param {
  plugin_param{
    name : "ObjectTemplate"
    root_dir : "/apollo/modules/perception/production/data/perception/camera/common/object_template/"
    config_file : <!--this file list the modules which will be loaded dynamicly and
    their process name to be running in -->
<cyber>
    <desc>cyber modules list config</desc>
    <version>1.0.0</version>
    <!-- sample module config, and the files should have relative path like
         ./bin/cyber_launch
         ./bin/mainboard
         ./conf/dag_streaming_0.conf -->

    <module>
        <name>perception</name>
        <dag_conf>/apollo/modules/perception/production/dag/dag_streaming_perception.dag</dag_conf>
        <!-- if not set, use default process -->
        <process_name>lidar_perception</process_name>
        <version>1.0.0</version>
    </module>
    <module>
        <name>perception_camera</name>
        <dag_conf>/apollo/modules/perception/production/dag/dag_streaming_perception_camera.dag</dag_conf>
        <!-- if not set, use default process -->
        <process_name>camera_perception</process_name>
        <version>1.0.0</version>
    </module>
    <module>
        <name>motion_service</name>
        <dag_conf>/apollo/modules/perception/production/dag/dag_motion_service.dag</dag_conf>
        <!-- if not set, use default process -->
        <process_name>motion_service</process_name>
        <version>1.0.0</version>
    </module>
</cyber>

```

```
//modules/perception/production/launch/perception.launch


<!--this file list the modules which will be loaded dynamicly and
    their process name to be running in -->
<cyber>
    <desc>cyber modules list config</desc>
    <version>1.0.0</version>
    <!-- sample module config, and the files should have relative path like
         ./bin/cyber_launch
         ./bin/mainboard
         ./conf/dag_streaming_0.conf -->

    <module>
        <name>perception</name>
        <dag_conf>/apollo/modules/perception/production/dag/dag_streaming_perception.dag</dag_conf>
        <!-- if not set, use default process -->
        <process_name>lidar_perception</process_name>
        <version>1.0.0</version>
    </module>
    <module>
        <name>perception_camera</name>
        <dag_conf>/apollo/modules/perception/production/dag/dag_streaming_perception_camera.dag</dag_conf>
        <!-- if not set, use default process -->
        <process_name>camera_perception</process_name>
        <version>1.0.0</version>
    </module>
    <module>
        <name>motion_service</name>
        <dag_conf>/apollo/modules/perception/production/dag/dag_motion_service.dag</dag_conf>
        <!-- if not set, use default process -->
        <process_name>motion_service</process_name>
        <version>1.0.0</version>
    </module>
</cyber>

```