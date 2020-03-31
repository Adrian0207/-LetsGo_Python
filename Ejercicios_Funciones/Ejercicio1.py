'''
Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla 
(suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto). 
Además subraya el mensaje utilizando el carácter =.
'''


def EscribirCentrado(cad):
    print(" " * int(40 - (len(cad)/2)),cad)
    print(" " * int(40 - (len(cad)/2)),"=" * len(cad))

EscribirCentrado('Mi mama me mima, amo a mi mama')