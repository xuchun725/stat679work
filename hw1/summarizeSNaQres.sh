echo "analysis, h, CPUtime" > table.csv
for filename in $(ls -l log | grep -oE "\w*\.log" | cut -f1 -d'.')
do
  h=$(grep -oE "hmax = [0-9]+" log/"$filename".log | cut -f3 -d' ')
  CPUtime=$(grep "Elapsed time" out/"$filename".out | cut -f4 -d' ')
  echo "$filename, $h, $CPUtime" >> table.csv
done
