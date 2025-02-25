#An action Atom

#the action type as string
string action_type

#if a waypoint movement is given -> a goal position in GPS
geographic_msgs/GeoPose goal_pose

# Specifies whether altitude of goal_pose.position is in AMSL | AGL | REL
auspex_msgs/AltitudeLevel altitude_level

#search height for seachr area and scan area. Always in AMSL
float32 height

#for hover in position 
float32 hover_duration # in ms

#for scan area -> positions in gps
geometry_msgs/Pose2D[] scan_polygon_vertices

#further parameters

#for circle
float32 radius
float32 speed #in m/s

