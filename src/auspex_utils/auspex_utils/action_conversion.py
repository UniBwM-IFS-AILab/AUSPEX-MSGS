"""
Utilities for converting simple action definitions into auspex_msgs/Action.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Type

from auspex_msgs.msg import Action

@dataclass
class BaseAction:
    """Base representation of an executable action with string arguments."""

    name: str
    task_id: int = 0
    id: int = 0
    status: str = None
    args: List[str] = field(default_factory=list)

    def to_action_msg(self) -> Action:
        """Create an Action message from this action description."""
        msg = Action()
        msg.name = self.name
        msg.args = list(self.args)
        msg.task_id = self.task_id
        msg.status = self.status
        msg.id = self.id
        return msg


# ============================================================================
# Action implementations start here. Add new action classes below this line.
# ============================================================================
class TakeOffAction(BaseAction):
    """Action for takeoff with a single height in meters above ground level (AGL) argument."""

    ACTION_NAME = "take_off"
    height_m_agl: Optional[float]

    def __init__(
        self,
        height_m_agl: Optional[float] = None,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.height_m_agl = float(arg_list[0])
            else:
                self.height_m_agl = float(height_m_agl)
                arg_list = [str(height_m_agl)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc

        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class LandAction(BaseAction):
    """Action for landing"""

    ACTION_NAME = "land"

    def __init__(
        self,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []
        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class Fly2DAction(BaseAction):
    """Action for flying 2D to a specified GPS point"""

    ACTION_NAME = "fly_2D"

    from_lat: float
    from_lon: float
    to_lat: float
    to_lon: float
    speed_m_s: float
    heading_offset_deg: float
    goal_yaw_deg: float

    def __init__(
        self,
        from_lat: float = 0.0,
        from_lon: float = 0.0,
        to_lat: float = 0.0,
        to_lon: float = 0.0,
        speed_m_s: float = 5.0,
        heading_offset_deg: float = 0.0,
        goal_yaw_deg: float = 0.0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.from_lat = float(arg_list[0])
                self.from_lon = float(arg_list[1])
                self.to_lat = float(arg_list[2])
                self.to_lon = float(arg_list[3])
                self.speed_m_s = float(arg_list[4])
                self.heading_offset_deg = float(arg_list[5])
                self.goal_yaw_deg = float(arg_list[6])
            else:
                self.from_lat = float(from_lat)
                self.from_lon = float(from_lon)
                self.to_lat = float(to_lat)
                self.to_lon = float(to_lon)
                self.speed_m_s = float(speed_m_s)
                self.heading_offset_deg = float(heading_offset_deg)
                self.goal_yaw_deg = float(goal_yaw_deg)
                arg_list = [str(from_lat), str(from_lon), str(to_lat), str(to_lon), str(speed_m_s), str(heading_offset_deg), str(goal_yaw_deg)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc
        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class Fly3DAction(BaseAction):
    """Action for flying 3D to a specified gps point"""

    ACTION_NAME = "fly_3D"

    from_lat: float
    from_lon: float
    from_alt_m_amsl: float
    to_lat: float
    to_lon: float
    to_alt_m_amsl: float
    speed_m_s: float
    heading_offset_deg: float
    goal_yaw_deg: float

    def __init__(
        self,
        from_lat: float = 0.0,
        from_lon: float = 0.0,
        from_alt_m_amsl: float = 0.0,
        to_lat: float = 0.0,
        to_lon: float = 0.0,
        to_alt_m_amsl: float = 0.0,
        speed_m_s: float = 5.0,
        heading_offset_deg: float = 0.0,
        goal_yaw_deg: float = 0.0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.from_lat = float(arg_list[0])
                self.from_lon = float(arg_list[1])
                self.from_alt_m_amsl = float(arg_list[2])
                self.to_lat = float(arg_list[3])
                self.to_lon = float(arg_list[4])
                self.to_alt_m_amsl = float(arg_list[5])
                self.speed_m_s = float(arg_list[6])
                self.heading_offset_deg = float(arg_list[7])
                self.goal_yaw_deg = float(arg_list[8])
            else:
                self.from_lat = float(from_lat)
                self.from_lon = float(from_lon)
                self.from_alt_m_amsl = float(from_alt_m_amsl)
                self.to_lat = float(to_lat)
                self.to_lon = float(to_lon)
                self.to_alt_m_amsl = float(to_alt_m_amsl)
                self.speed_m_s = float(speed_m_s)
                self.heading_offset_deg = float(heading_offset_deg)
                self.goal_yaw_deg = float(goal_yaw_deg)
                arg_list = [str(from_lat), str(from_lon), str(from_alt_m_amsl), str(to_lat), str(to_lon), str(to_alt_m_amsl), str(speed_m_s), str(heading_offset_deg), str(goal_yaw_deg)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc
        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class FlyStep3DAction(BaseAction):
    """Action for flying a 3D step to a specified gps point with altitude.
    Arguments are latitude, longitude, altitude in meters above mean sea level (AMSL)"""

    ACTION_NAME = "fly_step_3D"

    from_lat: float
    from_lon: float
    from_alt_m_amsl: float
    to_lat: float
    to_lon: float
    to_alt_m_amsl: float
    speed_m_s: float
    heading_offset_deg: float
    goal_yaw_deg: float

    def __init__(
        self,
        from_lat: float = 0.0,
        from_lon: float = 0.0,
        from_alt_m_amsl: float = 0.0,
        to_lat: float = 0.0,
        to_lon: float = 0.0,
        to_alt_m_amsl: float = 0.0,
        speed_m_s: float = 5.0,
        heading_offset_deg: float = 0.0,
        goal_yaw_deg: float = 0.0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.from_lat = float(arg_list[0])
                self.from_lon = float(arg_list[1])
                self.from_alt_m_amsl = float(arg_list[2])
                self.to_lat = float(arg_list[3])
                self.to_lon = float(arg_list[4])
                self.to_alt_m_amsl = float(arg_list[5])
                self.speed_m_s = float(arg_list[6])
                self.heading_offset_deg = float(arg_list[7])
                self.goal_yaw_deg = float(arg_list[8])
            else:
                self.from_lat = float(from_lat)
                self.from_lon = float(from_lon)
                self.from_alt_m_amsl = float(from_alt_m_amsl)
                self.to_lat = float(to_lat)
                self.to_lon = float(to_lon)
                self.to_alt_m_amsl = float(to_alt_m_amsl)
                self.speed_m_s = float(speed_m_s)
                self.heading_offset_deg = float(heading_offset_deg)
                self.goal_yaw_deg = float(goal_yaw_deg)
                arg_list = [str(from_lat), str(from_lon), str(from_alt_m_amsl), str(to_lat), str(to_lon), str(to_alt_m_amsl), str(speed_m_s), str(heading_offset_deg), str(goal_yaw_deg)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc
        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class FlyAtDistance2GroundAction(BaseAction):
    """Action for flying with a given distance to the ground between two GPS points.
    Arguments are from_lat, from_lon, from_alt_m_amsl, to_lat, to_lon, distance_m, speed_m_s, heading_offset_deg, goal_yaw_deg"""

    ACTION_NAME = "fly_at_distance_2_ground"

    from_lat: float
    from_lon: float
    from_alt_m_amsl: float
    to_lat: float
    to_lon: float
    distance_m: float
    speed_m_s: float
    heading_offset_deg: float
    goal_yaw_deg: float

    def __init__(
        self,
        from_lat: float = 0.0,
        from_lon: float = 0.0,
        from_alt_m_amsl: float = 0.0,
        to_lat: float = 0.0,
        to_lon: float = 0.0,
        distance_m: float = 0.0,
        speed_m_s: float = 5.0,
        heading_offset_deg: float = 0.0,
        goal_yaw_deg: float = 0.0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.from_lat = float(arg_list[0])
                self.from_lon = float(arg_list[1])
                self.from_alt_m_amsl = float(arg_list[2])
                self.to_lat = float(arg_list[3])
                self.to_lon = float(arg_list[4])
                self.distance_m = float(arg_list[5])
                self.speed_m_s = float(arg_list[6])
                self.heading_offset_deg = float(arg_list[7])
                self.goal_yaw_deg = float(arg_list[8])
            else:
                self.from_lat = float(from_lat)
                self.from_lon = float(from_lon)
                self.from_alt_m_amsl = float(from_alt_m_amsl)
                self.to_lat = float(to_lat)
                self.to_lon = float(to_lon)
                self.distance_m = float(distance_m)
                self.speed_m_s = float(speed_m_s)
                self.heading_offset_deg = float(heading_offset_deg)
                self.goal_yaw_deg = float(goal_yaw_deg)
                arg_list = [str(from_lat), str(from_lon), str(from_alt_m_amsl), str(to_lat), str(to_lon), str(distance_m), str(speed_m_s), str(heading_offset_deg), str(goal_yaw_deg)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc
        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class OpenServoAction(BaseAction):
    """Action for setting servo at channel channel to open."""

    ACTION_NAME = "open_servo"
    channel: int

    def __init__(
        self,
        channel: int = 0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.channel = int(arg_list[0])
            else:
                self.channel = int(channel)
                arg_list = [str(channel)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc

        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class CloseServoAction(BaseAction):
    """Action for setting servo at channel channel to close."""

    ACTION_NAME = "close_servo"
    channel: int

    def __init__(
        self,
        channel: int = 0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.channel = int(arg_list[0])
            else:
                self.channel = int(channel)
                arg_list = [str(channel)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc

        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class HoverAction(BaseAction):
    """Action for hovering in place for a specified duration in milliseconds."""

    ACTION_NAME = "hover"
    duration_ms: int

    def __init__(
        self,
        duration_ms: int = 0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.duration_ms = int(arg_list[0])
            else:
                self.duration_ms = int(duration_ms)
                arg_list = [str(duration_ms)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc

        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class IdleAction(BaseAction):
    """Action for waiting for a specified duration in milliseconds."""

    ACTION_NAME = "idle"
    duration_ms: int

    def __init__(
        self,
        duration_ms: int = 0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.duration_ms = int(arg_list[0])
            else:
                self.duration_ms = int(duration_ms)
                arg_list = [str(duration_ms)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc

        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class CircleGPSAction(BaseAction):
    """Action for circling around a GPS point at a specified radius and altitude.
    Arguments are latitude, longitude, altitude in meters above mean sea level (AMSL), radius in meters, speed in m/s."""

    ACTION_NAME = "circle_gps"
    lat: float
    lon: float
    alt_m_amsl: float
    radius_m: float
    speed_m_s: float
    duration_ms: int

    def __init__(
        self,
        lat: float = 0.0,
        lon: float = 0.0,
        alt_m_amsl: float = 0.0,
        radius_m: float = 0.0,
        speed_m_s: float = 5.0,
        duration_ms: int = 0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.lat = float(arg_list[0])
                self.lon = float(arg_list[1])
                self.alt_m_amsl = float(arg_list[2])
                self.radius_m = float(arg_list[3])
                self.speed_m_s = float(arg_list[4])
                self.duration_ms = int(arg_list[5])
            else:
                self.lat = float(lat)
                self.lon = float(lon)
                self.alt_m_amsl = float(alt_m_amsl)
                self.radius_m = float(radius_m)
                self.speed_m_s = float(speed_m_s)
                self.duration_ms = int(duration_ms)
                arg_list = [str(lat), str(lon), str(alt_m_amsl), str(radius_m), str(speed_m_s), str(duration_ms)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc

        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class AscendAction(BaseAction):
    """Ascend action for ascending by a specified height in meters. Arguments are alt_level (amsl|agl|rel) and height in meters."""

    ACTION_NAME = "ascend"
    alt_m_amsl: float

    def __init__(
        self,
        alt_m_amsl: float = 0.0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.alt_m_amsl = float(arg_list[0])
            else:
                self.alt_m_amsl = float(alt_m_amsl)
                arg_list = [str(alt_m_amsl)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc

        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class DescendAction(BaseAction):
    """Descend action for descending by a specified height in meters. Arguments are alt_level (amsl|agl|rel) and height in meters."""

    ACTION_NAME = "descend"
    alt_m_amsl: float

    def __init__(
        self,
        alt_m_amsl: float = 0.0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.alt_m_amsl = float(arg_list[0])
            else:
                self.alt_m_amsl = float(alt_m_amsl)
                arg_list = [str(alt_m_amsl)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc

        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class TurnAction(BaseAction):
    """Turn action for turning. Turn rel to current orientation (+ is clockwise)."""

    ACTION_NAME = "turn"
    yaw_deg: float

    def __init__(
        self,
        yaw_deg: float = 0.0,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []

        try:
            if arg_list:
                self.yaw_deg = float(arg_list[0])
            else:
                self.yaw_deg = float(yaw_deg)
                arg_list = [str(yaw_deg)]
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid arguments for " + self.ACTION_NAME) from exc

        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class StartDetectionAction(BaseAction):
    """Start detection action for starting object detection."""

    ACTION_NAME = "start_detection"

    def __init__(
        self,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []
        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class StopDetectionAction(BaseAction):
    """Stop detection action for stopping object detection."""

    ACTION_NAME = "stop_detection"

    def __init__(
        self,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []
        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class CaptureImageAction(BaseAction):
    """Capture image action for capturing an image."""

    ACTION_NAME = "capture_image"

    def __init__(
        self,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []
        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class SetWiFiOnAction(BaseAction):
    """Sets WiFi on action for enabling WiFi.   """

    ACTION_NAME = "set_wifi_on"

    def __init__(
        self,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []
        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

class SetWiFiOffAction(BaseAction):
    """Sets WiFi off action for disabling WiFi.   """

    ACTION_NAME = "set_wifi_off"

    def __init__(
        self,
        id: int = 0,
        task_id: int = 0,
        status: str = None,
        args: Optional[Sequence[str]] = None,
    ) -> None:

        arg_list = list(args) if args is not None else []
        super().__init__(name=self.ACTION_NAME, id=id, task_id=task_id, status=status, args=arg_list)

# ============================================================================
# Action implementations end here. Update ACTION_REGISTRY when adding actions.
# ============================================================================


# Registry mapping action_name -> action class
ACTION_REGISTRY: Dict[str, Type[BaseAction]] = {
    TakeOffAction.ACTION_NAME: TakeOffAction,
    LandAction.ACTION_NAME: LandAction,
    FlyStep3DAction.ACTION_NAME: FlyStep3DAction,
    Fly2DAction.ACTION_NAME: Fly2DAction,
    Fly3DAction.ACTION_NAME: Fly3DAction,
    FlyAtDistance2GroundAction.ACTION_NAME: FlyAtDistance2GroundAction,
    OpenServoAction.ACTION_NAME: OpenServoAction,
    CloseServoAction.ACTION_NAME: CloseServoAction,
    HoverAction.ACTION_NAME: HoverAction,
    CircleGPSAction.ACTION_NAME: CircleGPSAction,
    IdleAction.ACTION_NAME: IdleAction,
    AscendAction.ACTION_NAME: AscendAction,
    DescendAction.ACTION_NAME: DescendAction,
    TurnAction.ACTION_NAME: TurnAction,
    StartDetectionAction.ACTION_NAME: StartDetectionAction,
    StopDetectionAction.ACTION_NAME: StopDetectionAction,
    CaptureImageAction.ACTION_NAME: CaptureImageAction,
    SetWiFiOnAction.ACTION_NAME: SetWiFiOnAction,
    SetWiFiOffAction.ACTION_NAME: SetWiFiOffAction,
}


def create_action_from_msg(action_msg: Action) -> BaseAction:
    """Create an action instance from a received Action message."""
    try:
        action_cls = ACTION_REGISTRY[action_msg.name]
    except KeyError as exc:
        raise ValueError(f"Unknown action '{action_msg.name}'") from exc

    return action_cls(id=action_msg.id, task_id=action_msg.task_id, status=action_msg.status, args=action_msg.args)

