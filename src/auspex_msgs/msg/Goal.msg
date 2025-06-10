string goal_id                                                                                  # Unique identifier for this goal

string team_id                                                                                  # Team ID if goal is part of a multi-agent mission

string description                                                                              # Human-readable description

string type                                                                                     # Type of goal (e.g., DETECT, SCAN, MONITOR)

string parameters_json                                                                          # {object":"person", "area":"sector_5", "target":"device_123"} as key value pair

uint8 priority                                                                                  # Priority level (1-10, with 10 being highest)

string[] constraint_ids                                                                         # List of constraint IDs that apply to this goal

auspex_msgs/GoalCondition goal_condition                                                        # If is empty -> leaf node / if not is and or node.

string status                                                                                   # Goal status (PENDING, IN_PROGRESS, COMPLETED, FAILED)

builtin_interfaces/Time created_at                                                              # Timestamp when goal was created

builtin_interfaces/Time deadline                                                                # Deadline for goal completion (if applicable)