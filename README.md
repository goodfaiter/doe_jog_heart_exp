# doe_jog_heart_exp
Design of Experiment Project Code for Influence of Jogging on Heart Health and Motivation

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Install uv

```bash
# On macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install the package

Clone the repository and install the package with its dependencies:

```bash
git clone https://github.com/goodfaiter/doe_jog_heart_exp.git
cd doe_jog_heart_exp

# Create a virtual environment and install all dependencies
uv sync
```

To install in an existing project as a dependency:

```bash
uv add doe_jog_heart_exp
```

### Dependencies

- [numpy](https://numpy.org/) >= 1.26.0

## Usage

```python
import doe_jog_heart_exp
import numpy as np
```
