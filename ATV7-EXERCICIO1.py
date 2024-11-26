c = 0
soma_peso = 0
lista_altura = 0
lista_peso = 0



while True:
    codigo = str(input('Informe seu codigo'))
    

    
    if codigo == '0':
        media_peso = soma_peso / c
        media_altura = soma_altura / c

        print(f'A media de peso é {media_peso} \nA media de altura é {media_altura}')    
        break

    else:
        altura = float(input('Informe sua altura'))
    
        peso = float(input('Informe sua peso'))


        c +=1



  

