import json
data=[
{"id":1,"fname":"Sachin","lname":"Tendulkar"},
{"id":2,"fname":"Saurav","lname":"Ganguly"},
{"id":3,"fname":"Rahul","lname":"Dravid"},
{"id":4,"fname":"Yuvraj","lname":"Singh"}
]
json.dump(data,open("data.json","w"))
