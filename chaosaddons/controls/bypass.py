__doc__ = """
Sets the `dry` property on activities that match either by type or by names.

This allows to bypass some activities in certain contexts. For instance, you
want to run on development but not in production certain actions.

For instance, to bypass the execution of the `say-hello` activity:

```json
"controls": [
        {
            "name": "bypass-actions",
            "provider": {
                "type": "python",
                "module": "chaosaddons.controls.bypass",
                "arguments": {
                    "target_names": [
                        "say-hello"
                    ]
                }
            }
        }
    ],
```

For instance, to bypass the execution of all actions in the experiment:

```json
"controls": [
        {
            "name": "bypass-actions",
            "provider": {
                "type": "python",
                "module": "chaosaddons.controls.bypass",
                "arguments": {
                    "target_type": "action"
                }
            }
        }
    ],
```
"""
from typing import List

from chaoslib.types import Activity
from logzero import logger


def before_experiment_control(target_type: str = None,
                              target_names: List[str] = None, **kwargs):
    if target_type:
        logger.warning(
            "No '{}' will be executed as configured by the bypass "
            "control".format(target_type))
    if target_names:
        logger.warning(
            "The following activities will not be executed: {}".format(
                ", ".join(target_names)))


def before_activity_control(context: Activity, target_type: str = None,
                            target_names: List[str] = None):
    """
    Sets the `dry` property on the activity so it is not actually executed
    """
    if target_type and context["type"] == target_type:
        context["dry"] = True
    if target_names and context["name"] in target_names:
        context["dry"] = True


def after_activity_control(context: Activity, target_type: str = None,
                           target_names: List[str] = None):
    """
    Removes the `dry` property that was previously set
    """
    if target_type and context["type"] == target_type:
        context.pop("dry", None)
    if target_names and context["name"] in target_names:
        context.pop("dry", None)
