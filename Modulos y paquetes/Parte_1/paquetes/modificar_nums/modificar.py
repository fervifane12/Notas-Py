

lista=[]
lista_final=[]
final=[]
def modificar(nums):
    nums.sort(reverse=True)

    for i in nums:
        if nums.count(i)>1:
            ind=nums.index(i)
            nums.pop(ind)
    
    for a in nums:
        if a%2==0:
            lista_final.append(a)
    
    suma=sum(lista_final)
    lista_final.insert(0, suma)
    return "La lista modificada es: " + str(lista_final)
