import telnetlib, requests, json

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

payload = {  # 注意顺序!
    'case': 'testCase',
    'branchName': 'testBranchName',

}
r = requests.get(url, params=payload)
print(r.url)


# url1 = 'http://127.0.0.1:8003/api/v1/makecase/'
# r = requests.get(url1)
# print(r.json())
# data = r.json()
# list = data['testcases']
# case_list = []
# print(list)
#
# # for item in list:
# #     print(item['name'])
# #     list.append(item['name'])
# # print(list.__len__())
#
# for item1 in list:
#     print(item1['name'])
#     #print(list[item1]['name'])
#     #case_list.append(list)
#
# #print(json.loads(data))
# print(data['meta']['total'])


# url2 = 'http://127.0.0.1:8003/api/v1/makebranchjson/'
# r = requests.get(url2)
#
# data = r.json()
# print(data)
# print(data['meta']['total'])
# print(data['branches'])

url3 = 'http://127.0.0.1:8003/api/v1/makebranchjson/'
r = requests.get(url3)

data = r.json()
print(data)

