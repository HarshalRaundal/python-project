import json

error_data = []
format = ['date-time: ', 'filename: ','logger: ', 'Level: ', 'message: ']
with open('errorlog.log') as f:
    for line in f:
        content = line.split(' , ')
        temp = {}

        for i, val in enumerate(content):
            temp[format[i]] = val
            # print(i,"  ",val)
        error_data.append(temp)


filename = 'errorlog.json'

with open(filename, 'w') as f:
    json_data = json.dumps(error_data)
    json.dump(error_data, f, indent=1)




