<<<<<<< HEAD
# Ephys-Pipeline
=======
# Extracellular Electrophysiology Analysis Pipeline

## Project purpose

This repository contains a  workflow for processing and analysing our own extracellular electrophysiology recordings. The pipeline covers data organisation, recording inspection, preprocessing, spike sorting, quality control, and reporting.

The project originated during the Neuroinformatics Unit Open Software Summer School (OSSS) extracellular electrophysiology course and builds on the concepts and examples presented in [`neuroinformatics-unit/course_ephys_osss`](https://github.com/neuroinformatics-unit/course_ephys_osss).

The main goals are to:

- organise raw and processed electrophysiology data consistently;
- create a reproducible Python environment;
- inspect and preprocess extracellular recordings;
- run and evaluate spike sorting;
- generate quality-control metrics, figures, and reports;
- identify limitations associated with different electrode and probe types.

## Acknowledgements

This project was developed from material presented during the Neuroinformatics Unit Open Software Summer School 2026. We thank the [Neuroinformatics Unit](https://neuroinformatics.dev/) instructors and contributors for developing and sharing the [extracellular electrophysiology course](https://github.com/neuroinformatics-unit/course_ephys_osss), as well as the developers of SpikeInterface and the wider open-source neuroinformatics community.

## Repository structure

```text
.
├── data/
│   ├── raw/               # Original electrophysiology recordings
│   └── processed/         # Preprocessed data and spike-sorting outputs
├── notebooks/             # Exploratory and reproducible analyses
├── reports/
│   ├── figures/           # Final figures
│   └── tables/            # Quality metrics and summary tables
├── scripts/               # Reusable command-line workflows
├── src/                   # Reusable Python functions
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```


Stable and reusable functions should be moved from the notebooks into `src/`. Larger automated workflows should be placed in `scripts/`.

## Data policy

Electrophysiology recordings and generated spike-sorting data can be very large and must not be committed to GitHub.

Store original recordings locally in:

```text
data/raw/
```

Store generated data in:

```text
data/processed/
```

Before committing, confirm that data files are ignored:

```bash
git status
git check-ignore -v data/raw/example_recording.nwb
```

Only code, notebooks, lightweight figures, summary tables, metadata, and documentation should be tracked. Each collaborator is responsible for obtaining the recordings separately and placing them in the expected local folders.

# Collaborator Setup Guide

This guide explains how to download the shared repository, create the Python environment, pull updates, and push changes to GitHub.


## 1. Clone the repository

Open a terminal and move to the directory where you want to save the project. For example:

```bash
cd ~/Desktop
```

Clone the repository:

```bash
git clone REPOSITORY-URL (SSH)
```

Enter the newly created project folder:

```bash
cd REPOSITORY-NAME
```

The `git clone` command automatically:

- creates the local project folder;
- downloads the repository files;
- connects the local repository to GitHub;
- creates the remote connection called `origin`;
- checks out the default branch, normally `main`.

Verify that the repository is correctly connected:

```bash
git remote -v
git branch
git status
```

## 2. Create the Python environment

This project uses [`uv`](https://docs.astral.sh/uv/) to manage Python and its dependencies.

Check whether `uv` is already installed:

```bash
uv --version
```

On macOS, install it with Homebrew if necessary:

```bash
brew install uv
```

From the root of the repository, create the virtual environment and install the exact dependency versions recorded in `uv.lock`:

```bash
uv sync --locked
```

This creates a local `.venv` folder. The virtual environment is local and must not be committed to GitHub.

Verify the environment:

```bash
uv run python --version
uv run python -c "import spikeinterface; print(spikeinterface.__version__)"
```

Start JupyterLab with:

```bash
uv run jupyter lab
```

In VS Code, open the entire repository folder and select the following Python interpreter or notebook kernel:

```text
.venv/bin/python
```

## 3. Pull the latest changes

Before starting any work, move to the local repository:

```bash
cd ~/Desktop/REPOSITORY-NAME
```

Make sure you are on the `main` branch:

```bash
git switch main
```

Download and integrate the latest changes from GitHub:

```bash
git pull origin main
```

If `pyproject.toml` or `uv.lock` changed, update the local environment:

```bash
uv sync --locked
```

## 4. Make changes

Edit the notebooks, scripts, source code, reports, or documentation as required.

Inspect the modified files:

```bash
git status
git diff
```

Before committing, make sure that Git is not tracking:

- raw electrophysiology data;
- `.nwb` files;
- the `.venv` environment;
- temporary files;
- spike-sorting outputs;
- large processed datasets.

## 5. Commit the changes

Add the modified files to the staging area:

```bash
git add .
```

Check exactly what will be included:

```bash
git status
```

Create a commit with a short and descriptive message:

```bash
git commit -m "Describe the changes"
```

Examples:

```bash
git commit -m "Add recording loading notebook"
git commit -m "Update preprocessing parameters"
git commit -m "Add spike-sorting quality metrics"
git commit -m "Update project documentation"
```

## 6. Push the changes

Before pushing, pull once more to check whether another collaborator has added new changes:

```bash
git pull origin main
```

If Git reports no conflicts, push the commit:

```bash
git push origin main
```

## 7. Daily workflow

The standard workflow is:

```bash
cd ~/Desktop/REPOSITORY-NAME
git switch main
git pull origin main
uv sync --locked
```

After making changes:

```bash
git status
git diff
git add .
git status
git commit -m "Describe the changes"
git pull origin main
git push origin main
```

## Important collaboration rules

1. Always run `git pull origin main` before starting.
2. Avoid editing the same notebook at the same time as another collaborator.
3. Keep commits small and use descriptive messages.
4. Check `git status` before every commit.
5. Never commit electrophysiology data or `.nwb` files.
6. Use `uv add PACKAGE_NAME` when adding a dependency instead of installing it separately with `pip`.
7. Commit both `pyproject.toml` and `uv.lock` whenever dependencies change.
8. Tell the other collaborators after pushing changes to `main`.













>>>>>>> 7d2017772d0c746ed6183de6e719a705276a0654
