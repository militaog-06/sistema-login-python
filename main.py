user = 'Gabriel'
password = '1234'
tentativas = 0

while tentativas <3:
    usuario = input('Digite seu usuario: ')
    senha = input('Digite a sua senha: ')

    if usuario == user and senha == password:
        print('Login realizado com sucesso!')
        break
    else:
        tentativas += 1
        print('Usuario ou senha incorretos!')

        if tentativas <3:
            print(f'Tentativas restantes: {3 - tentativas}')
        else:
            print('Seu acesso foi bloqueado! Tentativas excedidas.')
