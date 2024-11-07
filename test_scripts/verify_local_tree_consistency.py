from tlverifier.merkle_functions.tl_functions import verify_local_tree_history_consistency
from services.tl_manager_adapter import *
import time
import pandas as pd



GREEN = "\033[92m"
ENDC = "\033[0m"


# Measure the time to verify consistency of a local tree
if __name__ == "__main__":
    print(GREEN + "======================== Verify tree consistency  =========================" + ENDC)

    trees = get_trees()
    samples_per_tree = 1000

    df = pd.DataFrame(index=trees.values(), columns=[f'sample_{i}' for i in range(0, samples_per_tree)])

    all_leaf_global = get_all_leaf_data_global_tree()
    global_tree_root = get_trustable_global_tree_root()['value']
    for tree_name, size in trees.items():
        samples = []
        all_consistency_proof = get_all_consistency_proof(tree_name)
        for i in range(0, samples_per_tree):
            start = time.perf_counter()
            result = verify_local_tree_history_consistency(all_leaf_global, all_consistency_proof, global_tree_root, tree_name)
            end = time.perf_counter()
            interval = (end - start)*1000
            samples.append(interval)
            if not result['success']:
                print(f'Verification failed at tree {tree_name} in sample {i}')
                break
        df.loc[size] = samples
        mean = df.loc[size].mean()
        median = df.loc[size].median()
        std = df.loc[size].std()
        print(f'{tree_name}')
        print(f'mean: {mean:.3f} ms')
        print(f'std: {std:.3f} ms;  {std*100/mean:.1f} %')
        print(f'median: {median:.3f} ms')
        print('')
    df.to_csv('local_tree_consistency_verification.csv')
