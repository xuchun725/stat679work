# Create a table in csv format to summarize the the results of all these analysis in log/ and out/.
# 1 row per analysis and 3 columns
# Usage: in `stat679work/hw1`, run `bash summarizeSNaQres.sh`
echo "analysis,h,CPUtime" > summary.csv
for filename in $(ls -l log | grep -oE "\w*\.log" | grep -oE "\w*[^(.log)]")
do
  h=$(grep -oE "hmax = [0-9]+" log/"${filename}".log | grep -oE "[0-9]+")
  CPUtime=$(grep "Elapsed time" out/"${filename}".out | grep -oE "[0-9]+.[0-9]+")
  echo "$filename,$h,$CPUtime" >> summary.csv
done
