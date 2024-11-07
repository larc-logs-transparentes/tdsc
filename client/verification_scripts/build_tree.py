from service.tl_manager_adapter import *
from service.utils import *
from pymerkle_logsTransparentes import MerkleTree
import time
import pandas as pd


def get_global_tree_leaves_with_tree_name(global_tree_leaves, tree_name):
    leaves_with_tree_name = []
    for leave in global_tree_leaves:
        if leave.get('value').get('tree_name') == tree_name:
            leaves_with_tree_name.append(leave)
    return leaves_with_tree_name

def _build_tree_continuously(list_of_data, m_tree=None):
    if m_tree is None:
        m_tree = MerkleTree()

    for data in list_of_data:
        m_tree.append_entry(data)
    return m_tree


def verify(samples_per_tree):
    trees = get_trees()
    df = pd.DataFrame(index=trees.values(), columns=[f'sample_{i}' for i in range(0, samples_per_tree)])
    global_tree_leaves = get_all_leaf_data_global_tree()['leaves']
    for tree_name, size in trees.items():
        leaves_in_global_tree = get_global_tree_leaves_with_tree_name(global_tree_leaves, tree_name)
        list_of_data = [str(i) for i in range(0, size)]

        samples = []
        for i in range(0, samples_per_tree):
            start = time.perf_counter()
            local_tree = None
            start_index = 0
            for global_tree_leaf in leaves_in_global_tree:
                tree_size = global_tree_leaf['value']['tree_size']
                end_index = tree_size
                data = list_of_data[start_index:end_index]

                local_tree = _build_tree_continuously(data, local_tree)
                local_tree_root = local_tree.root.decode('utf-8')

                if local_tree_root != global_tree_leaf['value']['value']:
                    print(f'Verification failed at tree {tree_name} in sample {i}')
                    break

                start_index = end_index
            end = time.perf_counter()
            interval = (end - start) * 1000 # in miliseconds
            samples.append(interval)
        df.loc[size] = samples
        print_statistics(tree_name, df.loc[size].mean(), df.loc[size].std(), df.loc[size].median() )
    df.to_csv('data/rebuild_tree.csv')


if __name__ == "__main__":
    verify()