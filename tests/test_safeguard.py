from chaoslib.exceptions import InterruptExecution
import pytest

from chaosaddons.controls.safeguards import configure_control


def test_fail_on_invalid_probes():
    missing_type_probe = {"name": "hello"}
    with pytest.raises(InterruptExecution) as x:
        configure_control(probes=[missing_type_probe])
        assert isinstance(x, InterruptExecution)


def test_fail_on_invalid_probes_with_unknown_python_function():
    invalid_python_func_probe = {
        "name": "hello",
        "type": "probe",
        "provider": {
            "type": "python",
            "module": "os",
            "func": "whatever"
        }}
    with pytest.raises(InterruptExecution) as x:
        configure_control(probes=[invalid_python_func_probe])
        assert isinstance(x, InterruptExecution)
