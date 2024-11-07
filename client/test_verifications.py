from verification_scripts import *
from service.args_parser import parser
from termcolor import cprint
import os

if __name__ == "__main__":
    args = parser.parse_args()
    cprint('###########################################################################', 'green')
    cprint('#                                                                         #', 'green')
    cprint('#                           Test Verifications                            #', 'green')
    cprint('#                                                                         #', 'green')
    cprint('###########################################################################', 'green')
    print('Test the performance of main verifications in Election Transparency')
    print(f"sample_size={args.sample_size}\n\n")


    cprint("================ Verify data entry (inclusion proof) ================", 'green')
    data_entry.verify(samples_per_tree=args.sample_size)

    cprint("===================== Verify tree consistency  ======================", 'green')
    df = local_tree_consistency.verify(samples_per_tree=args.sample_size)

    cprint("===================== Verify build tree     =========================", 'green')
    df = build_tree.verify(samples_per_tree=args.sample_size)
