for i in {5..15}
do
  cp execute.py Example_ds_$i
  cd Example_ds_$i
  python execute.py > 2-11.log
  cd ..
done