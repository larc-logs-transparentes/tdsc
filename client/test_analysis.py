from analysis_scripts import *
from service.args_parser import parser
from termcolor import cprint
import os

if __name__ == "__main__":
    args = parser.parse_args()
    cprint('###########################################################################', 'green')
    cprint('#                                                                         #', 'green')
    cprint('#                           Test Analysis                                #', 'green')
    cprint('#                                                                         #', 'green')
    cprint('###########################################################################', 'green')
    print('Test the performance of main analysis in Election Transparency')
    print(f"sample_size={args.sample_size}\n\n")


    cprint("================ Download ===========================================", 'green')
    download.download(sample_size=args.sample_size)

    cprint("===================== Verify tree    ==================================", 'green')
    verify_tree.verify(sample_size=args.sample_size)

    cprint("================ Preprocess ===========================================", 'green')
    preprocess.preprocess(sample_size=args.sample_size)

    cprint("================    Tally     ===========================================", 'green')
    tally.tally(sample_size=args.sample_size)

