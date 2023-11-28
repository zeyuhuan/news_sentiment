cd "$(dirname "$0")"
cd ../
source .env
.venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --reload
