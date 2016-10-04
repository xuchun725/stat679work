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

### exercise 2
- `summarizeSNaQres.sh`
- to create a table in `csv` format to summarize the results of all these analysis in `log` and `out` (with 1 row per analysis and 3 columns)
  - `analysis`: the file name root
  - `h`: "hmax" in `*.log`
  - `CPUtime`: "Elapsed time" in `*.out`
- usage: `bash summarizeSNaQres.sh`
- result: `summary.csv`


analysis | h | CPUtime |   
---------| --| --------
bT1      | 0 | 103354.760381735  
net1_snaq | 1 | 11648.984309726    
...      | ...| ...
