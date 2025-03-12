# CDSMatch

## Overview

**CDSMatch** is a Python package and command-line tool designed for matching IDs from two different genome annotation sources based on sequence similarity. It is particularly useful for tasks such as:

- Data reconciliation
- Entity resolution
- Fuzzy matching of genomic annotations

By leveraging sequence similarity, this tool enables researchers and bioinformaticians to map genome annotation identifiers across different datasets with high accuracy.

## Features

- **Sequence-based ID matching**: Uses sequence similarity to align genome annotation IDs.
- **Command-line utility**: Easily executable from the terminal for automated workflows.
- **Python API**: Can be integrated into custom scripts and pipelines.
- **Efficient processing**: Optimized for handling large-scale genomic datasets.

## Installation

```sh
git clone https://github.com/zitunstu24/CDSMatch.git
cd CDSMatch
pip install .
```

## Usage

### Command-Line Interface (CLI)

```sh
CDSMatch --config config.yml
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `--config` | Path to the config file (yml format) |

## Configuration
This tool uses a YAML file for configuration. You can customize various aspects, such as directories for genomes, output locations, and STAR parameters.

An example configuration file can be found at `config/config.yml`. Here's a typical structure:


```yml

cds_file_X: "data/input/NCBI_lotus_cds.fa"
cds_file_Y: "data/input/lotus_cds.fa"
blast_db: "data/output/ncbi_cds_db"
XML_output: "data/output/results.xml"
output_dir: "data/output"
output_csv: "CDSMatch_results.csv"
evalue: 0.001

```

## Dependencies

- Python 3.7+
- Biopython
- Pandas
- NumPy
- ace_tools_open

## Contributing

We welcome contributions! Feel free to submit issues, feature requests, or pull requests on our [GitHub repository](https://github.com/zitunstu24/CDSMatch).


## Contact

For questions or support, please reach out via the [GitHub issues](https://github.com/zitunstu24/CDSMatch/issues) or email me at abul.khayer@mpimp-golm.mpg.de or zitunstu24@gmail.com.

