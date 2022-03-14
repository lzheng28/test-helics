import fileinput
import os
import datetime

print(datetime.datetime.now())

np = [1, 2, 4, 8, 12, 16]

file_path = '.co_sim_1a.json'
for i in np:
    # os.system('cp co_sim_1a.json .co_sim_1a.json')
    # print(file_path)
    # file_data = ""
    # with open(file_path, "r", encoding="utf-8") as f:
    #     for line in f:
    #         old_str = line
    #         tmp = old_str.split(' ')
    #         # print(tmp)
    #         new_str = ''
    #         if tmp.count('hadrec.x'):
    #             for j in range(len(tmp)):
    #                 if(tmp[j] == '-np'):
    #                     tmp[j + 1] = str(i)
    #                 new_str = new_str + ' '+ tmp[j]
    #             line = line.replace(old_str,new_str)
    #         elif 'TransmissionFederate' in old_str:
    #             # print(old_str)
    #             # print(tmp)
    #             for j in range(len(tmp)):
    #                 if('TransmissionFederate' in tmp[j]):
    #                     tmp[j] = '"name":"TransmissionFederate_np_' + str(i) + '"' + '\n'
    #                 new_str = new_str + ' ' + tmp[j]
    #                 # print(tmp[j])
    #                 # print(new_str)
    #             line = line.replace(old_str,new_str)
    #         file_data += line
    # with open(file_path,"w",encoding="utf-8") as f:
    #     f.write(file_data)
    # os.system('helics run --path .co_sim_1a.json')
    os.system('mpirun -np ' + str(i) + ' hadrec.x input_3000.xml > ' + "TransmissionFederate_np_" + str(i) + '.log')
    # read execution time from log file
    log_file = "TransmissionFederate_np_" + str(i) + '.log'
    with open(log_file, "r", encoding="utf-8") as f:
        flag = False
        for line in f:
            if flag == True:
                print('np: ', i, ' execution time: ')
                tmp = line.split(' ')
                for j in range(len(tmp)):
                    if '.' in tmp[j]:
                        print(tmp[j])
                flag = False
            if "Dynamic Simulation: Total Application" in line:
                flag = True

# os.system('rm .co_sim_1a.json')

