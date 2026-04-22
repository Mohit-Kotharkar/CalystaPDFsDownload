import asyncio
import os
import yaml
from auth import authenticate_and_select_facility
from encounter_downloader import download_encounter_documents

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config')
DOWNLOADS_PATH = os.path.join(os.path.dirname(__file__), '..', 'downloads', 'TestFacility', '233957', 'Encounter_History')
os.makedirs(DOWNLOADS_PATH, exist_ok=True)

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

async def main():
    # Load credentials and settings
    credentials = load_yaml(os.path.join(CONFIG_PATH, 'credentials.yaml'))
    settings = load_yaml(os.path.join(CONFIG_PATH, 'settings.yaml'))

    # Authenticate and select facility
    playwright, browser, context, page = await authenticate_and_select_facility(credentials, settings)

    # Download encounter documents for hardcoded patient
    await download_encounter_documents(page, DOWNLOADS_PATH, patient_id="233957", per_page=10)

    await browser.close()
    await playwright.stop()
    print(f"Download complete. Files saved to {DOWNLOADS_PATH}")

if __name__ == "__main__":
    asyncio.run(main())
