import sys

import torch


class GPUDeviceChecker:
    """Class to check and assign the optimal PyTorch device based on the operating system."""

    def __init__(self) -> None:
        self.os_name: str = sys.platform
        self.device: torch.device = torch.device("cpu")

    def detect_device(self) -> torch.device:
        """Detects the available hardware acceleration based on the OS."""
        print("=== PyTorch Device Checker ===")
        print(f"PyTorch Version: {torch.__version__}")
        print(f"Operating System: {self.os_name}")

        if self.os_name == "darwin":
            self._check_macos_device()
        elif self.os_name == "win32":
            self._check_windows_device()
        else:
            print("Notice: Linux or other OS detected. Checking for CUDA...")
            self._check_cuda_device()

        return self.device

    def _check_macos_device(self) -> None:
        """Checks for MPS (Metal Performance Shaders) availability on macOS."""
        if torch.backends.mps.is_available():
            self.device = torch.device("mps")
            print("Success! Apple Hardware Acceleration (MPS) detected and ready.")
        else:
            self.device = torch.device("cpu")
            print("Notice: MPS not available. Using CPU.")

    def _check_windows_device(self) -> None:
        """Checks for CUDA GPU availability on Windows."""
        self._check_cuda_device()

    def _check_cuda_device(self) -> None:
        """Helper to check for CUDA availability."""
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
            print(
                f"Success! CUDA GPU detected and ready. GPU Name: {torch.cuda.get_device_name(0)}"
            )
        else:
            self.device = torch.device("cpu")
            print("Notice: CUDA GPU not available. Using CPU.")

    def run_test_tensor(self) -> None:
        """Runs a small mathematical test using tensors on the selected device."""
        x = torch.randn(3, 3, device=self.device)
        y = torch.ones(3, 3, device=self.device)
        result = x + y

        print("\nTest tensor computed successfully on the device:")
        print(result)
        print("================================\n")


if __name__ == "__main__":
    checker = GPUDeviceChecker()
    checker.detect_device()
    checker.run_test_tensor()
