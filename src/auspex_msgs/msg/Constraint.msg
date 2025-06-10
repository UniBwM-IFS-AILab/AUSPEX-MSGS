string constraint_id                                                # Unique identifier for this constraint

string type                                                         # Type of constraint (e.g., "SPATIAL", "TEMPORAL", "RESOURCE", "SAFETY")

string description                                                  # Human-readable description

# Constraint-specific parameters stored as a JSON string
# Examples:
# For SPATIAL: {"min_altitude": 10, "max_altitude": 30, "boundary_polygon": [[lat1, lon1], [lat2, lon2], ...]}
# For TEMPORAL: {"start_time": "2025-03-24T15:00:00Z", "end_time": "2025-03-24T16:00:00Z"}
# For RESOURCE: {"max_battery_usage": 0.8, "min_battery_reserve": 0.2}
string parameters_json

string severity                                                     # Severity of constraint (HARD, SOFT) # HARD: Cannot be violated # SOFT: Can be violated with penalty

float32 violation_cost                                              # For soft constraints, the penalty cost for violation