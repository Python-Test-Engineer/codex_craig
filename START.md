# Start commands

## CSV Analyser Manual Run

1. Open a terminal in this folder.
2. Install dependencies:
   `uv sync`
3. Start the app:
   `uv run uvicorn csv_analyser.main:app --app-dir src --reload --port 8001`
4. Open your browser:
   - App: http://127.0.0.1:8001/
   - API docs: http://127.0.0.1:8001/docs
