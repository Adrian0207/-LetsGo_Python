num = int(input('Ingrese un valor...'))

dic = {}
for i in range(1,num + 1):
    dic[i] = i ** 2

for clave, valor in dic.items():
    print(clave, '\t', valor)
