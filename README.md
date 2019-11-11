<p align="center">
<img width="264" height="264" src="https://i.imgur.com/ZwU41LG.png">
<br />
</p>

### About The Project 

Prevent accidental execution of binaries by prepending a "unique header" to the
binary.

### Requirements
* Python3

### Example CLI Usage

* Prepend "deadcafe" to binaries in a specific directory.
 ```bash 
 ./safeheader.py --patch --dir ./test_bins/\*
```

* Remove "deadcafe" from binaries in a specific directory.

```
./safeheader.py --rm --dir test_bins/\*
```

### Unit Tests
Executing  ``` python -m unittest``` should result in
```
.[+] Successfully patched ./test_bins/test.bin with header b'\xde\xad\xca\xfe'
.[!] Error, you cannot remove and patch the magicheader!
.[!] Error, you cannot remove and patch the magicheader!
.[!] Magic header has already been removed
.
----------------------------------------------------------------------
Ran 4 tests in 0.004s

OK
```
If anything else is produced, please create an issue.
