mydict = {("Berkin","Koca") : [100,80,60], ("İpek","iscelebi"):[100,100,90]}
mydict["Kobra"] = {45}

dictondict = {"berkin" : {"koca": [12,13,14]}}
print (mydict)



for key,value in mydict.items():
    if(key[0] == "Berkin"):
        value[2] += 5
        print(value)



# print(list(mydict.values())[0][1])
# print(list(mydict.keys())[0][1])
