#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from high_stakes.events import *

# Open log based on config
config_open_log()


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # Add driver logic here
    # Note that event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")


def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    # Keep turning until a collision
    while not inertial.latest_collision:

        # Turn right and left to the same heading
        for setpoint in [90, 120, 60, 90, -90, -120, -60, -90]:
            trigger_turner.turn(setpoint, FRAME_HEADING_RELATIVE)

            # Give inertial sensor time to settle
            sleep(1000, TimeUnits.MSEC)

            reset_robot_position_and_heading_to_gps()

            if inertial.latest_collision:
                break

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
