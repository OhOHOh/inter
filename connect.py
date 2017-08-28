import telnetlib, requests


url = 'http://10.0.169.155:8003'
if url[-1] != '/':
    url = url + '/'
print(url)
print(url[0] == 'h')


print('start')

try:
    r = requests.get('http://10.0.169.155:8003')
except:
    print('连接失败')
else:
    if r.status_code == requests.codes.ok:
        print('连接成功')
        print(r.text)
    print('什么情况')
    print(r.status_code)


context = {
    'result': '1',
    'headers': r.headers,
    'status_code': r.status_code,
    'content': r.text,
    'request': r.request,
}
print(context['result'])
