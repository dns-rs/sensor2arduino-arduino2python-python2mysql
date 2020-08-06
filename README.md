# ARDUINO UNO: light_temp_hum_json.ino
# sensor2arduino
Arduino UNO collects DHT11 and Photoresistor values into JSON object 
# arduino2python
The arduino forwards the JSON object to the serial port.

# RASPBERRY PI: serial2db.py
# python2mysql
The python script decrypts the JSON object and sends the data to mysql database alongside with a timestamp.
