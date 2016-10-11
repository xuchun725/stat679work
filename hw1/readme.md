# homework 1
- all commands and scripts should be run in the directory `stat679work/hw1`

## data
- copy the entire data directory (`log` and `out`) from `coursedata/hw1-snaqTimeTest` to `stat679sork/hw1` (in local repository)
```bash
cp -R ../../coursedata/hw1-snaqTimeTest/log ../../coursedata/hw1-snaqTimeTest/out .
```
![](http://p1.bqimg.com/567571/abb6c465b35f8415.png)

- untrack the data directories
```bash
touch .gitignore
echo log/* > .gitignore
echo out/* >> .gitignore
```


## scripts
### exercise 1
- `normalizeFileNames.sh`
- to change filenames in `log` and `out`, add `0` before `1-9` in filenames
- usage: `bash normalizeFileNames.sh`
- **feedback**: It's more conventional to use `timetes${x}_snaq.log` instead of `timetes"$X"_snaq.log`. About `${var}`:
  - When expending the variable in a string, `{}` can protect the variable to be expanded from characters immediately following it. e.g.,  `${x}yz`, `$xyz`
  - There is a lot that the shell can do with the notation ${x} for a variable named x. e.g., truncate the contents of a variable, make substitutions, use a default value, reference an array index, and so on.

### exercise 2
- `summarizeSNaQres.sh`
- to create a table in `csv` format to summarize the results of all these analysis in `log` and `out` (with 1 row per analysis and 3 columns)
  - `analysis`: the file name root
  - `h`: "hmax" in `*.log`
  - `CPUtime`: "Elapsed time" in `*.out`
- usage: `bash summarizeSNaQres.sh`
- result: `summary.csv`
- **feedback**:
  - In `csv` file, the comma is used to separate the columns. So there should be no extra space.
  - try to get much practice with `grep` and *extended regular expression*.
- tag [v1.2](https://github.com/xuchun725/stat679work/releases/tag/v1.2)

### exercise 3
- ex3 will overwrite `summarizeSNaQres.sh` and `summary.csv` in ex2. To go back to ex2, click tag [v1.2](https://github.com/xuchun725/stat679work/releases/tag/v1.2).
- to create a table in `csv` format to summarize the results of all these analysis in `log` and `out` with the same columns as before and additional columns for:
  - `Nruns`: number of runs
  - `Nfail`: tuning parameter, "max number of failed proposals"
  - `fabs`: tuning parameter called "ftolAbs" in the log file (tolerated difference in the absolute value of the score function, to stop the search)
  - `frel`: "ftolRel"
  - `xabs`: "xtolAbs"
  - `xrel`: "xtolRel"
  - `seed`: main seed, i.e. seed for the first runs
  - `under3460`: number of runs that returned a network with a score (-loglik value) better than (below) 3460
  - `under3450`: number of runs with a network score under 3450
  - `under3440`: number of runs with a network score under 3440
- usage: `bash summarizeSNaQres.sh`
- result: `summary.csv`  
