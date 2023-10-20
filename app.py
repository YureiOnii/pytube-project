from pytube import YouTube
from os import system as cmd
from time import sleep as esperar

while True:
    try:
        print(100 * "=")
        print("Bem-vindo ao instalador de video")
        print(100 * "=")
        esperar(1)
        cmd ("cls")
        
        yt = YouTube(input("Digite a url que deseja fazer o download: "))
        print(100 * "=")
        esperar(1)

        print(yt.title)
        desc = yt.description

        if yt.description:
            print(desc)

        else:
            print("Descrição inválida!!")
        
        print(100 * "=")
        escolha = input("1-[Continuar]\n2-[Sair]\n")
        print(100 * "=")

        if escolha == "1":
            input("Deseja fazer o download do video?")

        elif escolha == "2":
            break
        
        else:
            print("Digite uma opção válida!!")

    except KeyboardInterrupt:
        print("Digite um comando válido!")
        esperar(1)
        cmd("cls")
        break