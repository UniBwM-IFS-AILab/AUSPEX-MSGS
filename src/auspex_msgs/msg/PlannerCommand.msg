# The following commands can be issued to the planner

int8 REPLAN = 0                                     # Indicating the planner to REPLAN
int8 RESET = 1                                      # Indicating the planner to reset its plan.
int8 FINISHED = 2                                   # Indicating the planner that a plan is finished
int8 UPDATEPLAN = 3                                 # Indicating the planner that a plan needs an update
int8 FEEDBACK = 4                                   # Indicating the planner to process the feedback
int8 STATE_FEEDBACK = 5                             # Indicating the planner that the executor changed its state
int8 CANCEL_DONE = 6                                # Indicating the planner that the cancel is done
int8 ABORTED = 7                                    # Indicating the planner that the plan was aborted
int8 FAILED = 8                                     # Indicating the planner that the plan failed

int8 command                                        # Command


auspex_msgs/ExecutorState executor_state            # Current State of the Executor
auspex_msgs/ExecutionInfo info                  # Containing the feedback status from the executor