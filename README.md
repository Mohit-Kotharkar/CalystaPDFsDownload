# EMR Document Downloader

Automates downloading of Consent, Encounter, and Invoice PDFs for patients from EMR, with checkpointing, validation, and audit reporting.

## Features
- Parallel download of three document types
- Checkpoint and resume
- PDF validation and duplicate handling
- Per-patient audit report
- Configurable via YAML
- A csv file can be directly uploaded with patient list
- Make sure the title of the csv file is "Facility QA Patients.csv"
## Usage
1. Configure credentials and settings in `config/`
2. Run `python src/main.py`

See requirements.txt for dependencies.
