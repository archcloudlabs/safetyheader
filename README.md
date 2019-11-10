### SafeHeader
#### Purpose
Prevent accidental execution of malware by prepending a "unique header" to the
binary.

#### Example Usage
* Prepend "deadcafe" to binaries in a specific directory.
 ```bash 
./safeheader.py -d test_bins/\*
```
* Remove deadcafe from binaries in a specific directory.

```
./safeheader.py --rm --dir test_bins/\*
```
