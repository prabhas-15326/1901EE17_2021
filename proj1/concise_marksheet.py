import pandas as pd
import xlsxwriter
import openpyxl
import numpy as np
from xlsxwriter import workbook
from openpyxl.reader.excel import load_workbook

def concisemarksheet(positive_marks,negative_marks):
    Max=28
    non_attempted=0


    # reading master roll data
    master_roll_data = pd.read_csv('sample_input\master_roll.csv')

    # reading response data and deleting unnecessary columns
    responses_data = pd.read_csv('sample_input\\responses.csv')

    # creating a list of roll numbers
    roll_list=[]
    for roll in master_roll_data["roll"]:
        roll_list.append(roll)

    option_list=[]
    for index,row in responses_data.iterrows():
        list=[]
        for i in row:
            list.append(i)
        option_list.append(list[7:])


    # creating columns 
    responses_data = pd.read_csv('sample_input\\responses.csv')
    responses_data = responses_data.rename(columns={"Score":"Google_Score"})
    responses_data.insert(6,"Score_After_Negative",np.nan)
    responses_data["statusAns"]=np.nan


    # creating xlsx files and adding logo to the files
    for i in range(len(roll_list)):
        right=0
        wrong=0
        Not_attempted=0
        for row in range(len(option_list[i])):
            if option_list[0][row] == option_list[i][row]:
                right+=1 
            elif str(option_list[i][row]) != 'nan':
                wrong+=1
            else:
                Not_attempted+=1
        responses_data.loc[i,"Score_After_Negative"]=str(((positive_marks*right)+(negative_marks*wrong)))+"/140"
        responses_data.loc[i,"statusAns"]="["+str(right)+","+str(wrong)+","+str(Not_attempted)+"]"

    # converting to xlsx file
    responses_data.to_excel("sample_output/marksheet/concise_marksheet.xlsx",index=False)
    
    # changing the sheet name
    sheet_s=openpyxl.load_workbook("sample_output/marksheet/concise_marksheet.xlsx")
    ss_sheet = sheet_s['Sheet1']
    ss_sheet.title = 'concisemarksheet'
    sheet_s.save("sample_output/marksheet/concise_marksheet.xlsx")



