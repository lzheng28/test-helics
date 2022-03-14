# for i in {4..15}
# do
#   git rm -r --cached Example_ds_$i/Distribution*/gridlabd.xml Example_ds_$i/Distribution*/output/*.csv
# done

for i in {4..15}
do
  rm -r Example_ds_$i/Distribution*/gridlabd.xml Example_ds_$i/Distribution*/output/*.csv
done