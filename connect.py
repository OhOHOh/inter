import telnetlib, requests

print('start')

try:
    r = requests.get('http://10.0.169.162:8000/api/v1/hello')
except:
    print('连接失败')
else:
    if r.status_code == requests.codes.ok:
        print('连接成功')
        print(r.text)




