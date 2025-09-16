# The following commands can be issued to the Executor

int8 EXECUTE = 0                                    # Indicating the executor to start executing
int8 CONTINUE = 1                                   # Indicating the executor to continue executing
int8 PAUSE = 2                                      # Indicating the executor to pause the execution
int8 CANCEL = 3                                     # Indicating the executor to cancel the execution
int8 TERMINATE = 4                                  # Indicating the executor to terminate the execution
int8 KILL = 5                                       # Indicating the executor to kill the execution

string platform_id                                    # Platform ID. If specified command only holds for the platform_id. Must be in team_id.
int8 command                                        # Command