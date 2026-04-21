# Message for inter-executor task coordination
# Used to communicate task completion events between platforms

# Event types
int8 EVENT_STARTED = 0          # Task execution has started
int8 EVENT_COMPLETED = 1        # Task execution completed successfully
int8 EVENT_FAILED = 2           # Task execution failed
int8 EVENT_CANCELLED = 3        # Task execution was cancelled

# Header for timestamp
std_msgs/Header header

# Event type
int8 event_type

string event_id                            # Unique Event ID

# Platform that generated the event
string platform_id

# Team this platform belongs to
string team_id

# Plan ID this task belongs to
int64 plan_id

# Additional metadata as JSON
string metadata_json
