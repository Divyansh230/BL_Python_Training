def flatten(ls):
    flateened=[]

    for item in ls:
        if isinstance(item,list):
            flateened.extend(item)
        else:
            flateened.append(item)

    return flateened

ls=[[1,2,3],[4,5,6],[7,8,9]]
print(flatten(ls))