import requests

TL_MANAGER_URL = 'http://127.0.0.1:8000'


def get_trees():
    tree__leaves = [1000, 10000, 100000, 500000, 1000000]
    trees = {}
    for size in tree__leaves:
        tree_name = f'tree_{size}'
        trees[tree_name] = size
    return trees


def create_tree(tree_name, commitment_size):
    requests.post(f'{TL_MANAGER_URL}/tree-create', json={"tree_name": tree_name, "commitment_size": commitment_size})


def commit_tree(tree_name):
    requests.post(f'{TL_MANAGER_URL}/tree/commit', json={"tree_name": tree_name})


def insert_leaf(tree_name, data):
    return requests.post(f'{TL_MANAGER_URL}/insert-leaf', json={"tree_name": tree_name, "data": data})