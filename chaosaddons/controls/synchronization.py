import threading

__all__ = ["experiment_finished", "after_experiment_control"]


experiment_finished = threading.Event()


def after_experiment_control(**kwargs):
    experiment_finished.set()
