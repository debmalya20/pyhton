dic={
    "deb":"human",
    "age": 20
}
print(dic)
print(dic.get("deb"))#this will give error 

print(dic["deb"])#this will give null if the name dos not exist
print(dic.keys())#we can acess all keys
print(dic.values())