# # set
#
# a={3,4,5.6,5,6,"hel"}
# # a.add(2)
# # a.add(13)
# # a.add(4.8)
# # a.add("helo")
# # a.add(True)
# # a.add(False)
# print("set =",a)
# # print(type(a))
# for i in a:
#     print(i)

s=set()
lmt=int(input("enter the limit"))
for i in range(lmt):
    elements=int(input("enter the element"))
    s.add(elements)
print(s)