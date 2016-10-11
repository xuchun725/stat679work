# Create a table in csv format to summarize the the results of all these analysis in log/ and out/.
# 1 row per analysis and 13 columns
# Usage: in `stat679work/hw1`, run `bash summarizeSNaQres.sh`

echo "analysis,h,CPUtime,Nruns,Nfail,fabs,frel,xabs,xrel,seed,under3460,under3450,under3440" > summary.csv
for file in log/*.log
do
  filename=$(basename -s ".log" $file)  # get file name root
  h=$(grep -oE "hmax = [0-9]+" log/"${filename}".log | sed -E 's/.*([0-9]+)/\1/g')  # the maximum number of hybridizations allowed during the analysis
  CPUtime=$(grep "Elapsed time" out/"${filename}".out | sed -E 's/[^0-9]*([0-9]+\.[0-9]+).*/\1/g')  # total CPU time
  Nruns=$(grep "runs" log/net1_snaq.log | sed -E 's/BEGIN: ([0-9]+) runs.*/\1/g')  # number of runs
  Nfail=$(grep "failed" log/"${filename}".log | sed -E 's/.*proposals = ([0-9]+),.*/\1/g')  # max number of failed proposals
  fabs=$(grep "ftolAbs" log/"${filename}".log | sed -E 's/.*ftolAbs=(.+),/\1/g')  # tuning parameter called "ftolAbs" in the log file
  frel=$(grep "ftolRel" log/"${filename}".log | sed -E 's/.*ftolRel=(.+), f.*/\1/g')  # "ftolRel"
  xabs=$(grep "xtolAbs" log/"${filename}".log | sed -E 's/.*xtolAbs=(.+), x.*/\1/g')  # "xtolAbs"
  xrel=$(grep "xtolRel" log/"${filename}".log | sed -E 's/.*xtolRel=(.+)./\1/g')  # "xtolRel"
  seed=$(grep "main seed" log/"${filename}".log | sed -E 's/[^0-9]*([0-9]+).*/\1/g')  # main seed, i.e. seed for the first runs
  allthree=""
  for i in {3460,3450,3440}  # calculate number of runs with a network score under 3460,3450,3440
  do
    num=0
    for score in $(grep 'loglik of best' log/"${filename}".log | sed -E 's/.*loglik of best (.*)\..*$/\1/g') # get network scores for each analysis
    do
      if [ $score -lt $i ]  # compare scores with 3460,3450,3440
      then
        ((num=num+1))
      fi
    done
    allthree=${allthree},${num}  # put under3460,under3450,under3440 in one variable: allthree
  done
  echo "$filename,$h,$CPUtime,$Nruns,$Nfail,$fabs,$frel,$xabs,$xrel,$seed$allthree" >> summary.csv
done
