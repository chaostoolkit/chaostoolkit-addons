from chaosaddons.controls.repeat import after_activity_control


def test_repeat_n_times_in_hypothesis():
    a = {
        "name": "probe-B",
        "type": "probe",
        "provider": {
            "type": "python",
            "module": "builtins",
            "func": "sum",
            "arguments": {
                "iterable": [6, 7]
            }
        }
    }
    x = {
        "title": "hello",
        "description": "n/a",
        "steady-state-hypothesis": {
            "title": "",
            "probes": [
                {
                    "name": "probe-A",
                    "type": "probe",
                    "provider": {
                        "type": "python",
                        "module": "builtins",
                        "func": "sum",
                        "arguments": {
                            "iterable": [2, 3]
                        }
                    }
                },
                a
            ]
        }
    }

    assert len(x.get("steady-state-hypothesis").get("probes")) == 2
    
    after_activity_control(
        context=a, experiment=x, state={},
        repeat_count=2
    )

    assert len(x.get("steady-state-hypothesis").get("probes")) == 3
    
    after_activity_control(
        context=a, experiment=x, state={},
        repeat_count=2
    )

    assert len(x.get("steady-state-hypothesis").get("probes")) == 4
