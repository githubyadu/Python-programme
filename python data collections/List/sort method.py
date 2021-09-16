my_list=[11,12,777,889,654,-33,-44,-555,22,59,88]
new_list=[]
while my_list:
    min=my_list[0]
    for i in my_list:
        if i < min:
            min=i
    new_list.append(min)
    my_list.remove(min)
print(new_list)
print(my_list)