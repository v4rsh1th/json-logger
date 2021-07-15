import json
import glob

filesList = glob.glob('./*.json')
Logs = []

for fileDir in filesList:
    print('Merging ' + fileDir + '...')
    file = open(fileDir)
    data = json.load(file)
    for log in data:
        Logs.append(log)
    file.close()

with open('combinedLogs.json', 'w') as f:
    json.dump(Logs, f)
