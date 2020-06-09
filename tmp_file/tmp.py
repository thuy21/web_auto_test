import pymysql

conn = pymysql.connect(host='192.168.137.2', user='lecentMysql', passwd="lecentMysql#1234", db='lecent_prison_fund_sys')
db = conn.cursor()
code = []
name = []

with open('code.txt') as f:
    while True:
        res = f.readline()
        if len(res) == 0:
            break
        code.append(res)

with open('name.txt') as f2:
    while True:
        res2 = f2.readline()
        if len(res2) == 0:
            break
        name.append(res2)

res = []
for i in range(0, len(code)):

    db.execute("select * from treat_level_transfer where CreateTime like '%2020-05-27%' and PrisonerCode='"+code[i]+"' and ToTreatLevelName != '"+name[i]+"' ".format())
    results = db.fetchall()
    for items in results:
        res.append(items[0])

with open('res.txt', 'w+') as f:
    f.writelines()
