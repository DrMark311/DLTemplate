import torch

print("=== Probando PyTorch en Mac ===")

# 1. Verificar la versión de PyTorch
print(f"Versión de PyTorch instalada: {torch.__version__}")

# 2. Verificar si el hardware de Apple (MPS - Metal Performance Shaders) está disponible
if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("¡Éxito! Aceleración por hardware de Apple (MPS) detectada y lista.")
else:
    device = torch.device("cpu")
    print("Aviso: MPS no disponible. Se utilizará el CPU.")

# 3. Hacer una pequeña prueba matemática con tensores en el dispositivo
x = torch.randn(3, 3, device=device)
y = torch.ones(3, 3, device=device)
resultado = x + y

print("Tensor de prueba calculado correctamente en el dispositivo:")
print(resultado)
print("================================")
