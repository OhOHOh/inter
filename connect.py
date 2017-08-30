import telnetlib, requests


url = 'http://10.0.169.155:8003'
if url[-1] != '/':
    url = url + '/'
print(url)
print(url[0] == 'h')


print('start')

# try:
#     r = requests.get('http://10.0.169.155:8003')
# except:
#     print('连接失败')
# else:
#     if r.status_code == requests.codes.ok:
#         print('连接成功')
#         print(r.text)
#     print('什么情况')
#     print(r.status_code)




site = "<PreparedRequest [GET]>"
if site.find('GET') != -1:
    print('find!')
if 'GET' in site:
    print('find2!')

x = 50
def fun():
    global x
    print(x)
fun()
