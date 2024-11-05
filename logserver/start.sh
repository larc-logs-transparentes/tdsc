wget -O data/2022_round_2.zip https://github.com/larc-logs-transparentes/tdsc/releases/download/v0.0.1-dev/2022_round_2.zip data
unzip data/2022_round_2.zip 

docker compose up -d

python3 -m venv venv
source ./venv/bin/activate

pip install -r requirements.txt

python scripts/construct_trees.py
