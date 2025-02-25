# enum definition of area type
uint8 AREA_TYPE_NO_FLY = 0              # no fly zone
uint8 AREA_TYPE_SEARCH = 1              # search area
uint8 AREA_TYPE_DANGER = 2              # danger area (e.g. bad weather)
uint8 AREA_TYPE_H_PRIO = 3              # high prio search area

uint8 type                              # area type enum value

string description                      # area description

geographic_msgs/GeoPoint[] points       # in lat, lon, m AGL
