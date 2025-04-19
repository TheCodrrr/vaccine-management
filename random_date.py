import datetime as dt
import random as rd

def ZeroAdder(num1):
    if len(str(num1)) == 1 and str(num1).isdigit():
        return f"0{num1}"
    else:
        return f"{num1}"

date_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
leap_date_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def GenerateDate():
    date1 = dt.datetime.now()
    date1 = str(date1.date())
    date1 = date1.split('-')
    date1 = [str(date1[2]), str(date1[1]), str(date1[0])]
    date2 = []
    for i in date1:
        date2.append(int(i))
    # date2 = [21, 5, 2005]
    date_num = date2[0] + 5
    month_days = date_dict[date2[1]]
    date3 = []
    if date2[0] in [27, 28, 29, 30, 31] and date2[1] == 12:
        numx = 5 - (31 - date2[0])
        if numx == 1:
            day = rd.randint(1, 31)
            month = 1
            year = date2[2] + 1
            date3 = [day, month, year]
        else:
            # 28-12-2020
            date1 = [rd.randint(numx, 31), 1, date2[2] + 1]
            date2 = [rd.randint(1, numx), 2, date2[2] + 1]
            final_date = [date1, date2]
            date3 = rd.choice(final_date)
    elif date_num > month_days:
        date3 = [date_num - month_days, date2[1] + 1, date2[2]]
    else:
        date3 = [date2[0] + 5, date2[1], date2[2]]
    if int(date3[1]) > 12:
        date3[1] = "01"
        date3[2] = ZeroAdder(int(date3[2]) + 1)
    rd_num1 = [ZeroAdder(rd.randint(int(date3[0]), date_dict[date3[1]])), ZeroAdder(date3[1]), str(date3[2])]
    rd_num2 = [ZeroAdder(rd.randint(1, 30 - (date_dict[date3[1]] - int(date3[0])))), ZeroAdder(date3[1] + 1), str(date3[2])]
    if rd_num2[1] == '13':
        rd_num2 = [rd_num2[0], '01', str(int(rd_num2[2]) + 1)]
    rd_num = [rd_num1, rd_num2]
    return '-'.join(rd.choice(rd_num))