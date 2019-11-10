#!/usr/bin/python3
import glob
import argparse
import sys

SAFE_HEADER = b'\xDE\xAD\xCA\xFE'
def header_manipulation(directory, patch=None, remove=None):
    '''
    Name: header_manipulation
    Purpose: Add a fake header to a binary to prevent accidental execution in
             the moving of binaries.
    Return: Boolean value.
    '''
    samples = glob.glob(directory)
    if patch is not None and remove is not None:
        print("[!] Error, you cannot remove and patch the magicheader!")
        return False

    for sample in samples:
        try:
            with open(sample, "rb") as fin:
                real_data = fin.read()
                if real_data[0:4] == b'\xde\xad\xca\xfe' and remove is None:
                    print("[!] Safe header already exists within %s." % sample)

                if real_data[0:4] == b'\xde\xad\xca\xfe' and remove is not None:
                    print("[*] Safe header identified in %s! Removing safe header!" % sample)
                    real_data = real_data[4:] # Remove four bytes
                    try:
                        with open(sample, 'wb') as fout:
                            fout.write(real_data)
                    except IOError as err:
                        print("[!] Error: %s" % (err))
                        return False
                    print("[+] Successfully restored %s." % (sample))

                if real_data[0:4] != b'\xde\xad\xca\xfe' and remove is not None:
                    print("[!] Magic header has already been removed")

                if real_data[0:4] != b'\xde\xad\xca\xfe' and patch is not None:
                    new_binary = SAFE_HEADER + real_data
                    try:
                        with open(sample, 'wb') as fout:
                            fout.write(new_binary)
                    except IOError as err:
                        print("[!] Error: %s" % (err))
                        return False
                    print("[+] Successfully patched %s with header %s" % (sample, SAFE_HEADER))
        except IsADirectoryError:
            print("[!] Error, specified directory for got the '*'")
            return False

    return True

if __name__ == "__main__":
    print("[--<Project Safe Header>--]")
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", default="",
                        help="Specify directory to add safety header to.", required=True)

    parser.add_argument("-r", "--remove", default=None, action="store_true",
                        help="Specify directory to remove safety header to.", required=False)

    parser.add_argument("-p", "--patch", default=None, action="store_true",
                        help="Specify to patch binary or not.", required=False)
    args = parser.parse_args()

    if args.patch is not None and args.remove is not None:
        print("[!!!] You cannot patch some binaries and remove the patch at the same time! [!!!]")
        sys.exit(1)

    if header_manipulation(args.dir, args.patch, args.remove):
        print("[+] Successfully completed manipulation")
    else:
        print("[!] Something has gone horribly wrong with safeheader.")
