from chaoslib.exceptions import InvalidActivity
import pytest

from chaosaddons.controls.safeguards import validate_control


def test_fail_on_invalid_probes():
    invalid_type_probe = {
        "name": "my control",
        "provider": {
            "type": "python",
            "module": "chaosaddons.controls.safeguards",
            "arguments": {
                "probes": [
                    {
                        "name": "my probe",
                        "type": "action",  ## should be a probe
                        "provider": {
                            "type": "python",
                            "module": "os.path",
                            "func": "exists"
                        }
                    }
                ]
            }
        }
    }
    with pytest.raises(InvalidActivity) as x:
        validate_control(invalid_type_probe)


def test_fail_on_invalid_probes_with_unknown_python_function():
    invalid_python_func_probe = {
        "name": "my control",
        "provider": {
            "type": "python",
            "module": "chaosaddons.controls.safeguards",
            "arguments": {
                "probes": [
                    {
                        "name": "my probe",
                        "type": "probe",
                        "provider": {
                            "type": "python",
                            "module": "os.path",
                            "func": "whatever"
                        }
                    }
                ]
            }
        }
    }
    with pytest.raises(InvalidActivity) as x:
        validate_control(invalid_python_func_probe)


def test_fail_on_missing_tolerance():
    invalid_python_func_probe = {
        "name": "my control",
        "provider": {
            "type": "python",
            "module": "chaosaddons.controls.safeguards",
            "arguments": {
                "probes": [
                    {
                        "name": "my probe",
                        "type": "probe",
                        "provider": {
                            "type": "python",
                            "module": "os.path",
                            "func": "exists",
                            "arguments": {
                                "path": "/tmp"
                            }
                        }
                    }
                ]
            }
        }
    }
    with pytest.raises(InvalidActivity) as x:
        validate_control(invalid_python_func_probe)


def test_fail_when_no_probes_were_given():
    invalid_python_func_probe = {
        "provider": {
            "arguments": {
                "probes": [
                    {
                        "name": "my control",
                        "provider": {
                            "type": "python",
                            "module": "chaosaddons.controls.safeguards",
                            "arguments": [
                            ]
                        }
                    }
                ]
            }
        }
    }
    with pytest.raises(InvalidActivity) as x:
        validate_control(invalid_python_func_probe)


def test_journal_records_the_triggering_safeguard():
    from chaosaddons.controls import safeguards

    guardian = safeguards.guardian
    guardian.prepare([])
    try:
        run = {"activity": {"name": "sg"}, "status": "succeeded", "output": 1}
        guardian.interrupt_now("sg", run)
        journal = {}
        safeguards.after_experiment_control(context={}, state=journal)
        assert journal["safeguards"] == {"triggered_by": "sg", "run": run}
    finally:
        guardian.prepare([])
        guardian.terminate()

    journal = {}
    safeguards.after_experiment_control(context={}, state=journal)
    assert "safeguards" not in journal
