import json

data1 = [{'branchName1': 'master', 'age': 16}, {'branchName2': 'develop', 'age': 20}]
data2 = [{
    'branchName': 'testBranchName1',
    'compileTimes': 100,
    'runTimes': 100,
    'lastCompile': '2020-10-1',
    'lastRun': '2020-10-3',
},
    {
        'branchName': 'develop',
        'compileTimes': 200,
        'runTimes': 200,
        'lastCompile': '2030-10-1',
        'lastRun': '2030-10-3',
    }]
data3 = json.dumps(data2)  #无法操作了
print(data2)
print(data2[0])
print(data2[0]['branchName'])
print(data3)
print(data3[0])
