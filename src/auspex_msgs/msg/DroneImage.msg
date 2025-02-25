string platform_id                              # unique platform id (#1)
string team_id                                  # associated team id (#1)

sensor_msgs/CompressedImage image_compressed    # the compressed image message
int32 fps                                       # frames per seconds
int32 res_width                                 # resolution
int32 res_height                                # resolution
geographic_msgs/GeoPoint gps_position           # gps position