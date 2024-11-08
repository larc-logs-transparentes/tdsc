from tl_manager_adapter import *
import base64
import time

if __name__ == "__main__":
    trees = get_trees()

    for (tree_name, size) in trees.items():
        print(f'Creating {tree_name} with size {size}')
        tree = create_tree(tree_name, 2048)
        start = time.perf_counter()
        for i in range(0, size):
            data = base64.b64encode(str(i).encode())
            response = insert_leaf(tree_name, data.decode('utf-8'))
            print(f'{i} of {size}', end='\r')
        commit_tree(tree_name)
        end = time.perf_counter()
        print(f'Built {tree_name} with size {size} in {end - start} seconds\n')

