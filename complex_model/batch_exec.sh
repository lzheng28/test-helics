for i in {4..15}
do
  echo $i
  cp execute.py Example_ds_$i
  cd Example_ds_$i
  python execute.py
  cd ..
done
