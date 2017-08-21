import telnetlib, requests

print('start')

try:
    tn = telnetlib.Telnet('127.0.0.1',port='8000', timeout=20)
    # tn = telnetlib.Telnet('10.0.176.232', port='80', timeout=20)
except:
    print('connect fail')
else:
    print('connect success')
print('end')

try:
    r = requests.get('http://127.0.0.1:8000')
except:
    print('连接失败')
else:
    if r.status_code == requests.codes.ok:
        print('连接成功')

