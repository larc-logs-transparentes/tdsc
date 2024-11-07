from tlverifier.merkle_functions.tl_functions import verify_data_entry
from service.tl_manager_adapter import *
from service.utils import *
import time
import pandas as pd

def verify(samples_per_tree):
    trees = get_trees()
    df = pd.DataFrame(index=trees.values(), columns=[f'sample_{i}' for i in range(0, samples_per_tree)])
    trustable_root = get_trustable_global_tree_root()['value']
    for (tree_name, size) in trees.items():
        samples = []
        for i in range(0, samples_per_tree):
            data_proof = get_data_proof(tree_name, i)
            start = time.perf_counter()
            result = verify_data_entry(data_proof, trustable_root, str(i))
            end = time.perf_counter()
            if not result['success']:
                print(f'Verification failed at tree {tree_name} in sample {i}')
                break
            interval = (end - start) * 1000 # in miliseconds
            samples.append(interval)

        df.loc[size] = samples
        print_statistics(tree_name, df.loc[size].mean(), df.loc[size].std(), df.loc[size].median() )
    df.to_csv('data/data_entry_verification.csv')

# Measure the time to verify a data entry in a tree
if __name__ == "__main__":
    verify()
