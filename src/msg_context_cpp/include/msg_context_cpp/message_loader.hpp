#ifndef MESSAGE_LOADER_HPP
#define MESSAGE_LOADER_HPP

#ifdef HAVE_HAT_MENTHON  // Defined in CMakeLists.txt if hat_menthon is found AND MSG_CONTEXT=MENTHON
    #include "hat_menthon/msg/user_command.hpp"
    #include "hat_menthon/msg/platform_state.hpp"
    #include "hat_menthon/msg/sensor_mode.hpp"
    #include "hat_menthon/msg/platform_capabilities.hpp"
    #include "hat_menthon/msg/frame_data.hpp"
    #include "hat_menthon/msg/battery_state.hpp"

    using UserCommand = hat_menthon::msg::UserCommand;
    using SensorMode = hat_menthon::msg::SensorMode;
    using PlatformState = hat_menthon::msg::PlatformState;
    using PlatformCapabilities = hat_menthon::msg::PlatformCapabilities;
    using SensorCapabilities = hat_menthon::msg::SensorCapabilities;
    using PlatformClass = hat_menthon::msg::PlatformClass;
    using FrameData = hat_menthon::msg::FrameData;
    using BatteryState = hat_menthon::msg::BatteryState;

#else  // Default to auspex_msgs if hat_menthon is not found or MSG_CONTEXT != MENTHON
    #include "auspex_msgs/msg/user_command.hpp"
    #include "auspex_msgs/msg/platform_state.hpp"
    #include "auspex_msgs/msg/sensor_mode.hpp"
    #include "auspex_msgs/msg/platform_capabilities.hpp"
    #include "auspex_msgs/msg/frame_data.hpp"
    #include "auspex_msgs/msg/battery_state.hpp"

    using UserCommand = auspex_msgs::msg::UserCommand;
    using SensorMode = auspex_msgs::msg::SensorMode;
    using PlatformState = auspex_msgs::msg::PlatformState;
    using PlatformCapabilities = auspex_msgs::msg::PlatformCapabilities;
    using SensorCapabilities = auspex_msgs::msg::SensorCapabilities;
    using PlatformClass = auspex_msgs::msg::PlatformClass;
    using FrameData = auspex_msgs::msg::FrameData;
    using BatteryState = auspex_msgs::msg::BatteryState;
#endif

#endif // MESSAGE_LOADER_HPP
