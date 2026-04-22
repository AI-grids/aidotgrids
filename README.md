# aidotgrids

## Overview

1. [Quick start](#1-quick-start)
2. [Prerequisites](#2-prerequisites)
3. [Datasets](#3-datasets)
4. [Running tests](#4-running-tests)
5. [Contributions](#5-contributions)
6. [License](#6-license)


## 1. Quick start

### (Option A) Use the stable ai4climate release (recommended)

```bash
pip install -U aidotgrids
```

### (Option B) Use the bleeding‑edge version bundled with this repo

```bash
git clone https://github.com/AI-grids/aidotgrids
cd aidotgrids

pip uninstall -y aidotgrids         # ensure the PyPI version is removed
export PYTHONPATH=$PYTHONPATH:$(pwd)/aidotgrids
```

## 2. Prerequisites

| Dependency | Version     |
| ---------- | ----------- |
| Python     | ≥ 3.9       |
| PyTorch    | ≥ 2.2       |
| CUDA (opt) | 11.8 / 12.X |

Create a clean environment (example with conda):

```bash
conda create -n aidotgrids python=3.10 pytorch=2.2 cudatoolkit=11.8 -c pytorch -y
conda activate aidotgrids
```

## 3. Datasets

All standardized tasks are hosted on Hugging Face Hub and can be downloaded 
automatically via `aidotgrids.load`. Current coverage:

| Task / Dataset          | Modality                    | Docs                                   |
| ----------------------- | --------------------------- | -------------------------------------- |
| **OPFData**             | Graphs (optimal-power-flow) | [details](docs/opfdata.md)             |
| **PowerGraph**          | Transmission-grid graphs    | [details](docs/powergraph.md)          |
| **SolarCube**           | Satellite imagery           | [details](docs/solarcube.md)           |
| **BuildingElectricity** | Time-series load profiles   | [details](docs/buildingelectricity.md) |
| **WindFarm**            | SCADA & weather             | [details](docs/windfarm.md)            |


Load a dataset in a few lines:

```Python
from aidotgrids import load

ds = load(
    task_name="OPFData",
    subtask_name="train_small_test_medium",
    root_path="~/AI-grids"  # local cache directory
)
```

## 4. Running tests




## 5. Contributions

We welcome pull requests for new datasets, models and algorithms. Please read
[contributions.md](docs/contributions.md) before opening an issue or pull request.


## 6. License

This project is licensed under the MIT license. See [LICENSE](LICENSE) file for details.
