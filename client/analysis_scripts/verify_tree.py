# from tl_downloader.src.download_bu import download_bu, ask_user_which_election
from tl_verifier.verify_tree import verify_tree
import time
import pandas as pd
from service.utils import *
import shutil



def verify(samples_number):
    df = pd.DataFrame(index=[0], columns=[f'sample_{i}' for i in range(0, samples_number)])
    samples = []
    for i in range(0, samples_number):
        print(f'Testing sample: {i}')
        start = time.perf_counter()
        verify_tree("eleicao_545")
        end = time.perf_counter()
        interval = (end - start) * 1000 # in miliseconds
        samples.append(interval)

    df.loc[0] = samples
    print_statistics("Test verify tree", df.loc[0].mean(), df.loc[0].std(), df.loc[0].median() )
    df.to_csv('data/verify_tree.csv')


if __name__ == "__main__":
    verify(50)
    
