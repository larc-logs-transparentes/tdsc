sudo apt install -y python3.10-venv

python3 -m venv .venv
source ./venv/bin/activate

pip install --extra-index-url https://test.pypi.org/simple/ tlverifier==0.0.28
pip install -r requirements.txt