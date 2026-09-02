import torch

from core.check_gpu import GPUDeviceChecker


def test_gpu_device_checker_initialization():
    """Verifica que la clase se inicialice correctamente."""
    checker = GPUDeviceChecker()
    assert checker.os_name is not None
    assert isinstance(checker.device, torch.device)


def test_detect_device():
    """Verifica que la detección devuelva un objeto de tipo torch.device."""
    checker = GPUDeviceChecker()
    device = checker.detect_device()

    # Debe ser de tipo torch.device
    assert isinstance(device, torch.device)
    # Debe ser uno de los dispositivos soportados
    assert device.type in ["cpu", "cuda", "mps"]


def test_run_test_tensor(capsys):
    """Verifica que la suma de tensores se ejecute sin excepciones."""
    checker = GPUDeviceChecker()
    checker.detect_device()

    # La prueba pasa si esto se ejecuta sin lanzar un error (ej. DeviceMismatch)
    checker.run_test_tensor()

    # Verificamos que generó la salida esperada por consola
    captured = capsys.readouterr()
    assert "Test tensor computed successfully" in captured.out
