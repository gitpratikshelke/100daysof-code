#day 33
#dictionary-dictionary is set of key_value pair
dic={1:"pratik",2:"object" ,3:"sid"}
print(dic[1])


info={'name':'pratik','age':19,'eligible':True}
print(info)
print(info['name'])
print(info.get('eligible'))
print(info.keys)#for all keys


for key in info.keys():
    print(info[key])