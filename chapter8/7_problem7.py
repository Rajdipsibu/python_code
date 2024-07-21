# def remover(l,word):
#     l.remove(word)
#     return l
# l=["raju","saju","kaju","ju"]
# print(remover(l,"ju"))

def remover(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
    
l=["raju","saju","kaju","ju"]
print(remover(l,"ju"))