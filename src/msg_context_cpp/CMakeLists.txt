cmake_minimum_required(VERSION 3.8)
project(msg_context_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Required dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(auspex_msgs REQUIRED)

# Try to find hat_menthon (optional)
find_package(hat_menthon QUIET)

# Check if MSG_CONTEXT is set to "MENTHON"
if(DEFINED ENV{MSG_CONTEXT} AND "$ENV{MSG_CONTEXT}" STREQUAL "MENTHON")
  set(MSG_CONTEXT_MENTHON TRUE)
else()
  set(MSG_CONTEXT_MENTHON FALSE)
endif()

# Only enable Menthon messages if both conditions are met
if(hat_menthon_FOUND AND MSG_CONTEXT_MENTHON)
  message(STATUS "hat_menthon found and MSG_CONTEXT=MENTHON. Using Menthon messages.")
  add_compile_definitions(HAVE_HAT_MENTHON)
endif()

# Declare interface library
add_library(${PROJECT_NAME} INTERFACE)

target_include_directories(${PROJECT_NAME} INTERFACE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)

# Export dependencies
ament_export_include_directories(include)
ament_export_dependencies(rclcpp auspex_msgs)

if(hat_menthon_FOUND AND MSG_CONTEXT_MENTHON)
  ament_export_dependencies(hat_menthon)
endif()

# Install headers
install(
  DIRECTORY include/
  DESTINATION include
)

# Install interface library
install(
  TARGETS ${PROJECT_NAME}
  EXPORT export_${PROJECT_NAME}
  DESTINATION lib
)

# Export library
ament_export_targets(export_${PROJECT_NAME} HAS_LIBRARY_TARGET)

ament_package()
