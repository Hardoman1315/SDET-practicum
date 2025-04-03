cd ../..
python3 -m venv .venv
source .venv/bin/activate
cd "CLI scripts" || exit 1
pip install -r requirements.txt
