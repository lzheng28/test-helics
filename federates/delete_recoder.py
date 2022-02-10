import fileinput
frm = 2
to = 101

file_path = "Example_ds_15/Distribution" + "/IEEE_123_feeder_0.glm"
print(file_path)
j = 0
file_data = ""
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        old_str = line
        j = j + 1
        if j >= 6815 and j <= 6831:
            new_str = "// " + old_str
            line = line.replace(old_str,new_str)
        file_data += line
with open(file_path,"w",encoding="utf-8") as f:
    f.write(file_data)

for i in range(frm, to):
    file_path = "Example_ds_15/Distribution_" + str(i) + "/IEEE_123_feeder_0.glm"
    print(file_path)
    j = 0
    file_data = ""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            old_str = line
            j = j + 1
            if j >= 6815 and j <= 6831:
                new_str = "// " + old_str
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(file_data)