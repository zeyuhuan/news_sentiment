cd "$(dirname "$0")"
cd ../
rm -rf .venv
conda env create -f environment.yml -p .venv