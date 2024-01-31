"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'banana'
contagem = 0
palavra_adivinha = '*' * len(palavra_secreta)  # variável responsável por guardar a palavra com as letras adivinhadas

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print(palavra_adivinha)
    alternativa = input('Digite uma letra: ').lower()
    if len(alternativa) != 1 or not alternativa.isalpha():  # isalpha garante que seja alguma letra
        print('Digite apenas uma letra válida.')
        continue

    contagem += 1

    nova_adivinha = ''
    for letra_secreta, letra_adivinhada in zip(palavra_secreta, palavra_adivinha):
        # função zip percorre simultaneamente cada letra de cada variável proposta dentro dos ()
        if alternativa == letra_secreta:
            nova_adivinha += alternativa
        else:
            nova_adivinha += letra_adivinhada

    palavra_adivinha = nova_adivinha

    if palavra_adivinha == palavra_secreta:
        print(f'Parabéns! Você acertou a palavra {palavra_adivinha} em {contagem} tentativas')
        break
