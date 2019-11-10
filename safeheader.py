#!/usr/bin/python3
import glob
import argparse
import sys

SAFE_HEADER= b'\xDE\xAD\xCA\xFE'
def add_header(directory):
    '''
    '''
    samples = glob.glob(directory)

    for sample in samples:
        try:
            with open(sample, "rb") as fin:
                real_data = fin.read()
                if real_data[0:4] == b'\xde\xad\xca\xfe':
                    print("[*] Safe header has already been appended. Exiting!")
                    sys.exit(1)
                new_binary = SAFE_HEADER + real_data
                with open(sample, 'wb') as fout:
                    fout.write(new_binary)
                print("[+] Successfully patched %s with header" % (sample))
        except IsADirectoryError:
            print("[!] Error, specified directoy for got the '*'")
            sys.exit(1)
    return True


def remove_header(directory):
    '''
    '''
    samples = glob.glob(directory)

    for sample in samples:
        try:
            with open(sample, "rb") as fin:
                real_data = fin.read()
                if real_data[0:4] == b'\xde\xad\xca\xfe':
                    print("[+] Safe header identified. Removing.")
                    real_data = real_data[4:]
                    with open(sample, 'wb') as fout:
                        fout.write(real_data)
                    print("[+] Successfully restored %s." % (sample))
                else:
                    print("[+] ELF header already exists %s." % (sample))

        except IsADirectoryError:
            print("[!] Error, specified directoy for got the '*'")
            sys.exit(1)
    return True


if __name__ == "__main__":
    print("[--<Project Safe Header>--]")
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", default="", help="Specify directory to add safety header to.",
                        required=True)
    parser.add_argument("-r", "--rm", default="", action="store_true", help="Specify directory to rmeove safety header to.",
                        required=False)
    args = parser.parse_args()

    if args.rm:
        remove_header(args.dir)

    elif add_header(args.dir):
        print("[+] Successfully patched binaries with header")
