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












>>>>>>> 7d2017772d0c746ed6183de6e719a705276a0654
