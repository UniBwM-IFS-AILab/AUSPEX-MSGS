#!/usr/bin/env python3
import os

if os.getenv('MSG_CONTEXT') == 'MENTHON':
    from hat_menthon.msg import Area, FrameData, PlatformState, PlatformCapabilities, PlatformClass, SearchMission, SensorCapabilities, SensorMode, UserCommand, Waypoints, BatteryState
    from auspex_msgs.msg import ActionInstance, ActionsVLN, ExecuteAtom, KnowledgeChange, ObjectKnowledge, Plan, ActionStatus
else:
    from auspex_msgs.msg import Area, FrameData, PlatformState, PlatformCapabilities, PlatformClass, SearchMission, SensorCapabilities, SensorMode, UserCommand, Waypoints, BatteryState
    from auspex_msgs.msg import ActionInstance, ActionsVLN, ExecuteAtom, KnowledgeChange, ObjectKnowledge, Plan, ActionStatus
