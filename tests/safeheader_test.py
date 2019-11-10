"""
Tests for safeheader
"""
import json
import os
import sys
import unittest
sys.path.append("../")

from safeheader import header_manipulation

class TestSafeHeader(unittest.TestCase):

    def setUp(self):
        self.binary = b'\x90\x90\x90\x90'
        try:
            os.mkdir("./test_bins/")
        except:
            pass
        with open("./test_bins/test.bin", "wb+") as fout:
            try:
                fout.write(self.binary)
            except IOError:
                print("[!] Error, could not write test.bin file for unit test")
                sys.exit(1)

    def tearDown(self):
        try:
            os.remove("./test_bins/test.bin")
            pass
        except IOError:
            print("[!] Error, could not remove test.bin file for unit test")
            sys.exit(1)

        os.rmdir("./test_bins/")


    def test_header_manipulation_add_header(self, directory="./test_bins/*", patch=True, remove=None):
        '''
        Name: test_header_manipulation_add_header
        Purpose: Test adding header
        '''
        assert(header_manipulation(directory, patch, remove) == True)


    def test_header_manipulation_remove_header(self, directory="./test_bins/*", patch=None, remove=True):
        '''
        Name: test_header_manipulation_remove_header
        Purpose: Test removing header.
        '''
        assert(header_manipulation(directory, patch, remove) == True)

    def test_header_manipulation_conflict_header(self, directory="./test_bins/*", patch=True, remove=True):
        '''
        Name: test_header_manipulation_conflict_header
        Purpose: Test conflicting user arguments 
        '''
        assert(header_manipulation(directory, patch, remove) == False)

if __name__ == "__main__":
    unittest.main()
