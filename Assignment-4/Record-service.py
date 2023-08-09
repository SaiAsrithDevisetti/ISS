import sqlite3
import csv

conn = sqlite3.connect('record.db')   # create connection
cur = conn.cursor()    # create cursor

# create table named Ticker
cur.execute("""CREATE TABLE Ticker (
    Date TEXT,
    Company_Name TEXT,
    Industry TEXT,
    Pervious_Day_Price REAL,
    Current_Price REAL,
    Change_in_Price REAL,
    Confidence TEXT
    )""")
company_name = []   # list which stores company name
industry = []       # list which stores industry of the company
day1_val = []       # list which stores day1 prices
day2_val = []       # list which stores day2 prices
day3_val = []       # list which stores day3 prices
day4_val = []       # list which stores day4 prices
day5_val = []       # list which stores day5 prices
with open('Record/2021111022 Date 20-05-2022.csv', 'r') as csv_1:
    csv_read1 = csv.DictReader(csv_1)
    for col1 in csv_read1:
        company_name.append(col1['Company Name'])
        industry.append(col1['Industry'])
        day1_val.append(col1['Last Price'])
with open('Record/2021111022 Date 21-05-2022.csv', 'r') as csv_2:
    csv_read2 = csv.DictReader(csv_2)
    for col2 in csv_read2:      # appending day2 prices into list
        day2_val.append(col2['Last Price'])
with open('Record/2021111022 Date 22-05-2022.csv', 'r') as csv_3:
    csv_read3 = csv.DictReader(csv_3)
    for col3 in csv_read3:      # appending day3 prices into list
        day3_val.append(col3['Last Price'])
with open('Record/2021111022 Date 23-05-2022.csv', 'r') as csv_4:
    csv_read4 = csv.DictReader(csv_4)
    for col4 in csv_read4:       # appending day4 prices into list
        day4_val.append(col4['Last Price'])
with open('Record/2021111022 Date 24-05-2022.csv', 'r') as csv_5:
    csv_read5 = csv.DictReader(csv_5)
    for col5 in csv_read5:      # appending day5 prices into list
        day5_val.append(col5['Last Price'])
# data base table: day1
cur.execute("""CREATE TABLE DB_Day1 (
    Date TEXT,
    Company_Name TEXT,
    Industry TEXT,
    Current_Price REAL
    )""")
# data base table: day2
cur.execute("""CREATE TABLE DB_Day2 (
    Date TEXT,
    Company_Name TEXT,
    Industry TEXT,
    Current_Price REAL
    )""")
# data base table: day3
cur.execute("""CREATE TABLE DB_Day3 (
    Date TEXT,
    Company_Name TEXT,
    Industry TEXT,
    Current_Price REAL
    )""")
# data base table: day4
cur.execute("""CREATE TABLE DB_Day4 (
    Date TEXT,
    Company_Name TEXT,
    Industry TEXT,
    Current_Price REAL
    )""")
# data base table: day5
cur.execute("""CREATE TABLE DB_Day5 (
    Date TEXT,
    Company_Name TEXT,
    Industry TEXT,
    Current_Price REAL
    )""")
# insertion of data into data base tables
for i in range(0, 89):
    cur.execute("""INSERT INTO DB_Day1 VALUES('20-05-2022',?, ?, ?);""", [company_name[i], industry[i], day1_val[i]])
for i in range(0, 89):
    cur.execute("""INSERT INTO DB_Day2 VALUES('21-05-2022',?, ?, ?);""", [company_name[i], industry[i], day2_val[i]])
for i in range(0, 89):
    cur.execute("""INSERT INTO DB_Day3 VALUES('22-05-2022',?, ?, ?);""", [company_name[i], industry[i], day3_val[i]])
for i in range(0, 89):
    cur.execute("""INSERT INTO DB_Day4 VALUES('23-05-2022',?, ?, ?);""", [company_name[i], industry[i], day4_val[i]])
for i in range(0, 89):
    cur.execute("""INSERT INTO DB_Day5 VALUES('24-05-2022',?, ?, ?);""", [company_name[i], industry[i], day5_val[i]])

change1 = []        # list which stores change on second day
change2 = []        # list which stores change on third day
change3 = []        # list which stores change on fourth day
change4 = []        # list which stores change on fivth day
instructions = []   # list which stores instructions from control
ranges = []         # from the instruction we obtain ranges to assign confidence

for i in range(0, 89):
    change1.append(((float(day2_val[i]) - float(day1_val[i])) / float(day1_val[i])) * 100)      # calculated per first day onto second day
    change2.append(((float(day3_val[i]) - float(day1_val[i])) / float(day1_val[i])) * 100)      # calculated per first day onto third day
    change3.append(((float(day4_val[i]) - float(day1_val[i])) / float(day1_val[i])) * 100)      # calculated per first day onto fourth day
    change4.append(((float(day5_val[i]) - float(day1_val[i])) / float(day1_val[i])) * 100)      # calculated per first day onto fivth day

with open('Control/control-table.csv', 'r') as control:
    control_tab = csv.DictReader(control)
    for col6 in control_tab:
        instructions.append(col6['Change in Price Percent'])     # appends instuctions as strings into list


def extract_nums(string):        # function to recognise and return integers in a string
    nums = []
    for char in string:
        if char.isnumeric():
            num = float(char)
            nums.append(num)
    return nums                 # returns the integers in the string as lists


for i in range(0, 9):
    ranges.append(extract_nums(instructions[i]))   # ranges contains the integers present in the instructions
conf1 = []      # stores confidence of second day
conf2 = []      # stores confidence of third day
conf3 = []      # stores confidence of fourth day
conf4 = []      # stores confidence of fivth day
high1, high2, high3, low1, low2, low3 = 0, 0, 0, 0, 0, 0
for i in range(0, 89):                                               # this for loop deals with change % on second day
    if(industry[i] == 'Finance - General'):
        if(change1[i] < ranges[0][0]):
            conf1.append('Low')
            low1 += 1   # there is increment in low1 when low is obtained on Finance
        if(change1[i] >= ranges[1][0] and change1[i] <= ranges[1][1]):
            conf1.append('Medium')
        if(change1[i] > ranges[2][0]):
            conf1.append('High')
            high1 += 1   # there is increment in high1 when high is obtained on Finance
    if(industry[i] == 'Auto Ancillaries'):
        if(change1[i] < ranges[3][0]):
            conf1.append('Low')
            low2 += 1   # there is increment in low2 when low is obtained on Auto Ancillaries
        if(change1[i] >= ranges[4][0] and change1[i] <= (10 * ranges[4][1])):
            conf1.append('Medium')
        if(change1[i] > (10 * ranges[5][0])):
            conf1.append('High')
            high2 += 1   # there is increment in high2 when high is obtained on Auto Ancillaries
    if(industry[i] == 'Ceramics & Granite'):
        if(change1[i] < ranges[6][0]):
            conf1.append('Low')
            low3 += 1   # there is increment in low3 when low is obtained on Ceramics & Granite
        if(change1[i] >= ranges[7][0] and change1[i] <= ranges[7][1]):
            conf1.append('Medium')
        if(change1[i] > ranges[8][0]):
            conf1.append('High')
            high3 += 1   # there is increment in high3 when high is obtained on Ceramics & Granite

for i in range(0, 89):                                              # this for loop deals with change % on third day
    if(industry[i] == 'Finance - General'):
        if(change2[i] < ranges[0][0]):
            conf2.append('Low')
            low1 += 1   # there is increment in low1 when low is obtained on Finance
        if(change1[i] >= ranges[1][0] and change2[i] <= ranges[1][1]):
            conf2.append('Medium')
        if(change1[i] > ranges[2][0]):
            conf2.append('High')
            high1 += 1   # there is increment in high1 when high is obtained on Finance
    if(industry[i] == 'Auto Ancillaries'):
        if(change2[i] < ranges[3][0]):
            conf2.append('Low')
            low2 += 1   # there is increment in low2 when low is obtained on Auto Ancillaries
        if(change2[i] >= ranges[4][0] and change2[i] <= (10 * ranges[4][1])):
            conf2.append('Medium')
        if(change2[i] > (10 * ranges[5][0])):
            conf2.append('High')
            high2 += 1   # there is increment in high2 when high is obtained on Auto Ancillaries
    if(industry[i] == 'Ceramics & Granite'):
        if(change2[i] < ranges[6][0]):
            conf2.append('Low')
            low3 += 1   # there is increment in low3 when low is obtained on Ceramics & Granite
        if(change2[i] >= ranges[7][0] and change2[i] <= ranges[7][1]):
            conf2.append('Medium')
        if(change2[i] > ranges[8][0]):
            conf2.append('High')
            high3 += 1   # there is increment in high3 when high is obtained on Ceramics & Granite

for i in range(0, 89):                                                  # this for loop deals with change % on fourth day
    if(industry[i] == 'Finance - General'):
        if(change3[i] < ranges[0][0]):
            conf3.append('Low')
            low1 += 1   # there is increment in low1 when low is obtained on Finance
        if(change3[i] >= ranges[1][0] and change3[i] <= ranges[1][1]):
            conf3.append('Medium')
        if(change3[i] > ranges[2][0]):
            conf3.append('High')
            high1 += 1   # there is increment in high1 when high is obtained on Finance
    if(industry[i] == 'Auto Ancillaries'):
        if(change3[i] < ranges[3][0]):
            conf3.append('Low')
            low2 += 1   # there is increment in low2 when low is obtained on Auto Ancillaries
        if(change3[i] >= ranges[4][0] and change3[i] <= (10 * ranges[4][1])):
            conf3.append('Medium')
        if(change3[i] > (10 * ranges[5][0])):
            conf3.append('High')
            high2 += 1   # there is increment in high2 when high is obtained on Auto Ancillaries
    if(industry[i] == 'Ceramics & Granite'):
        if(change3[i] < ranges[6][0]):
            conf3.append('Low')
            low3 += 1   # there is increment in low3 when low is obtained on Ceramics & Granite
        if(change3[i] >= ranges[7][0] and change3[i] <= ranges[7][1]):
            conf3.append('Medium')
        if(change3[i] > ranges[8][0]):
            conf3.append('High')
            high3 += 1   # there is increment in high3 when high is obtained on Ceramics & Granite

for i in range(0, 89):                                                  # this for loop deals with change % on fivth day
    if(industry[i] == 'Finance - General'):
        if(change4[i] < ranges[0][0]):
            conf4.append('Low')
            low1 += 1   # there is increment in low1 when low is obtained on Finance
        if(change4[i] >= ranges[1][0] and change4[i] <= ranges[1][1]):
            conf4.append('Medium')
        if(change4[i] > ranges[2][0]):
            conf4.append('High')
            high1 += 1   # there is increment in high1 when high is obtained on Finance
    if(industry[i] == 'Auto Ancillaries'):
        if(change4[i] < ranges[3][0]):
            conf4.append('Low')
            low2 += 1   # there is increment in low2 when low is obtained on Auto Ancillaries
        if(change4[i] >= ranges[4][0] and change4[i] <= (10 * ranges[4][1])):
            conf4.append('Medium')
        if(change4[i] > (10 * ranges[5][0])):
            conf4.append('High')
            high2 += 1   # there is increment in high2 when high is obtained on Auto Ancillaries
    if(industry[i] == 'Ceramics & Granite'):
        if(change4[i] < ranges[6][0]):
            conf4.append('Low')
            low3 += 1   # there is increment in low3 when low is obtained on Ceramics & Granite
        if(change4[i] >= ranges[7][0] and change4[i] <= ranges[7][1]):
            conf4.append('Medium')
        if(change4[i] > ranges[8][0]):
            conf4.append('High')
            high3 += 1   # there is increment in high3 when high is obtained on Ceramics & Granite


def maxi(a, b, c):   # this function returns the maximum of the three arguments
    max = 0
    if(a > b):
        max = a
    if(b >= a):
        max = b
    if(max >= c):
        max = max
    if(max < c):
        max = c
    return max


# insert data into Ticker table
for i in range(0, 89):
    cur.execute("""INSERT INTO Ticker VALUES('20-05-2022', ?, ?, 'NOT_LISTED', ?, 'NOT_LISTED', 'Listed new');""", [company_name[i], industry[i], day1_val[i]])
for i in range(0, 89):
    cur.execute("""INSERT INTO Ticker VALUES('21-05-2022', ?, ?, ?, ?, ?, ?);""", [company_name[i], industry[i], day1_val[i], day2_val[i], change1[i], conf1[i]])
for i in range(0, 89):
    cur.execute("""INSERT INTO Ticker VALUES('22-05-2022', ?, ?, ?, ?, ?, ?);""", [company_name[i], industry[i], day2_val[i], day3_val[i], change2[i], conf2[i]])
for i in range(0, 89):
    cur.execute("""INSERT INTO Ticker VALUES('23-05-2022', ?, ?, ?, ?, ?, ?);""", [company_name[i], industry[i], day3_val[i], day4_val[i], change3[i], conf3[i]])
for i in range(0, 89):
    cur.execute("""INSERT INTO Ticker VALUES('24-05-2022', ?, ?, ?, ?, ?, ?);""", [company_name[i], industry[i], day4_val[i], day5_val[i], change4[i], conf4[i]])

# create a table named Metrics
cur.execute("""CREATE TABLE Metrics (
    KPIs TEXT,
    Metrics TEXT
    )""")

max_val = maxi(high1, high2, high3)    # gives the max value of the three arguments
if(max_val == high1):
    b_industry = 'Finance - General'   # if first argument is max the industry is finance
if(max_val == high2):
    b_industry = 'Auto Ancillaries'    # if second argument is max the industry is auto ancillaries
if(max_val == high3):
    b_industry = 'Ceramics & Granite'  # if third argument is max the industry id ceramics and granite

min_val = maxi(low1, low2, low3)       # gives the max value of the three arguments
if(min_val == low1):
    w_industry = 'Finance - General'   # if first argument is max the industry is finance
if(min_val == low2):
    w_industry = 'Auto Ancillaries'    # if second argument is max the industry is auto ancillaries
if(min_val == low3):
    w_industry = 'Ceramics & Granite'  # if third argument is max the industry id ceramics and granite
loss = min(change4)                         # min function returns the minimum value of the list
gain = max(change4)                         # max function returns the maximum value of the list
b_company_index = change4.index(gain)       # obtaining the index of maximum value
w_company_index = change4.index(loss)       # obtaining the index of minimim value
b_company = company_name[b_company_index]   # based on the index obtained we get the best company
w_company = company_name[w_company_index]   # based on the index obtained we get the worst company
# inserting data into Metrics table
cur.execute("""INSERT INTO Metrics VALUES('Best listed Industry', ?)""", [b_industry])
cur.execute("""INSERT INTO Metrics VALUES('Best Company', ?)""", [b_company])
cur.execute("""INSERT INTO Metrics VALUES('Gain %', ?)""", [gain])
cur.execute("""INSERT INTO Metrics VALUES('Worst listed Industry', ?)""", [w_industry])
cur.execute("""INSERT INTO Metrics VALUES('Worst Company', ?)""", [w_company])
cur.execute("""INSERT INTO Metrics VALUES('Loss %', ?)""", [loss])

conn.commit()
for data in cur:
    print(data)
conn.close()
