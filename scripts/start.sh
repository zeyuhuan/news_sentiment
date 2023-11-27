cd "$(dirname "$0")"
cd ../
.venv/bin/uvicorn main:app --reload
