> [!WARNING]
> **Esta es una plantilla.** Por favor, crea un nuevo repositorio a partir de ella para tu proyecto.

# 🚀 PyTorch Deep Learning Template

Plantilla profesional para Inteligencia Artificial y Deep Learning. Compatible con **Windows (CUDA)** y **macOS (Apple Silicon MPS)**.

---

## 📦 1. Requisitos Previos

Necesitas instalar [**uv**](https://docs.astral.sh/uv/), el gestor ultrarrápido de paquetes en Python:

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

*(Reinicia tu terminal después de instalar).*

---

## 🚀 2. Inicialización Rápida

1. **Clona tu nuevo repositorio** y abre la carpeta en la terminal.
2. *(Opcional)* Abre `pyproject.toml` y cambia `name = "dl-project"` por el nombre real de tu proyecto.
3. **Instala todo automáticamente:**
   ```bash
   uv sync
   ```
   > Esto creará la carpeta `.venv` y descargará PyTorch con soporte para GPU automáticamente (CUDA para Windows, MPS para Mac).

---

## 📁 3. Estructura Principal

- `main.py` -> Tu punto de entrada. Escribe tu código aquí.
- `data/` -> Para datasets y CSVs en crudo *(Ignorado por Git)*.
- `checkpoints/` -> Para guardar los pesos y modelos *(Ignorado por Git)*.
- `notebooks/` -> Para experimentación y análisis (Jupyter).
- `src/core/` -> Carpeta base para tus módulos (arquitecturas, utils, etc).

---

## 🛠️ 4. VS Code (Opcional)

- Cuando abras el proyecto, acepta **"Instalar extensiones recomendadas"** (Python, Ruff, Jupyter, etc).
- Tendrás un entorno altamente productivo y con autocompletado inteligente gracias a Pylance.

---

## 📋 5. Comandos Útiles (`uv`)

- **Instalar nueva librería:** `uv add nombre-paquete` (ej. `uv add seaborn`)
- **Ver librerías instaladas:** `uv pip list`
- **Actualizar todo a la última versión:** `uv lock --upgrade && uv sync`

---

## 🐍 6. Cambiar la versión de Python

Si necesitas que tu proyecto corra con otra versión de Python (por ejemplo, bajar a `3.11`):

1. **Consulta las versiones disponibles** ejecutando: `uv python list`
2. **Abre el archivo** `.python-version` y cambia el número a la versión exacta que deseas (ej. `3.11`).
3. **Sincroniza el entorno:** Vuelve a ejecutar `uv sync`.