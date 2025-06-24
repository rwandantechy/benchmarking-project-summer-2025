# System Configuration

## Hardware
- Target platforms: Embedded/edge devices (e.g., Raspberry Pi), and standard x86_64 systems
- RAM: Minimum 4GB recommended
- CPU: Multi-core (ARM or x86)

## Operating System
- Linux (Debian/Ubuntu recommended)
- macOS (development)
- Windows (WSL2 or native Docker)

## Software Dependencies
- Docker (for containerized model serving)
- Docker Compose (for multi-container orchestration)
- Python 3.8+
- Required Python packages (see `requirements.txt`):
  - numpy, pandas, matplotlib, seaborn
  - psutil, requests, tqdm
  - pytest, black (development)

## Configuration
- All configuration options are managed in `src/config.py` and (optionally) `src/config.json`.
- Key parameters:
  - `memory_test_size`: Size of memory test (MB)
  - `cpu_test_duration`: Duration of CPU test (seconds)
  - `disk_test_size`: Size of disk test (MB)
  - `verbose`: Enable verbose logging

## Containerization
- Models are served via Docker containers using Ollama.
- The `Dockerfile` and `docker-compose.yml` provide reproducible environments for benchmarking.

---
