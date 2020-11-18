import threading

__all__ = ["experiment_finished"]


experiment_finished = threading.Event()


def after_experiment_control(**kwargs):
    experiment_finished.set()
