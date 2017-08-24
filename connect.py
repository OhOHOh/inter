import telnetlib, requests

print('start')

try:
    r = requests.get('http://10.0.169.155:8003/')
except:
    print('连接失败')
else:
    if r.status_code == requests.codes.ok:
        print('连接成功')
        print(r.text)
    print('什么情况')
    print(r.status_code)




