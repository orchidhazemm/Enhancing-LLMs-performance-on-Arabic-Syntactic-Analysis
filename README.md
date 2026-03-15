# Enhancing LLMs Performance on Arabic Syntactic Analysis

Graduation project on improving Large Language Model performance for Arabic syntactic analysis (parsing, dependency parsing, POS tagging, etc.).

## Project structure

| Folder | Description |
|--------|-------------|
| **[data/](data/)** | Datasets for Arabic syntactic analysis (raw and preprocessed). |
| **[notebooks/](notebooks/)** | Jupyter notebooks for experiments, analysis, and visualizations. |
| **[src/](src/)** | Source code: preprocessing, model interfaces, evaluation pipelines. |
| **[experiments/](experiments/)** | Experiment configs, run logs, and reproducibility notes. |
| **[results/](results/)** | Outputs, metrics, tables, and figures. |
| **[scripts/](scripts/)** | Utility scripts (download data, preprocess, run evaluation). |
| **[ui/](ui/)** | Web or desktop UI for running and visualizing the analysis. |

## Large files

Datasets and model weights are not stored in this repo (GitHub’s 100 MB file limit). Use [data/README.md](data/README.md) for options: external hosting + download script, **Git LFS**, or **DVC**.

## Setup

Install dependencies (adjust to your environment):

```bash
pip install -r requirements.txt
```

## Usage

See `notebooks/` for step-by-step experiments and `scripts/` for batch runs.

## License

See [LICENSE](LICENSE) if present.
