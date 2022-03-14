1. To compile:

g++ fed1.cpp -o fed1 -I /home/lei/software/helics-2.6.1/include/ -L /home/lei/software/helics-2.6.1/lib -lhelicsSharedLib

g++ fed2.cpp -o fed2 -I /home/lei/software/helics-2.6.1/include/ -L /home/lei/software/helics-2.6.1/lib -lhelicsSharedLib

2. To run:

Three termimals, run ```./fed1```, ```./fed2```, ```helics_broker -f 2``` respectively.

3. 更新代码并编译GridPACK：
```
cd home/lei/package/GridPACK_ds/src/build
git pull
./build_config.sh
make -j 4
```

4. 添加hadrec.x 到~/.bashrc(路径需要替换成编译hadrec.x的路径)
```
export PATH="/home/lei/package/GridPACK_ds/src/build/applications/hadrec/:$PATH"
source ~/.bashrc
source activate py3.7-helics-2.6.1
```

5. 运行test样例：
```
cd /home/lei/workfile/test-helics/federates
git pull
cp execute.py Example_ds_*/.
cd Example_ds_*
python3 execute.py
```



