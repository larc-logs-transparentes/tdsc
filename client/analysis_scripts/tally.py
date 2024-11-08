# from tl_downloader.src.download_bu import download_bu, ask_user_which_election
from tl_verifier.verify_tree import verify_tree
import time
import pandas as pd
from service.utils import *
import shutil
from tl_sum.src.service.json_utils import get_json_data_from_file, get_json_data_from_dir, print_dict
from pathlib import Path
from tl_sum.src.bu_functions import soma_votos




def verify(samples_number):
    df = pd.DataFrame(index=[0], columns=[f'sample_{i}' for i in range(0, samples_number)])
    samples = []
    for i in range(0, samples_number):
        print(f'\nTesting sample: {i}')
        files, bus_json = get_json_data_from_dir(Path('./data/preprocessed_bu_jsons/eleicao_545'))
        start = time.perf_counter()
        resultado = soma_votos(bus_json, 'presidente')
        end = time.perf_counter()
        interval = (end - start) * 1000 # in miliseconds
        samples.append(interval)

    df.loc[0] = samples
    print_statistics("\nTest tally", df.loc[0].mean(), df.loc[0].std(), df.loc[0].median() )
    df.to_csv('data/tally.csv')


if __name__ == "__main__":
    verify(50)
    
