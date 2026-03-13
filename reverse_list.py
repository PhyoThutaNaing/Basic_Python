"""
item = ["clothes", "shoes", "perfume"]
gender = ["men", "men", "men"]
price = ["starting from 300rs", "starting from 500rs", "starting from 400rs"]

item1 = ["clothes", "shoes", "perfume"]
gender1 = ["women", "women", "women"]
price1 = ["starting from 10000rs", "starting from 99000rs", "starting from 50000rs"]


for item,gender,price,item1,gender1,price1 in zip(item, gender, price, item1,gender1,price1):
    print(item, "for", gender, price, ".")
    print(item1, "for", gender1, price1, ".")
    

print(''' "She said,' "She will go to picnic" ''')

print('\'She said\' , \'She will go to picnic\'')

"""

print("{},{},{}".format("clothes", "shoes", "perfume"))

print("{2},{0},{1}".format("clothes", "shoes", "perfume"))


print("{c},{b},{a}".format(a = "clothes", b = "shoes", c ="perfume"))
