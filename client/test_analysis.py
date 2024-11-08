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
    download.download(samples_per_tree=args.sample_size)

    # cprint("===================== Verify tree ===================================", 'green')
    # df = local_tree_consistency.verify(samples_per_tree=args.sample_size)

    # cprint("===================== Verify build tree     =========================", 'green')
    # df = build_tree.verify(samples_per_tree=args.sample_size)
