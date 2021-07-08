def fun(l):
    output = []
    dic = {}
    for i in l:
        word = " ".join(sorted(i))
        
        if (word not in dic):
            output.append(i)
            dic[word]=1
    
    return output

    
l = ["geeks","eekgs","code","edoc"]
print("Original array", l)
output = fun(l)
print("Reverse of array", output)


