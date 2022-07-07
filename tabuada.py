#Marcos de Aguiar Sampaio, 1°B Noturno;
#RGM: 29792088 
m = int(input("Escolha o número da tabuada: \n"))
a = int(input("Escolha o número de início: \n"))
s = int(input("Escolha o número do fim da tabuada: \n"))
print('-' *18)
print('tabuada de {}:'.format(m))
print('-' *18)
while(a <= s):
    print('{0} X {1} = {2}'.format(a, m, (a * m)))
    a = a + 1
print('-' *18)
