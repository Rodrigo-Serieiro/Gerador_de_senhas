import random
import time

min = 'abcdefghijklmnopqrstuvwxyy'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '[]{}()*#;/,-_%'


all = min + max + num + sybs


def gerador_senha(comprimento: int):
    return "".join(random.sample(all, comprimento))


def nova_senha(tamanho: int):
    return gerador_senha(tamanho)


def main():
    tamanho = -1
    while True:
        tamanho = int(input(f'Digite o tamanho da senha: '))
        if (tamanho >= 4 and tamanho <= 20):
            print('estamos gerando sua senha...')
            time.sleep(1)
            print(f'Sua senha é {nova_senha(tamanho)}')
            resposta = input('Gerar uma nova senha ? [s ou n]')
            if resposta.lower() == 'n':
                print('Até a próxima!')
                break
        else:
            print('Digite apenas números entre 04 e 20.')


main()
