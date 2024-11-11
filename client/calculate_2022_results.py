from analysis_scripts.tl_downloader.download_bu import download_bu
from analysis_scripts.tl_verifier.verify_tree import verify_tree
from analysis_scripts.tl_preprocessor.src.bu_preprocessor import preprocess_bus
from analysis_scripts.tl_sum.src.bu_functions import soma_votos
from analysis_scripts.tl_sum.src.service.json_utils import get_json_data_from_dir, print_dict
from termcolor import cprint
import os
import shutil
from pathlib import Path



if __name__ == "__main__":
    cprint('###########################################################################', 'green')
    cprint('#                                                                         #', 'green')
    cprint('#                           Calculate Results                             #', 'green')
    cprint('#                                                                         #', 'green')
    cprint('###########################################################################', 'green')
    print('Test the results of 2022 Brazilian Elections\n\n')



    cprint("================ Download ===========================================", 'green')
    if os.path.exists("./data/trees/eleicao_545"):
        shutil.rmtree("./data/trees/eleicao_545")
    download_bu("eleicao_545")

    cprint("===================== Verify tree    ==================================", 'green')
    result = verify_tree("eleicao_545")
    print(result)

    cprint("================ Preprocess ===========================================", 'green')
    preprocess_bus('./data/trees/eleicao_545', './data/preprocessed_bu_jsons/eleicao_545')

    cprint("================    Tally     ===========================================", 'green')
    files, bus_json = get_json_data_from_dir(Path('./data/preprocessed_bu_jsons/eleicao_545'))
    result = soma_votos(bus_json, 'presidente')
    print_dict(result)

