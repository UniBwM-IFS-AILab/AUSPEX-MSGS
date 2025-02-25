## Representation of an action instance that appears in a plan.

# A unique identifier of the action 
string id

# name of the action
string action_name

# Parameters of the action instance, required to be constants.
up_msgs/Atom[] parameters


# Current status of the action
int8 status

int8 ACTION_INACTIVE = 1
int8 ACTION_ACTIVE = 2
int8 ACTION_COMPLETED = 3
int8 ACTION_ABORTED = 4