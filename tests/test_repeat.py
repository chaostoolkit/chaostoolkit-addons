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


def test_repeat_once():
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
        "method": [
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
                a,
                {
                    "name": "probe-C",
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
            ]
    }

    assert len(x.get("method")) == 3
    
    after_activity_control(
        context=a, experiment=x, state={},
        repeat_count=2
    )

    assert len(x.get("method")) == 4


def test_repeat_inserts():
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
        "method": [
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
                a,
                {
                    "name": "probe-C",
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
                {
                    "name": "probe-D",
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
            ]
    }

    assert len(x.get("method")) == 4
    
    after_activity_control(
        context=a, experiment=x, state={},
        repeat_count=3
    )

    assert len(x.get("method")) == 6

    m = x.get("method")
    assert m[0]["name"] == "probe-A"
    assert m[1]["name"] == "probe-B"
    assert m[2]["name"] == "probe-B"
    assert m[3]["name"] == "probe-B"
    assert m[4]["name"] == "probe-C"
    assert m[5]["name"] == "probe-D"
