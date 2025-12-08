my_list = ["January", "February", "March", "April", "May", "June", "July"]

print(my_list[0])

my_list.append("August")

print(my_list)
print(len(my_list))

#creating a list using the list() constructor
new_list = list(("CPU", "RAM", "Processor", "Storage"))

for component in new_list:
    print(component)