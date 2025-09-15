std_msgs/Header header                          # header for time stamps (#2)

string platform_id                              # unique platform id (#1)
string team_id                                  # associated team id (#1)

geographic_msgs/GeoPoint platform_gps_position  # in WGS84 coordinates (#3)

geometry_msgs/Pose platform_pose    	        # in world coordinates (#4)

string platform_status                          # e.g current performing action (#5)

BatteryState battery_state          # the battery state of the platform

string sensor_id                                # id of the current selected sensor (#6)

geometry_msgs/Point sensor_position             # sensor position relative to platform (#7)

int16 fov_hor                                   # in degrees (#8)
int16 fov_vert                                  # in degrees (#8)
uint8 zoom_level                                # zoom level (#8)

geometry_msgs/Vector3 gimbal_orientation        # relative to platform in degrees (#9)
float64 elevation_angle                         # angle of the gimbal in [-180,180] to ground (#9)
float64 azimuth_angle                           # angle of the gimbal in [0, 360] to true north (#9)

SensorMode sensor_mode                          # mode of the current selected sensor (#10)
