import pymysql

db = pymysql.connect(host = 'localhost', user='root', passwd='dlsduqdl', db='capstone', charset='utf8')
cursor = db.cursor()

query = 'select Q_noun, BRDNO from QnA;'
cursor.execute(query)
result = cursor.fetchall()

for row in result:
	if row[0] != '':
		print(row[1])
		print(row[0])
db.close()