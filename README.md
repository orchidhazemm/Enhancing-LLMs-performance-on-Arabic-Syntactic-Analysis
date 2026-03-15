# Enhancing LLMs Performance on Arabic Syntactic Analysis

**Making large language models better at understanding and generating Arabic.**

A graduation project that improves Arabic NLP by training custom tokenizers, fine-tuning with LoRA, and building an end-to-end pipeline from data to a live inference API.

## Demo

**[Watch the demo video](https://drive.google.com/file/d/1F9lIXivl3uhYdingkMCE_aZ5-VnAAx--/view?usp=share_link)** *(Google Drive)*

---

## What This Project Does

- **Custom Arabic tokenizers** — Train and merge tokenizers tailored to Arabic script and morphology for more efficient and accurate tokenization.
- **Fine-tuning & evaluation** — Fine-tune base LLMs on Arabic instruction data and evaluate syntactic and generative quality.
- **Adaptive LoRA training** — Use parameter-efficient LoRA (and variants) to adapt models to Arabic without full fine-tuning.
- **Live inference API** — Serve the fine-tuned model via FastAPI (e.g. from notebooks) with a simple `/generate` endpoint for demos and the UI.

---

## Project Structure

| Folder | What's inside |
|--------|----------------|
| **[data/](data/)** | Dataset descriptions and **download links** (files are on Google Drive). |
| **[notebooks/](notebooks/)** | Jupyter notebooks: custom tokenizer training, merging, fine-tuning, evaluation, and the FastAPI app. |
| **[src/](src/)** | Reusable source code (preprocessing, evaluation, utilities). |
| **[experiments/](experiments/)** | Configs and notes for reproducible runs. |
| **[results/](results/)** | Metrics, tables, and figures. |
| **[scripts/](scripts/)** | Download and run scripts. |
| **[ui/](ui/)** | Web UI and assets for the demo. |

---

## Datasets

We use Arabic instruction and text corpora hosted on Google Drive (not in the repo due to size). **Download them from the links in [data/README.md](data/README.md)** and place the files in the `data/` folder.

| Dataset | Use |
|--------|-----|
| **Alpaca Arabic (cleaned)** | Instruction tuning |
| **Beetlware** | Arabic text corpus |
| **Gemma2 Arabic instruct (cleaned)** | Instruction data for Gemma2-style models |
| **ShareGPT Arabic instruction** | Instruction / conversation data |

All links and filenames are listed in [data/README.md](data/README.md).

---

## Setup

```bash
git clone https://github.com/orchidhazemm/Enhancing-LLMs-performance-on-Arabic-Syntactic-Analysis.git
cd Enhancing-LLMs-performance-on-Arabic-Syntactic-Analysis
pip install -r requirements.txt   # if present; otherwise install deps from notebooks
```

1. Download the datasets from [data/README.md](data/README.md) into `data/`.
2. Run the notebooks in order (tokenizer training → merging → fine-tuning & evaluation → API app as needed).

---

## Usage

- **Notebooks:** Open `notebooks/` in Jupyter (or Colab). Start with tokenizer training, then fine-tuning & evaluation, then the app notebook for the API.
- **API:** The notebook runs a FastAPI server and (optionally) exposes it via ngrok for a public `/generate` endpoint.
- **UI:** Use the [ui/](ui/) folder for the web interface that talks to the API.

---

## Tech Stack

- **Models & training:** Transformers, PEFT (LoRA), Accelerate  
- **Serving:** FastAPI, Uvicorn  
- **Notebooks:** Jupyter (Colab-friendly)  
- **Data:** Arabic instruction datasets (Alpaca, ShareGPT, Gemma2-style, Beetlware)

---

## License

See [LICENSE](LICENSE) if present.
