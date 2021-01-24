#!/usr/bin/python3
"""
Add "safe header" to prevent accidental patching.
"""
import glob
import argparse
import sys

SAFE_HEADER = b'\xDE\xAD\xCA\xFE'

def write(fname, data):
    '''
    Purpose: write binary data to disk
    Return: Boolean value indiciating success or false on IO failure
    '''
    try:
        with open(fname, 'wb') as fout:
            fout.write(data)
        return True
    except IOError as err:
        print("[!] Error: %s" % (err))
    return False


def recursive_check():
    '''
    perform recursive check for enduser input.
    Return: Boolean for whether or not the user should continue..
    '''
    choice = input("Do you want to proceed? [Y/N]> ")
    if choice.lower() not in ["y","n"]:
        recursive_check()
    elif choice.lower() == "y":
        return True
    else:
        return False

def user_chk(samples):
    '''
    Check for user input prior to performing header patch.
    Return: None
    '''
    print("safetyheader is about to be applied to the following files: ")
    [print("\t" + x) for x in samples]
    status = recursive_check()
    if status is False:
        print("[*] Quitting!")
        sys.exit(0)


def header_manipulation(directory, patch=None, remove=None):
    '''
    Purpose: Add a fake header to a binary to prevent accidental execution in
             the moving of malicious binaries.
    Return: Boolean value.
    '''
    samples = glob.glob(directory)
    user_chk(samples)

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
                    real_data = real_data[4:] # Remove safeheader

                    if write(sample, real_data):
                        print("[+] Successfully restored %s." % (sample))
                    else:
                        print("[!] Something went wrong restoring %s." % (sample))

                if real_data[0:4] != b'\xde\xad\xca\xfe' and remove is not None:
                    print("[!] Magic header has already been removed")

                if real_data[0:4] != b'\xde\xad\xca\xfe' and patch is not None:
                    new_binary = SAFE_HEADER + real_data
                    if write(sample, new_binary):
                        print("[+] Successfully patched %s with header %s" % (sample, SAFE_HEADER))
        except IsADirectoryError:
            print("[!] Error, specified directory forgot the '*'")
            return False

    return True

if __name__ == "__main__":
    print("[--<Project Safe Header>--]")
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", default="",
                        help="Specify directory to add safety header to.", required=True)

    parser.add_argument("-r", "--remove", default=None, action="store_true",
                        help="Specify directory to remove safety header to.", required=False)

    parser.add_argument("-p", "--patch", default=True, action="store_true",
                        help="Specify to patch binary or not.", required=False)
    args = parser.parse_args()

    if args.patch is not None and args.remove is not None:
        print("[!!!] You cannot patch some binaries and remove the patch at the same time! [!!!]")
        sys.exit(1)

    if header_manipulation(args.dir, args.patch, args.remove):
        print("[+] Successfully completed manipulation")
    else:
        print("[!] Something has gone horribly wrong with safeheader.")
