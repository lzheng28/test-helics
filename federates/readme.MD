1. To compile:

g++ fed1.cpp -o fed1 -I /home/lei/software/helics-2.6.1/include/ -L /home/lei/software/helics-2.6.1/lib -lhelicsSharedLib

g++ fed2.cpp -o fed2 -I /home/lei/software/helics-2.6.1/include/ -L /home/lei/software/helics-2.6.1/lib -lhelicsSharedLib

2. To run:

Three termimals, run ```./fed1```, ```./fed2```, ```helics_broker -f 2``` respectively.
