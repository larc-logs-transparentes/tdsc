from tlverifier.merkle_functions.tl_functions import verify_data_entry
from services.tl_manager_adapter import *
import time
import pandas as pd

GREEN = "\033[92m"
ENDC = "\033[0m"

# Measure the time to verify a data entry in a tree
if __name__ == "__main__":
    print(GREEN + "======================== Verify data entry (inclusion proof) =========================" + ENDC)

    trees = get_trees()
    samples_per_tree = 1000

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
            interval = (end - start)*1000
            samples.append(interval)
        df.loc[size] = samples
        mean = df.loc[size].mean()
        median = df.loc[size].median()
        std = df.loc[size].std()
        print(f'{tree_name}')
        print(f'mean: {mean:.3f} ms')
        print(f'std: {std:.3f} ms;  {std*100/mean:.1f} %')
        print(f'median: {median:.3f} ms')
        print('')


    df.to_csv('data_entry_verification.csv')
