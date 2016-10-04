# Create a table in csv format to summarize the the results of all these analysis in log/ and out/.
# 1 row per analysis and 3 columns
# Usage: in `stat679work/hw1`, run `bash summarizeSNaQres.sh`
echo "analysis, h, CPUtime" > summary.csv
for filename in $(ls -l log | grep -oE "\w*\.log" | cut -f1 -d'.')
do
  h=$(grep -oE "hmax = [0-9]+" log/"$filename".log | cut -f3 -d' ')
  CPUtime=$(grep "Elapsed time" out/"$filename".out | cut -f4 -d' ')
  echo "$filename, $h, $CPUtime" >> summary.csv
done
