std_msgs/Header header                          # header for time stamps (#2)

string platform_id                              # unique platform id (#1)
string platform_ip                              # unique platform ip (#1)
string team_id                                  # associated team id (#1)

geographic_msgs/GeoPoint platform_gps_position  # in WGS84 coordinates (#3)

geometry_msgs/Pose platform_pose    	        # in local NED coordinates (#4)

string platform_status                          # e.g current performing action (#5)

BatteryState battery_state          # the battery state of the platform
