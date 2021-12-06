import pandas as pd
import xlsxwriter
import os
import openpyxl
import numpy as np
from xlsxwriter import workbook
from openpyxl.reader.excel import load_workbook


def generating_marksheet(positive_marks,negative_marks):
    Max=28
    non_attempted=0

    # reading master roll data
    master_roll_data = pd.read_csv('sample_input\master_roll.csv')


    # creating a list of roll numbers
    roll_list=[]
    for roll in master_roll_data["roll"]:
        roll_list.append(roll)


    name_list=[]
    for name in master_roll_data["name"]:
        name_list.append(name)


    # reading response data and deleting unnecessary columns
    responses_list=[]
    responses_data = pd.read_csv('sample_input\\responses.csv')



    option_list=[]
    for index,row in responses_data.iterrows():
        list=[]
        for i in row:
            list.append(i)
        option_list.append(list[7:])


    score_list=[]
    for index,row in responses_data.iterrows():
        score_list.append(row[2])


    # creating a sample_ouput folder
    parent_dir= "sample_output"
    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)

    main_dir= "sample_output/marksheet"
    if not os.path.exists(main_dir):
        os.mkdir(main_dir)

    # creating xlsx files and adding logo to the files
    for i in range(len(roll_list)):
        writer = pd.ExcelWriter(main_dir+"/"+roll_list[i]+'.xlsx', engine ='xlsxwriter')
        workbook=xlsxwriter.Workbook(writer)
        worksheet=workbook.add_worksheet('quiz')

        cell_format=workbook.add_format()
        cell_format.set_bold()
        cell_format.set_align("center")
        cell_format.set_font_size(18)
        cell_format.set_font_name("century")

        worksheet.insert_image('A1','logo.png') 
        worksheet.write(7,2,'MARK SHEET',cell_format) 
        border_format=workbook.add_format({'border':1})
        worksheet.conditional_format( 'A13:E16' , { 'type' : 'blanks' , 'format' : border_format} )
        worksheet.conditional_format( 'A13:E16' , { 'type' : 'no_blanks' , 'format' : border_format} )
        worksheet.conditional_format( 'A19:B47' , { 'type' : 'blanks' , 'format' : border_format} )
        worksheet.conditional_format( 'A19:B47' , { 'type' : 'no_blanks' , 'format' : border_format} )
        worksheet.set_column('A:E',20)

        format_top=workbook.add_format()
        format_top.set_align("right")
        format_top.set_font_name("century")

        format=workbook.add_format()
        format.set_bold()
        format.set_font_name("century")
        format.set_font_size(12)

        format_headings=workbook.add_format()
        format_headings.set_bold()
        format_headings.set_align("center")
        format_headings.set_font_name("century")
        format_headings.set_font_size(12)

        format_align=workbook.add_format()
        format_align.set_align("center")
        format_align.set_font_name("century")

        format_blue=workbook.add_format()
        format_blue.set_align("center")
        format_blue.set_font_color('blue')
        format_blue.set_font_name("century")

        format_green=workbook.add_format()
        format_green.set_align("center")
        format_green.set_font_color('green')
        format_green.set_font_name("century")

        format_red=workbook.add_format()
        format_red.set_align("center")
        format_red.set_font_color('red')
        format_red.set_font_name("century")

        worksheet.write(9,0,'NAME :',format_top)
        worksheet.write(9,1,name_list[i],format)
        worksheet.write(9,4,'Exam :',format_top)
        worksheet.write(9,5,'quiz',format)
        worksheet.write(10,0,'RollNO :',format_top)
        worksheet.write(10,1,roll_list[i],format)
        worksheet.write(18,0,'Student Ans',format_headings)
        worksheet.write(18,1,'Corrected Ans',format_headings)

        for row in range(len(option_list[i])):
            try:
                worksheet.write(row+19,0,option_list[i][row],format_green)
            except:
                pass
        for row in range(len(option_list[0])):
            worksheet.write(row+19,1,option_list[0][row],format_blue)
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
        worksheet.write(12,1,"Right",format_headings)
        worksheet.write(12,2,"Wrong",format_headings)
        worksheet.write(12,3,"Not Attempt",format_headings)
        worksheet.write(12,4,"Max",format_headings)
        worksheet.write(13,1,right,format_green)
        worksheet.write(13,2,wrong,format_red)
        worksheet.write(13,3,Not_attempted,format_align)
        worksheet.write(13,4,Max,format_align)
        worksheet.write(13,0,"No.",format_headings)
        worksheet.write(14,0,"Marking",format_headings)
        worksheet.write(15,0,"Total",format_headings)
        worksheet.write(14,1,positive_marks,format_green)
        worksheet.write(14,2,negative_marks,format_red)
        worksheet.write(14,3,non_attempted,format_align)
        worksheet.write(15,1,(positive_marks*right),format_green)
        worksheet.write(15,2,(negative_marks*wrong),format_red)
        worksheet.write(15,4,str(((positive_marks*right)+(negative_marks*wrong)))+"/140",format_blue)
        responses_data.loc[i,"Score_After_Negative"]=str(((positive_marks*right)+(negative_marks*wrong)))+"/140"
        responses_data.loc[i,"statusAns"]="["+str(right)+","+str(wrong)+","+str(Not_attempted)+"]"
        writer.save()
        workbook.close()


