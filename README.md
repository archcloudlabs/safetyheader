<p align="center">
<img width="264" height="264" src="https://i.imgur.com/ZwU41LG.png">
<br />
</p>

#### About The Project 

Prevent accidental execution of binaries by prepending a "unique header" to the
binary.

#### Requirements
* Python3

#### Example CLI Usage

* Prepend "deadcafe" to binaries in a specific directory.
 ```bash 
 ./safeheader.py --patch --dir ./test_bins/\*
```

* Remove deadcafe from binaries in a specific directory.

```
./safeheader.py --rm --dir test_bins/\*
```

#### Unit Tests
```
 python -m unittest
```
