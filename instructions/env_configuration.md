# Project Setup Guide for "Modern ML" Course

## Course Information
**Title:** Modern ML  
**URL:** [https://fintechscientist.com/courses/modern_ml/](https://fintechscientist.com/courses/modern_ml/)

## UV Library Overview

UV is a modern Python toolchain that includes a package installer, resolver, and project manager. Key benefits:
- Up to 30x faster than pip for package installation
- Built-in project management and dependency isolation
- Reliable dependency resolution with lockfile support
- Standalone binary with no Python requirement

## Setup Instructions

### 1. Install UV

Download and install UV using standalone installers:

```bash
# macOS (Intel) and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone the Repository

```bash
git clone https://github.com/marcusos/modern-ml.git
cd modern-ml
```

### 3. Initialize UV Project

Create a new UV project configuration:

```bash
# Initialize project
uv init
```

This will create:
- `pyproject.toml`: Project metadata and dependencies
- `.uv/`: UV project directory
- `.venv/`: Virtual environment

### 4. Configure Project Dependencies

Edit `pyproject.toml` to add required dependencies:

```toml
[project]
name = "modern-ml"
version = "0.1.0"
dependencies = [
    "pandas",
    "catboost",
    "seaborn",
    "shap",
    "optuna",
    "mlflow",
    "nixtla",
    "mapie",
    "arfs"
]
```

### 5. Install Dependencies

Install project dependencies:

```bash
# Update the env and install dependencies
uv sync
```

### 7. Project Structure

Your project should now have this structure:
```
modern-ml/
├── .venv
│   ├── bin
│   ├── lib
│   └── pyvenv.cfg
├── .python-version
├── README.md
├── hello.py
├── pyproject.toml
└── uv.lock
```

## Common UV Commands

```bash
# Update dependencies
uv update

# Add new dependency
uv add package_name

# Remove dependency
uv remove package_name

# Sync environment with lock file
uv sync

# Use pip from uv
uv pip [command name]

# Generate a requirements from UV
uv pip freeze > requirements.txt
```

## Troubleshooting

1. Permission Issues:
   ```bash
   chmod -R 755 .venv/
   ```

2. Update UV:
   ```bash
   uv self update
   ```

3. Reset Virtual Environment:
   ```bash
   rm -rf .venv/
   uv project venv
   uv project sync
   ```