for i in {3..5}
do
  cp execute.py Example_ds_$i
  cd Example_ds_$i
  python execute.py > 2-12.log
  cd ..
done
