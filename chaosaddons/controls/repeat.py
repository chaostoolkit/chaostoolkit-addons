from copy import deepcopy
from typing import List

from chaoslib.types import Activity, Experiment,  Run
from logzero import logger

__all__ = ["after_activity_control"]


def after_activity_control(context: Activity, experiment: Experiment,
                           state: Run, repeat_count: int = 0,
                           break_if_previous_iteration_failed: bool = False
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
    """
    activity = context
    activity_name = activity["name"]
    repeat_count = repeat_count - 1
    last_status = state.get("status")

    if break_if_previous_iteration_failed and last_status != "succeeded":
        logger.debug(
            "Last iteration failed so stopping our iterations "
            f"of '{activity_name}'")
        return

    hypothesis_activities = experiment.get(
        "steady-state-hypothesis", {}).get("probes", [])
    repeat_activity(
        activity, hypothesis_activities, repeat_count=repeat_count)

    method_activities = experiment.get("method", [])
    repeat_activity(
        activity, method_activities, repeat_count=repeat_count)

    rollback_activities = experiment.get("rollbacks", [])
    repeat_activity(
        activity, rollback_activities, repeat_count=repeat_count)


###############################################################################
# Internals
###############################################################################
def repeat_activity(activity: Activity, activities: List[Activity],
                    repeat_count: int = 0) -> None:
    if not activities:
        return

    activity_name = activity["name"]

    for a in reversed(activities):
        if a["name"] == activity_name:
            activity = deepcopy(activity)
            if "iteration_index" not in activity:
                activity["iteration_index"] = 1
            else:
                if activity["iteration_index"] == repeat_count:
                    return
                activity["iteration_index"] += 1

            activities.append(activity)
            break
