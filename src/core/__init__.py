from .check_gpu import GPUDeviceChecker


def main() -> None:
    checker = GPUDeviceChecker()
    checker.detect_device()
    checker.run_test_tensor()
