my_set = {"January", "February", "March"}

for month in my_set:
    print(month)

my_set.add("April")

print(len(my_set))
print(type(my_set))


print("hello".capitalize())

# creating a set using the set() constructor
new_set = set(("apple", "mango", "pineapple"))
for fruit in new_set:
    print(fruit)