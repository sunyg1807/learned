import json
date= {'name':'张三','age':25}
date1=json.dumps(date)###json.dumps将字典更改为json字符串(数据）
date2=json.loads(date1)###json.loads将json数据更改为字典
print(date1,type(date1))
print(date2,type(date2))