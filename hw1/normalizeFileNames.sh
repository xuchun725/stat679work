for x in {1..9}
do
  mv log/timetest"$x"_snaq.log log/timetest0"$x"_snaq.log
  mv out/timetest"$x"_snaq.out out/timetest0"$x"_snaq.out
done
