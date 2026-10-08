'''
==============================
      SISTEMA DE ACESSO
==============================

Usuário: Gabriel
Senha: ****

❌ Senha incorreta!
Tentativas restantes: 2

Senha: ****

❌ Senha incorreta!
Tentativas restantes: 1

Senha: ****

✅ Login realizado com sucesso!
Bem-vindo, Gabriel!

'''
user = 'Gabriel'
password = 1234
tentativas = 1

usuario = input('Digite seu usuario: ')
senha = int(input('Digite a sua senha: '))

while senha != password and tentativas <3:
        print('A sua senha esta incorreta! Tente novamente.')
        
        senha = input('Digite a sua senha novamente: ')
        
        tentativas += 1

if senha == password:
    print('Seu login foi efetuado com sucesso!')
else:
    print('Suas tentativas foram excedidas.')