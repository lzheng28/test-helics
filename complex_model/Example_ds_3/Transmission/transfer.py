#transfer.py
filepath1 = '/home/lei/Desktop/test-helics/complex_model/Example_ds_3/Transmission/classical_model_3000bus.dyr.bak'
generator = []
with open(filepath1, "r", encoding="utf-8") as f:
    for line in f:
        a = line.split(' ')
        generator.append(a[0])

print('generator = ', generator)

filepath2 = '/home/lei/Desktop/test-helics/complex_model/Example_ds_3/Transmission/classical_model_3000bus.dyr'

file_data = ""
with open(filepath2, "r", encoding="utf-8") as f:
    count = 0
    index = 0
    generator_index = 0
    for line in f:
        if(count == index and generator_index < len(generator)):
            index = index + 7
            old_str = line
            tmp = old_str.split(' ')
            tmp[0] = generator[generator_index]
            generator_index = generator_index + 1
            new_str = ''
            for j in range(len(tmp)):
                if j != 0:
                    new_str = new_str + ' ' + tmp[j]
                else:
                    new_str = new_str + tmp[j]
            line = line.replace(old_str, new_str)
        file_data += line
        count = count + 1
with open(filepath2,"w",encoding="utf-8") as f:
    f.write(file_data)

file_data = ""                
with open(filepath2, "r", encoding="utf-8") as f:
    count = 0
    index = 1
    generator_index = 0
    for line in f:
        if(count == index and generator_index < len(generator)):
            index = index + 7
            old_str = line
            tmp = old_str.split(' ')
            tmp[0] = generator[generator_index]
            generator_index = generator_index + 1
            new_str = ''
            for j in range(len(tmp)):
                if j != 0:
                    new_str = new_str + ' ' + tmp[j]
                else:
                    new_str = new_str + tmp[j]
            line = line.replace(old_str, new_str)
        file_data += line
        count = count + 1
with open(filepath2,"w",encoding="utf-8") as f:
    f.write(file_data)

file_data = ""
with open(filepath2, "r", encoding="utf-8") as f:
    count = 0
    index = 2
    generator_index = 0
    for line in f:
        if(count == index and generator_index < len(generator)):
            index = index + 7
            old_str = line
            tmp = old_str.split(' ')
            tmp[0] = generator[generator_index]
            generator_index = generator_index + 1
            new_str = ''
            for j in range(len(tmp)):
                if j != 0:
                    new_str = new_str + ' ' + tmp[j]
                else:
                    new_str = new_str + tmp[j]
            line = line.replace(old_str, new_str)
        file_data += line
        count = count + 1
with open(filepath2,"w",encoding="utf-8") as f:
    f.write(file_data)
