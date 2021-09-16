lst=[1,2,3,4,5,6,7,8,9,11,12]
def linear_search(lst):
    element=int(input("enter the element to search"))
    fla=0
    for i in lst:
        if i==element:
            fla=1
            break
    if fla==0:
        print("not found")

    else:
        print("found")

linear_search(lst)

