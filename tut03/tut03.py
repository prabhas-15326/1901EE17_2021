import os

def Output_by_Roll_Number(y):
    file_exist=0
    if os.path.isfile("./"+y[0]+".csv"):
        file_exist=1
    with open(y[0]+".csv","a+") as output:
        if not file_exist:
            output.write("rollno,register_sem,sub_code,sub_type\n")
        output.write(y[0]+","+y[1]+","+y[2]+","+y[3]+"\n")
    return 0

def Output_by_Subject(y):
    file_exist=0
    if os.path.isfile("./"+y[2]+".csv"):
        file_exist=1
    with open(y[2]+".csv","a+") as f:
        if not file_exist:
            f.write("rollno,register_sem,sub_code,sub_type\n")
        f.write(y[0]+","+y[1]+","+y[2]+","+y[3]+"\n")
    return 0

# Taking "regtable_old.csv" as input file in reading mode
with open("regtable_old.csv", "r") as f:
    for i in f.readlines()[1:]:
        x=i.strip().split(",")
        del x[4],x[4],x[4],x[4],x[2]
        Output_by_Roll_Number(x)
        Output_by_Subject(x)