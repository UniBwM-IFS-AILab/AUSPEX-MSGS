std_msgs/Header header                      # header for time stamps

string team_id                              # associated team id

PlatformClass platform_class                # class of platform this mission is meant for

Area search_area                            # in WGS84 coordinates

Area[] no_fly_zones                         # in WGS84 coordinates

uint16 max_height                           # in m AGL

uint16 min_height                           # in m AGL

uint16 desired_ground_dist                  # in m above ground

geographic_msgs/GeoPoint starting_point     # in WGS84 coordinates

string[] target_objects                     # a list of objects to be searched for

string mission_goal                         # as string

geographic_msgs/GeoPoint[] pois             # in WGS84 coordinates

Area[] prio_areas                           # in WGS84 coordinates

SensorMode sensor_mode                      # mode to scan this area with

Area[] danger_zones                         # in WGS84 coordinates
