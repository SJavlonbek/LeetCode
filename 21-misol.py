def mergeTwoLists( list1, list2) :
        list3=[]
        for n, ns in zip(list1, list2):
            list3.extend([n,ns])
        return list3

print(mergeTwoLists([1,2,4],[1,3,4]))