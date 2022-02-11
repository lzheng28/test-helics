for i in {3..15}
do
  cp execute.py Example_ds_$i
  cd Example_ds_$i
  python execute.py > 2-13.log
  cd ..
done
