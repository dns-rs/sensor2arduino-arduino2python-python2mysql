import MySQLdb
import json
import serial
import random
from subprocess import PIPE, Popen, call
from datetime import datetime
import calendar

conn = MySQLdb.connect(host= "localhost",
                  user="your_username",
                  passwd="your_password",
                  db="your_database_name")
x = conn.cursor()

ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1)

def is_json(helperTemporary):
	try: 
		json_object = json.loads(helperTemporary)
	except ValueError as e:
		return False
	return True
		
# Database

while True:
	temporary = ser.readline()
	if is_json(temporary):
		jsonObj = json.loads(temporary)			
		try:   
			d = datetime.utcnow()
			unixtime = calendar.timegm(d.utctimetuple())
			print "--------------------------"
				   
			inputData = (unixtime, jsonObj["temperature"],jsonObj["humidity"],jsonObj["brightness"])
			x.execute("""INSERT INTO your_table_name SET datum=%s, temperature=%s, humidity=%s, feny=%s""",inputData)
			conn.commit()
			print inputData
			   
			print "--------------------------"
		except:
			#conn.rollback()
			print ("That didn't work")
