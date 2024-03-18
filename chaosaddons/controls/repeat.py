import logging
from copy import deepcopy
from typing import List

from chaoslib.types import Activity, Experiment, Run

__all__ = ["after_activity_control"]
logger = logging.getLogger("chaostoolkit")


def after_activity_control(
    context: Activity,
    experiment: Experiment,
    state: Run,
    repeat_count: int = 0,
    break_if_previous_iteration_failed: bool = False,
) -> None:
    """
    Repeat the activity a certain number of times.

    For instance, the following snippet shows how to run the action twice,
    including the original call to the activity.

    ```json
    "method: [
        {
            "type": "action",
            "name": "say-hello",
            "provider": {
                "type": "process",
                "path": "echo",
                "arguments": "hello"
            },
            "controls": [{
                "name": "repeat-me",
                "provider": {
                    "type": "python",
                    "module": "chaosaddons.controls.repeat",
                    "arguments": {
                        "repeat_count": 2
                    }
                }
            }]
        }
    ]

    You may set `break_if_previous_iteration_failed` to stop iterating if
    an activity failed to run. Note it's not about the return value of
    the activity but if it actually executed as planned.

    Note, if `repeat_count` is less than 2, then this is a noop.
    """
    activity = context

    # prevent endless looping
    if "iteration_index" in activity:
        return None

    activity_name = activity["name"]
    activity_type = activity["type"]

    repeat_count = repeat_count - 1
    if repeat_count <= 0:
        logger.debug(
            f"Do not repeat {activity_type} '{activity_name}' when "
            "`repeat_count` is less than 2"
        )
        return None

    logger.debug(
        f"Repeat {activity_type} '{activity_name}' {repeat_count} more times"
    )
    last_status = state.get("status")

    if break_if_previous_iteration_failed and last_status != "succeeded":
        logger.debug(
            "Last iteration failed so stopping our iterations "
            f"of '{activity_name}'"
        )
        return

    hypothesis_activities = experiment.get("steady-state-hypothesis", {}).get(
        "probes", []
    )
    repeat_activity(activity, hypothesis_activities, repeat_count=repeat_count)

    method_activities = experiment.get("method", [])
    repeat_activity(activity, method_activities, repeat_count=repeat_count)

    rollback_activities = experiment.get("rollbacks", [])
    repeat_activity(activity, rollback_activities, repeat_count=repeat_count)


###############################################################################
# Internals
###############################################################################
def repeat_activity(
    activity: Activity, activities: List[Activity], repeat_count: int = 0
) -> None:
    if not activities:
        return

    activity_name = activity["name"]
    copy_activities = activities[:]

    for pos, a in enumerate(copy_activities):
        if a["name"] == activity_name:
            for index in range(1, repeat_count + 1):
                new_activity = deepcopy(activity)
                new_activity["iteration_index"] = index
                activities.insert(pos + index, new_activity)
            break
