## Representation of an task that appears in a plan.

int64 id   	                    # A unique identifier of the action

int64 goal_id                   # The id of the goal this task belongs to

string name                     # name of the task

upf_msgs/Atom[] parameters      # Parameters of the task

string  status                  # Current status of the task as ActionStatus.msg stringified.