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


set(MSGS_FILES
"msg/BatteryState.msg"
"msg/ExecuteAtom.msg"
"msg/PlatformState.msg"
"msg/ActionsVLN.msg"
"msg/FrameData.msg"
"msg/UserCommand.msg"
"msg/PlatformCommand.msg"
"msg/ObjectKnowledge.msg"
"msg/PlatformClass.msg"
"msg/SearchMission.msg"
"msg/SensorMode.msg"
"msg/Area.msg"
"msg/PlatformCapabilities.msg"
"msg/SensorCapabilities.msg"
"msg/Waypoints.msg"
"msg/ActionInstance.msg"
"msg/Plan.msg"
"msg/KnowledgeChange.msg"
"msg/AltitudeLevel.msg"
"msg/PlannerCommand.msg"
"msg/ExecutorCommand.msg"
"msg/ExecutorState.msg"
"msg/ExecutionInfo.msg"
"msg/GoalCondition.msg"
"msg/Goal.msg"
"msg/Constraint.msg"
"msg/PlanStatus.msg"
"msg/ActionStatus.msg"
"msg/ClientInfo.msg"
)

set(SRVS_FILES
"srv/CancelGoal.srv"
"srv/GetOrigin.srv"
"srv/SetOrigin.srv"
"srv/StringCommand.srv"
"srv/GetAltitude.srv"
"srv/GetHeighestPoint.srv"
"srv/GetLocationsROI.srv"
"srv/AddAction.srv"
"srv/AddActionString.srv"
"srv/ExistsKnowledge.srv"
"srv/InsertKnowledge.srv"
"srv/QueryKnowledge.srv"
"srv/UpdateKnowledge.srv"
"srv/DeleteKnowledge.srv"
"srv/WriteKnowledge.srv"
)

set(ACTION_FILES
"action/ExecuteSequence.action"
)

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
