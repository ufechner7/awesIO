# awesIO

Input/Output standard for airborne wind energy systems

awesIO reuses the windIO code with modifications.

Currently includes schemas for:
- Power curves
- Wind resource
- Airborne systems
- Ground stations
- Operational constraints
- Tether specifications


## Installation

### Install Directly from Git Repository (Recommended for Users)

Install the latest version from the main branch without cloning:

```bash
pip install git+https://github.com/awegroup/awesIO.git
```

Install from a specific branch:

```bash
pip install git+https://github.com/awegroup/awesIO.git@branch-name
```

Install from a specific commit or tag:

```bash
pip install git+https://github.com/awegroup/awesIO.git@commit-hash
pip install git+https://github.com/awegroup/awesIO.git@v0.1.0
```

**Using in a Conda environment:**

```bash
conda activate your_environment
pip install git+https://github.com/yourusername/awesIO.git
```

## Usage

After installation, you can import the package in your Python code:

```python
import awesio
from awesio.validator import validate_yaml
from awesio.yaml import load_yaml

```

## Examples

Example YAML configuration files are available in the `examples/` directory.
