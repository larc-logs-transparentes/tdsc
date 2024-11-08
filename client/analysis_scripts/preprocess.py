# from tl_downloader.src.download_bu import download_bu, ask_user_which_election
import time
import pandas as pd
from service.utils import *
import shutil
from analysis_scripts.tl_preprocessor.src.bu_preprocessor import preprocess_bus



def preprocess(sample_size):
    df = pd.DataFrame(index=[0], columns=[f'sample_{i}' for i in range(0, sample_size)])
    samples = []
    for i in range(0, sample_size):
        print(f'\nTesting sample: {i}')
        start = time.perf_counter()
        preprocess_bus('./data/trees/eleicao_545', './data/preprocessed_bu_jsons/eleicao_545')
        end = time.perf_counter()
        interval = (end - start) * 1000 # in miliseconds
        samples.append(interval)

    df.loc[0] = samples
    print_statistics("\nTest preprocess", df.loc[0].mean(), df.loc[0].std(), df.loc[0].median() )
    df.to_csv('data/preprocess.csv')


if __name__ == "__main__":
    preprocess(50)
    
