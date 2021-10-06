import csv 
from openpyxl.workbook import Workbook
import os

grades = {}
names_roll = {}
subjects_master = {}
file_names_roll = open("names-roll.csv", 'r')
file_subject_master = open("subjects_master.csv", 'r')

csvreader01 = csv.DictReader(file_names_roll)
for row in csvreader01:
  names_roll[row['Roll']] = row['Name']
csvreader02 = csv.DictReader(file_subject_master)
for row in csvreader02:
  subjects_master[row['subno']] = [row['subname'],row['ltp'],row['crd']]
  file_grades = open("grades.csv", 'r')
csvreader03 = csv.DictReader(file_grades)
for row in csvreader03:
  if not row['Roll'] in grades.keys():
    grades[row['Roll']] = {}
    if row['Sem'] not in grades[row['Roll']].keys():
      grades[row['Roll']][row['Sem']] = [[ row['SubCode'],subjects_master[row['SubCode']][0],subjects_master[row['SubCode']][1],subjects_master[row['SubCode']][2],row['Sub_Type'],row['Grade']]]
    else:
       grades[row['Roll']][row['Sem']].append([ row['SubCode'],subjects_master[row['SubCode']][0],subjects_master[row['SubCode']][1],subjects_master[row['SubCode']][2],row['Sub_Type'],row['Grade']])
  else:
    if row['Sem'] not in grades[row['Roll']].keys():
      grades[row['Roll']][row['Sem']] = [[ row['SubCode'],subjects_master[row['SubCode']][0],subjects_master[row['SubCode']][1],subjects_master[row['SubCode']][2],row['Sub_Type'],row['Grade']]]
    else:
       grades[row['Roll']][row['Sem']].append([ row['SubCode'],subjects_master[row['SubCode']][0],subjects_master[row['SubCode']][1],subjects_master[row['SubCode']][2],row['Sub_Type'],row['Grade']])

grades = {'BB': 8, 'BC': 7, 'AB' : 9, 'CC' : 6, 'AA' : 10, 'CD' : 5, 'DD' : 4, 'F' : 0, 'F*' : 0, 'DD*' : 4}
for roll in grades.keys():
  overall_sem = []
  overall_sem.append(['Roll No.', roll])
  overall_sem.append(['Name of the Student',names_roll[roll]])
  overall_sem.append(['Discipline',roll[4:6]])
  sem = ['Semester No.']
  cred = ['Semester wise Credit Taken']
  spi = ['SPI']
  t_cred = ['Total Credits Taken']
  cpi = ['CPI']
  filepath = 'output/' + roll + '.xlsx'
  directory = os.path.dirname(filepath)
  if not os.path.exists(directory):
    os.makedirs(directory)
  wb = Workbook()
  for sem in grades[roll].keys():
    sem.append(sem)
    sl_num = 1 
    credt = 0
    sp_i = 0 
    ws = wb.create_sheet()
    ws.title = 'Sem' + sem
    ws.append(['Sl No.','Subject Name','L-T-P','Credit','Subject Type','Grade'])    
    for data in grades[roll][sem]:
      sp_i += int(data[3]) * grades[data[5]]
      credt += int(data[3]) 
      data.insert(0,sl_num)
      ws.append(data)
      sl_num += 1 
    cred.append(credt)
    spi.append(round(sp_i/credt,2))
    if type(t_cred[-1]) == str:
      t_cred.append(credt)
    else:
      a = credt
      a += t_cred[-1] + credt
      t_cred.append(a) 

  overall_sem.append(sem)
  overall_sem.append(cred)
  overall_sem.append(spi)
  overall_sem.append(t_cred)
  ws = wb['Sheet']
  for row in overall_sem:
    ws.append(row)
  wb.save(filename=filepath)


