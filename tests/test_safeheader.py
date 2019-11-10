"""
Tests for safeheader
"""
try:
    from safeheader import header_manipulation
    import os
    import sys
    import unittest
except ImportError as err:
    print("[!] Error could not import %s" % (err))



class TestSafeHeader(unittest.TestCase):
    '''
    Tests for safeheader functions
    '''

    def setUp(self):
        self.binary = b'\x90\x90\x90\x90'
        try:
            os.mkdir("./test_bins/")
        except IOError as io_err:
            print("[IOError] %s" % io_err)
            sys.exit(1)
        with open("./test_bins/test.bin", "wb+") as fout:
            try:
                fout.write(self.binary)
            except IOError:
                print("[!] Error, could not write test.bin file for unit test")
                sys.exit(1)

    def tearDown(self):
        try:
            os.remove("./test_bins/test.bin")
        except IOError:
            print("[!] Error, could not remove test.bin file for unit test")
            sys.exit(1)

        os.rmdir("./test_bins/")


    @classmethod
    def test_header_manipulation_add_header(cls, directory="./test_bins/*",
                                            patch=True, remove=None):
        '''
        Name: test_header_manipulation_add_header
        Purpose: Test adding header
        '''
        assert header_manipulation(directory, patch, remove) is True


    @classmethod
    def test_header_manipulation_remove_header(cls, directory="./test_bins/*",
                                               patch=None, remove=True):
        '''
        Name: test_header_manipulation_remove_header
        Purpose: Test removing header.
        '''
        assert header_manipulation(directory, patch, remove) is True

    @classmethod
    def test_header_manipulation_conflict_header(cls, directory="./test_bins/*",
                                                 patch=True, remove=True):
        '''
        Name: test_header_manipulation_conflict_header
        Purpose: Test conflicting user arguments
        '''
        assert header_manipulation(directory, patch, remove) is False

if __name__ == "__main__":
    unittest.main()
