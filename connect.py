import telnetlib

print('start')

try:
    tn = telnetlib.Telnet('127.0.0.1',port='8000', timeout=20)
    # tn = telnetlib.Telnet('10.0.176.232', port='80', timeout=20)
except:
    print('connect fail')
else:
    print('connect success')

print('end')

