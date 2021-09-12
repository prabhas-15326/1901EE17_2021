import os
import csv
import openpyxl

def Output_by_Roll_Number(roll_no):
    file_exist=0
    if os.path.isfile("./"+roll_no[0]+".csv"):
        file_exist=1
    with open(roll_no[0]+".csv", 'a+', newline='') as f:
        # creating roll number in csv file in append mode
        writer = csv.writer(f)
        if not file_exist:
            writer.writerow(header)
        writer.writerow([roll_no[0], roll_no[1], roll_no[2], roll_no[3]])


def Output_by_Subject(subject):
    file_exist=0
    if os.path.isfile("./"+subject[2]+".csv"):
        file_exist=1
    with open(subject[2]+".csv", 'a+', newline='') as f:
        # creating subject in csv file in append mode 
        writer = csv.writer(f)
        if not file_exist:
            writer.writerow(['rollno', 'register_sem', 'sub_code', 'sub_type'])
        writer.writerow([subject[0], subject[1], subject[2], subject[3]])

def csv_xlsx(y):
    # creating xlsx file
    wb = openpyxl.Workbook()
    ws = wb.active
    with open(y+'.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            ws.append(row)
    wb.save(y+'.xlsx')  #saving a file as xlsx
    os.remove(y+'.csv') #removing csv files

l=[]; k=[]  #creating empty list
# Taking "regtable_old.csv" as input file in reading mode
with open("regtable_old.csv", "r") as input:
    # reading a file in csv 
    reader = csv.reader(input, delimiter=',')
    header = next(reader) 
    del header[2], header[3], header[3], header[3], header[3]
    for row in reader:
        del row[2], row[3], row[3], row[3], row[3]
        Output_by_Subject(row)
        Output_by_Roll_Number(row)
        k.append(row[0])    #adding the roll numbers to the list
        l.append(row[2])    #adding the subjects to the list
       
for i in l:
    # checking whether the list has xlsx file 
    if not os.path.isfile("./"+i+".xlsx"):
       csv_xlsx(i)
for j in k:
    # checking whether the list has xlsx file
    if not os.path.isfile("./"+j+".xlsx"):
        csv_xlsx(j)
    
    
    
    
