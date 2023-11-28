cd "$(dirname "$0")"
cd ../
source .env
.venv/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
