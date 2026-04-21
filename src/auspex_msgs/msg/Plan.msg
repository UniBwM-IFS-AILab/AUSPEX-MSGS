string platform_id                          # related platform id
string team_id                              # team_id as string
int8 priority                               # priority of the plan
int64 plan_id                               # unique
string status                               # Current State of the Plan (as name of the enum PlanStatus)
string tpn                                  # The Temporal Plan Network as stringified JSON
upf_msgs/Plan upf_plan                      # The plan in upf format TimeTriggeredPlan
auspex_msgs/Task[] tasks
auspex_msgs/Action[] actions