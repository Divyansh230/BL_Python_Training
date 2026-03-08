def transpose(lst):
    lst2 = []
    for i in range(len(lst)):
        temp=[]
        for j in range(len(lst[i])):
             temp.append(lst[j][i])
        lst2.append(temp)

    return lst2

ls=[[1,2,3],[4,5,6],[7,8,9]]
print(transpose(ls))

