#!/usr/bin/env python3
import os

if os.getenv('MSG_CONTEXT') == 'MENTHON':
    from hat_menthon.msg import Area, DroneImage, DroneState, Plan, PlatformCapabilities, PlatformClass, SearchMission, SensorCapabilities, SensorMode, UserCommand, Waypoints
    from auspex_msgs.msg import ActionInstance, ActionsVLN, ExecuteAtom, KnowledgeChange, ObjectKnowledge, Plan
else:
    from auspex_msgs.msg import Area, DroneImage, DroneState, Plan, PlatformCapabilities, PlatformClass, SearchMission, SensorCapabilities, SensorMode, UserCommand, Waypoints
    from auspex_msgs.msg import ActionInstance, ActionsVLN, ExecuteAtom, KnowledgeChange, ObjectKnowledge, Plan
