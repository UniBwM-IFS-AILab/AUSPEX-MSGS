#ifndef MESSAGE_LOADER_HPP
#define MESSAGE_LOADER_HPP

#ifdef HAVE_HAT_MENTHON  // Defined in CMakeLists.txt if hat_menthon is found AND MSG_CONTEXT=MENTHON
    #include "hat_menthon/msg/user_command.hpp"
    #include "hat_menthon/msg/drone_state.hpp" 
    #include "hat_menthon/msg/sensor_mode.hpp"  
    #include "hat_menthon/msg/platform_capabilities.hpp"  
    #include "hat_menthon/msg/drone_image.hpp"

    using UserCommand = hat_menthon::msg::UserCommand;
    using SensorMode = hat_menthon::msg::SensorMode;
    using DroneState = hat_menthon::msg::DroneState;
    using PlatformCapabilities = hat_menthon::msg::PlatformCapabilities;
    using SensorCapabilities = hat_menthon::msg::SensorCapabilities;
    using PlatformClass = hat_menthon::msg::PlatformClass;
    using DroneImage = hat_menthon::msg::DroneImage;

#else  // Default to auspex_msgs if hat_menthon is not found or MSG_CONTEXT != MENTHON
    #include "auspex_msgs/msg/user_command.hpp"
    #include "auspex_msgs/msg/drone_state.hpp"  
    #include "auspex_msgs/msg/sensor_mode.hpp"  
    #include "auspex_msgs/msg/platform_capabilities.hpp"  
    #include "auspex_msgs/msg/drone_image.hpp"

    using DroneImage = auspex_msgs::msg::DroneImage;
    using UserCommand = auspex_msgs::msg::UserCommand;
    using SensorMode = auspex_msgs::msg::SensorMode;
    using DroneState = auspex_msgs::msg::DroneState;
    using PlatformCapabilities = auspex_msgs::msg::PlatformCapabilities;
    using SensorCapabilities = auspex_msgs::msg::SensorCapabilities;
    using PlatformClass = auspex_msgs::msg::PlatformClass;
#endif

#endif // MESSAGE_LOADER_HPP
