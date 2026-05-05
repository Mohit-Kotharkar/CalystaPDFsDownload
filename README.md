# EMR Document Downloader

Automates downloading of Consent, Encounter, and Invoice PDFs for patients from Calysta EMR, with checkpointing, validation, and audit reporting.

## Features
- Parallel download of three document types
- Checkpoint and resume
- PDF validation and duplicate handling
- Per-patient audit report
- Configurable via YAML

## Usage
1. Configure credentials and settings in `config/`
2. Run `python src/main.py`

See requirements.txt for dependencies.
