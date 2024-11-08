docker compose up -d

cd ../..
source .venv/bin/activate

cd -

python construct_trees.py
