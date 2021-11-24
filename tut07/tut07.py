import pandas as pd


ltp_dict = {}
main_dict = {}


def check(dict_submit_, dict1, roll):
    if roll in dict1:
        t = dict1[roll].copy()
        m = len(t)
        lis1 = []
        n = len(dict_submit_)
        if(m != n):
            for i in t:
                x = ltp_dict[i]
                if(dict_submit_.count(i) != x[0][1]):
                    if t.count(i) != x[0][1]:
                        d = x[0][1]-t.count(i)
                        while(d > 0):
                            lis1.append(i)
                            d -= 1
                lis1.append(i)
            for j in dict_submit_:
                x = ltp_dict[j]
                if j in lis1:
                    lis1.remove(j)
            if(len(lis1)) != 0:
                if roll in main_dict:
                    main_dict[roll].append(lis1)
                else:
                    main_dict[roll] = []
                    main_dict[roll].append(lis1)
                return roll


def ltp_integers(x):
    count = 0
    zeroes = 0
    for i in range(len(x)):
        if((x[i]) == "0"):
            zeroes += 1
    count = 3-zeroes
    return count


def feedback_not_submitted():
    ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3: 'practical'}
    output = "course_feedback_remaining.xlsx"
    df = pd.read_csv
    roll_nos= df['rollno'].values.tolist()
    data = df[['register_sem', 'schedule_sem', 'subno']].values.tolist()
    subs = df['subno'].values.tolist()
    unrepeat_rollno = set(roll_nos)
    dict1 = {}
    i = 0
    for k in roll_nos:
        if k in dict1:
            dict1[k].append(subs[i])
        else:
            dict1[k] = []
            dict1[k].append(subs[i])
        i += 1
    i = 0

    dict_data = {}
    for sub in subs:
        dict_data[sub] = []
        dict_data[k] = data[i]
        i += 1
    file = pd.read_csv("course_feedback_submitted_by_students.csv")
    sub_submit_ = file['course_code'].values.tolist()
    roll_submit_ = file['stud_roll'].values.tolist()
    unrepeat_rollno_submit_ = set(file)
    dict_submit_ = {}
    m = 0
    for j in roll_submit_:
        if k in dict_submit_:
            dict_submit_[k].append(sub_submit_[l])
        else:
            dict_submit_[k] = []
            dict_submit_[k].append(sub_submit_[l])
        l += 1
        info = pd.read_csv('studentinfo.csv')
        ltp = pd.read_csv('course_master_dont_open_in_excel.csv')

        list_of_ltp = ltp['ltp'].values.tolist()
        sub_of_ltp = ltp['subno'].values.tolist()
        l = 0
        for k in sub_of_ltp:
            integers = ltp_integers(list_of_ltp[l])
        if k in ltp_dict:
            ltp_dict[k].append([list_of_ltp[l], integers])
        else:
            ltp_dict[k] = []
            ltp_dict[k].append([list_of_ltp[l], integers])
        l += 1
    list_info = info[['Name', 'email', 'aemail', 'contact']].values.tolist()
    roll_info = info['Roll No'].values.tolist()
    dict_info = {}
    l = 0
    for k in roll_info:
        if k in dict_info:
            dict_info[k].append(info[l])
        else:
            dict_info[k] = []
            dict_info[k].append(info[l])
        l += 1
    for i in unrepeat_rollno_submit_:
        if i in ltp_dict:
            temp = check(ltp_dict[i], dict1, i)
    output_list = [[]]
    for i in main_dict:
        for j in main_dict[i]:
            for k in j:
                lis_emp = []
                lis_emp.append(i)
                lis_emp.extend(dict_data[k])
                p = dict_info[i]
                for l in range(4):
                    lis_emp.append(p[0][l])
                    output_list.append(lis_emp)
    print(output_list)
    output_data = pd.DataFrame(output_list, columns=[
                                   'rollno', 'register_sem', 'schedule_sem', 'subno', 'Name', 'email', 'aemail', 'contact'])
    print(output_data.head())


feedback_not_submitted()
