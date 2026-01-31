# Workout Tracking Using Google Sheets

Short description
-----------------

Logs your natural-language exercise input to a Google Sheet using the 100DaysOfPython nutrition API and a Sheety endpoint.

Getting started
---------------

Prerequisites:
- Python 3.8+
- An account / credentials for the nutrition API (APP_ID and API_KEY)
- A Sheety endpoint connected to the Google Sheet (SHEET_ENDPOINT) and an API token (BEARER)

Install dependencies:

```bash
pip install -r requirements.txt
```

Environment variables
---------------------

Set these environment variables before running the script:

- `APP_ID` — nutrition API app id
- `API_KEY` — nutrition API key
- `SHEET_ENDPOINT` — your Sheety POST endpoint URL
- `BEARER` — token used by Sheety (the script sends it in a `Bearer` header)

Usage
-----

Run the script and enter exercises when prompted. Separate multiple exercises with " and ".

```bash
python main.py
# Example input when prompted:
"ran 3 miles and cycled 20 minutes"
```

What happens
------------

1. The script sends each exercise phrase to the nutrition API to parse name, duration and calories.
2. It posts a row per exercise to the configured Sheety endpoint with `date`, `time`, `exercise`, `duration`, and `calories`.

Notes & troubleshooting
-----------------------

- If you get HTTP 401/403, verify `APP_ID`, `API_KEY`, and `BEARER` values.
- The script splits input on the literal string " and ". Use that to separate multiple exercises.
- The script expects the Sheety endpoint to accept JSON in the format used in `main.py`.

Want changes?
-------------

If you want I can:
- add better header formatting for Sheety (e.g., `Authorization: Bearer <token>`),
- add an example `.env` file and a small helper to load it,
- or add input validation and retries.
