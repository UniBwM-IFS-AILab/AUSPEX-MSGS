cmake_minimum_required(VERSION 3.5)
project(auspex_msgs)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geographic_msgs)
find_package(action_msgs REQUIRED)
find_package(upf_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)


# Collect interface files automatically
file(GLOB MSGS_FILES     RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}" CONFIGURE_DEPENDS
  "${CMAKE_CURRENT_SOURCE_DIR}/msg/*.msg")
file(GLOB SRVS_FILES     RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}" CONFIGURE_DEPENDS
  "${CMAKE_CURRENT_SOURCE_DIR}/srv/*.srv")
file(GLOB ACTION_FILES   RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}" CONFIGURE_DEPENDS
  "${CMAKE_CURRENT_SOURCE_DIR}/action/*.action")

# Optional: sort for deterministic builds
list(SORT MSGS_FILES)
list(SORT SRVS_FILES)
list(SORT ACTION_FILES)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${MSGS_FILES}
  ${SRVS_FILES}
  ${ACTION_FILES}
  DEPENDENCIES geometry_msgs upf_msgs sensor_msgs geographic_msgs std_msgs builtin_interfaces ${PROJECT_DEPENDENCIES}
)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
