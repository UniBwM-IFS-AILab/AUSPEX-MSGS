## Representation of an action instance that appears in a plan.

int8 id   	                    # A unique identifier of the action

string action_name              # name of the action

int8 task_id                  # if an action the task it was planned from

upf_msgs/Atom[] parameters      # Parameters of the action instance, required to be constants.

string  status                  # Current status of the action as ActionStatus.msg