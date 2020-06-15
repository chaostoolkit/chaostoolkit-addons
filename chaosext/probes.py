# -*- coding: utf-8 -*-

from chaoslib.exceptions import FailedActivity
from chaoslib.types import Configuration, Secrets


def empty_probe(configuration: Configuration = None, secrets: Secrets = None):
    return True
