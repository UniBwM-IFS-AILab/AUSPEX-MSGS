string platform_id                          # related platform id
string team_id                              # team_id as string
int8 priority                               # priority of the plan
int8 plan_id                              # unique
string status                               # Current State of the Plan (as name of the enum PlanStatus)

auspex_msgs/ActionInstance[] tasks
auspex_msgs/ActionInstance[] actions