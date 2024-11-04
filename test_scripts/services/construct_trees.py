from test_scripts.services.tl_manager_adapter import *
import time
import base64

if __name__ == "__main__":
    trees = get_trees()

    for (tree_name, size) in trees.items():
        print(f'Creating {tree_name} with size {size}')
        tree = create_tree(tree_name, 2048)

        for i in range(0, size):
            data = base64.b64encode(str(i).encode())
            response = insert_leaf(tree_name, data.decode('utf-8'))
            print(f'{i} of {size}', end='\r')
        commit_tree(tree_name)
        print('')
