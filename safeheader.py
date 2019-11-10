#!/usr/bin/env python
import glob
import argparse
import sys

SAFE_HEADER= b'\xDE\xAD'
def add_header(directory):
    '''
    '''
    samples = glob.glob(directory)

    for sample in samples:
        try:
            with open(sample, "rb") as fin:
                real_data = fin.read()
                new_binary = SAFE_HEADER + real_data
        except IsADirectoryError:
            print("[!] Error, specified directoy for got the '*'")
            sys.exit(1)
            with open(sample, 'wb') as fout:
                fout.write(new_binary)
        print("[+] Successfully patched %s with header" % (sample))
    return True

if __name__ == "__main__":
    print("[--<Project Safe Header>--]")
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", default="", help="Specify directory to add safety header to.",
                        required=True)
    args = parser.parse_args()

    if add_header(args.dir):
        print("[+] Successfully patched binaries with header")
