

clientes = {}

while True:
    codigo = str(input('Informe seu codigo'))
    

    
    if codigo == '0':
        print("\nResultados do Senso:")
        print(f"Mais alto: Código {mais_alto[0]}, Altura {mais_alto[1]['altura']}m")
        print(f"Mais baixo: Código {mais_baixo[0]}, Altura {mais_baixo[1]['altura']}m")
        print(f"Mais gordo: Código {mais_gordo[0]}, Peso {mais_gordo[1]['peso']}kg")
        print(f"Mais magro: Código {mais_magro[0]}, Peso {mais_magro[1]['peso']}kg")
        print(f"Média de altura: {media_altura:.2f}m")
        print(f"Média de peso: {media_peso:.2f}kg")
        break

    else:
        
        altura = float(input('Informe sua altura'))
        peso = float(input('Informe sua peso'))
        
        # Dentro do codigo tem o item altura e peso, que estao recebendo o valor das variaveis
        clientes[codigo] = {'Altura' : altura, 'Peso' : peso}


        # sum faz a soma de tudo, no caso soma os valores do dicionario cliente
        total_altura = sum(cliente['altura'] for cliente in clientes.values())
        total_peso = sum(cliente['peso'] for cliente in clientes.values())
        #len faz a contagem de itens dentro
        media_altura = total_altura / len(clientes)
        media_peso = total_peso / len(clientes)


        mais_alto = max(clientes.items(), key=lambda alt: alt[1]['altura'])
        mais_baixo = min(clientes.items(), key=lambda baix: baix[1]['altura'])
        mais_gordo = max(clientes.items(), key=lambda gord: gord[1]['peso'])
        mais_magro = min(clientes.items(), key=lambda mag: mag[1]['peso'])

  

