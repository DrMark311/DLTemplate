# 🚀 PyTorch Multiplatform Deep Learning Template

Plantilla profesional y robusta para proyectos de Inteligencia Artificial, Visión Computacional y Deep Learning. Diseñada para funcionar "Out of the box" con aceleración por hardware tanto en **Windows (NVIDIA CUDA 13.2)** como en **macOS (Apple Silicon MPS)**.

---

## 📦 1. Requisitos Previos (Instalación)

Para garantizar un entorno reproducible, este proyecto utiliza [**uv**](https://docs.astral.sh/uv/) (el gestor de paquetes de Python ultra-rápido escrito en Rust) en lugar de `pip` o `conda`.

### A. Instalar Git y GitHub Desktop
1. Descarga e instala [Git](https://git-scm.com/downloads).
2. (Opcional pero recomendado) Descarga [GitHub Desktop](https://desktop.github.com/) para manejar los repositorios de forma visual.

### B. Instalar `uv`
Ejecuta el siguiente comando en tu terminal dependiendo de tu sistema operativo:

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
*(Reinicia tu terminal después de la instalación para que reconozca el comando).*

---

## 🚀 2. Clonación y Puesta en Marcha

1. **Clona el repositorio** en tu computadora local:
   ```bash
   git clone <url-de-tu-repositorio>
   cd PyTorchOnMac
   ```
2. **Sincroniza el entorno y las dependencias:**
   ```bash
   uv sync
   ```
   *Magia pura:* Si estás en Windows, `uv` descargará automáticamente la versión de PyTorch con **CUDA 13.2**. Si estás en Mac, descargará la versión nativa con soporte para **MPS**.
3. **Verifica que el hardware se detecte correctamente:**
   ```bash
   uv run python src/pytorchonmac/check_gpu.py
   ```

---

## 📁 3. Estructura del Proyecto

Esta plantilla sigue las mejores prácticas arquitectónicas para Deep Learning. El repositorio está diseñado para que **nunca subas datos pesados por accidente a GitHub**, gracias a un estricto blindaje en el `.gitignore`.

```text
PyTorchOnMac/
│
├── 📂 data/               <- 🛑 IGNORADO POR GIT.
│   │                         Pon aquí tus datasets, imágenes, CSVs o bases de datos en crudo.
│   │                         (Ej: data/train_images/, data/labels.csv)
│   
├── 📂 checkpoints/        <- 🛑 IGNORADO POR GIT.
│   │                         Usa esta carpeta para guardar los pesos de tu modelo mientras entrena.
│   │                         (Ej: checkpoints/modelo_epoch_10.pt, modelo_final.safetensors)
│   
├── 📂 notebooks/          <- 💡 Jupyter Notebooks para Análisis Exploratorio (EDA).
│   │                         Ideal para visualizar gráficas, probar transformaciones o 
│   │                         hacer prototipos rápidos antes de pasarlos a producción.
│   
├── 📂 src/pytorchonmac/   <- 💻 CÓDIGO FUENTE DE PRODUCCIÓN.
│   │                         Aquí vive el código del proyecto estructurado en POO (Orientado a Objetos).
│   │
│   ├── check_gpu.py       <- Clase global para inicializar y auto-detectar el dispositivo (MPS/CUDA/CPU).
│   └── __init__.py        
│
├── 📄 AGENTS.md           <- Reglas, estilo de código y directrices de IA para agentes automatizados.
├── 📄 pyproject.toml      <- Configuración maestra del proyecto, dependencias y reglas de linter (Ruff).
└── 📄 uv.lock             <- Archivo generado automáticamente por `uv` (no editar manualmente).
```

---

## 🛠️ 4. Automatización con VSCode

Si usas **Visual Studio Code**, el proyecto ya viene pre-configurado para ti.
1. Al abrir la carpeta en VSCode, dale click en **"Instalar extensiones recomendadas"** (Python, Pylance, Ruff).
2. El editor detectará el entorno virtual (`.venv`) automáticamente.
3. El código se formateará de manera automática (`formatOnSave`) y respetará el mantenimiento de tus librerías gracias a la configuración de `settings.json`.

¡Feliz entrenamiento! 🧠🔥
