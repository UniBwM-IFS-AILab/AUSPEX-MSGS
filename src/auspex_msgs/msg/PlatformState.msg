std_msgs/Header header                          # header for time stamps

string platform_id                              # unique platform id
string platform_ip                              # unique platform ip
string team_id                                  # associated team id

geographic_msgs/GeoPoint platform_gps_position  # in WGS84 coordinates

geometry_msgs/Pose platform_pose    	        # in local NED coordinates
float32 yaw_deg                                 # yaw angle in degrees
float32 pitch_deg                               # pitch angle in degrees
float32 roll_deg                                # roll angle in degrees

string platform_status                          # e.g current performing action

BatteryState battery_state          # the battery state of the platform
