import random

lista_id = []
def creador_lista(lista_id):
    for i in range(0,100):
        caracteres = 0
        id=""
        while caracteres <=10:
            id+=str(random.randint(0,9))
            caracteres +=1
        while id in lista_id:
            id+=str(random.randint(0,9))
        else:
            lista_id.append(id)
    return lista_id

creador_lista(lista_id)

# print(lista_id)


