
float32 voltage          # Voltage in Volts (Mandatory)
float32 current          # Negative when discharging (A)  (If unmeasured NaN)
float32 charge           # Current charge in Wh  (If unmeasured NaN)
float32 capacity         # Capacity in Wh (last full capacity)  (If unmeasured NaN)
float32 design_capacity  # Capacity in Wh (design capacity)  (If unmeasured NaN)
float32 percentage       # Charge percentage on 0 to 1 range  (If unmeasured NaN)
float32[] cell_voltage   # An array of individual cell voltages for each cell in the pack