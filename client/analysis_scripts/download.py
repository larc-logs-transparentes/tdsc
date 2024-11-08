# from tl_downloader.src.download_bu import download_bu, ask_user_which_election
from analysis_scripts.tl_downloader.download_bu import download_bu
import time
import pandas as pd
from service.utils import *
import shutil
import os



def download(samples_number):
    df = pd.DataFrame(index=[0], columns=[f'sample_{i}' for i in range(0, samples_number)])
    samples = []
    for i in range(0, samples_number):
        if os.path.exists("./data/trees/eleicao_545"):
            shutil.rmtree("./data/trees/eleicao_545")
        print(f'Testing sample: {i}')
        start = time.perf_counter()
        download_bu("eleicao_545")
        end = time.perf_counter()
        interval = (end - start) * 1000 # in miliseconds
        samples.append(interval)

    df.loc[0] = samples
    print_statistics("Test Download", df.loc[0].mean(), df.loc[0].std(), df.loc[0].median() )
    df.to_csv('data/download.csv')


if __name__ == "__main__":
    download(1)
    
