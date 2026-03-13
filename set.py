"""
my_set = {1,2,3}

print(my_set)

my_set.add("Phyo Thuta Naing")
print(my_set)

my_set.update(["a,b,c"], {2.4, 5.7}, ['apple, banana'])

"""

x = {1,2,3,4}
y = {1,2, 'apple, banana'}
z = {1,2,3,4, "Phyo Thuta Naing"}

a = x ^ y

b = a ^ z

for x in "banana":
  print(x)
  
print(b)

print(type(b))

print(id(b))

