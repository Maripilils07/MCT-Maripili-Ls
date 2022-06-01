#Hi,my birthday is:7 of March
print('Areas que puedo calcular:ciculo,trapezoide y rombo')

print('Para trapezoide: ')
b1=int(input('Ingrese la medida de la base menor: '))
b2=int(input('Ingrese la medida de la base mayor: '))
alt=int(input('Ingrese la altura de la figura: '))
suma=(b1+b2)

print('El area de es esta figura es:',(suma*alt/2))
pi=3.1416
print('Para circulo:')
print('Ponga cero si no es la medida que corresponde: ')
print('Ponga su medida donde corresponda:')
r1=int(input('Ingrese el radio de la figura:'))
print('Sí es diametro:')
dia1=int(input('Ingrese la medida:'))
print('El radio de la figuar es el diametro dividido entre 2')
r=dia1/2
re=r1*r1
re1=pi*re
re2=pi*r
print('Su respuesta si puso diametro es: ',re2)
print('Su respuesta si puso radio: ',re1)
print('Para rombo:')
d1=int(input('Ingrese la medida de la diagonal mayor: '))
d2=int(input('Ingrese la medida de la diagonal menor: '))
resultado1=d1*d2
res2=resultado1/2
print('Su respuesta es: ',res2)