from datetime import date
from time import sleep
import emoji
import requests
from bs4 import BeautifulSoup as bs
from games.ping_pong import Game17
from apps import Notepad
from apps import calculadora
from apps import navegador
from games import jogo_da_velha
import pygame
from tkinter import *

import random # random.sample escolhe um dos valores de uma lista

root = Tk()

print("\033[1;32;40m Bem Vindo, esse é o Py_Operational_System, um sistema operacional totalmente desenvolvido em python.")
print(emoji.emojize(" Esse projeto foi desenvolvido pela future fundation :thumbs_up: :snake: :smile: ", use_aliases=True))
print("Antes de tudo lembre-se: com grandes poderes vem grandes responsabilidades.")
criação = '31/08/2021'
fazer = 'ping pong'
sleep(3)
while True:
    data_atual = (f'{date.today().day}/{date.today().month}/{date.today().year}')
    try:
        comando = str(input("Digite o comando(help para ajuda): ")).lower()
    except ValueError:
        print("Você deve digitar uma string")
        continue
    try:
        if comando == 'exit':
            break
        if comando == 'help':
            print("""Comandos possíveis: 
                games
                exit
                data
                notepad
                navegador
                relatar problema
                valor do bitcoin
                calculadora
                musicas
                star wars
                sortear
                criar txt
                ver txt""")
            continue
        elif comando == 'games':
            jogo_selecionado = str(input("""Jogos disponíveis:
                jogo da velha
                : """)).lower()
            if jogo_selecionado == 'jogo da velha':
                jogo_da_velha.velha_game()
        elif comando == 'data':
            print(data_atual)
        elif comando == 'notepad':
            print("Recomendamos salvar os dados na pasta files")
            Notepad.Notepad_start()
        elif comando == 'navegador':
            navegador.navegador_start()
        elif comando == 'relatar problema':
            print("e-mail: futurefundationbr@gmail.com")
            print("Qualquer crítica é muito bem vinda")
        elif comando == 'preço do bitcoin':
            url = 'https://www.bitcoinprice.com/'
            r = requests.get(url)
            soup = bs(r.content, "html.parser")
            price = soup.find("span", {"id": "price"})
            print("Bitcoin: ", price.text)  # print only the text
        elif comando == 'calculadora':
            calculadora.start_calculadora()
        elif comando == 'ping pong':
            Game17.start_ping_pong()
        elif comando == 'musicas':
            selecionada = str(input("""Músicas Disponíveis: 
                praise to the lord the almigthy
                just as i am
                    """)).lower()
            if 'praise to the lord' in selecionada:
                pygame.init()
                pygame.mixer.music.load('music/2001-01-0720-praise-to-the-lord-the-almighty-instrumental-192k-eng.mp3')
                pygame.mixer.music.play(0)
            if selecionada == 'just as i am':
                pygame.init()
                pygame.mixer.music.load('music/JustAsIAm.mp3')
                pygame.mixer.music.play(0)
        elif comando == "star wars":
            print("#Staréamelhorsaga")
            print("Que a força esteja com você, sempre!")
            imagem = PhotoImage(file="files/images/darth_Vader.png")

            lb = Label(root, image=imagem)

            lb.place(x=0, y=20)

            root.mainloop()
        elif comando == 'sortear':
            quantidade = int(input("Quantos valores você quer usar para o sortéio, o computador sorteará um deles: "))
            tipo = str(input("Digite se você quer sortear números(num) ou letras(letr): ")).lower()
            valores = []
            if tipo == 'letr':
                for c in quantidade:
                    valor = str(input("Digite a string: "))
                    valores.append(valor)
            else:
                for c in quantidade:
                    valor = int(input("Digite o número: "))
                    valores.append(valor)
            value = random.sample(valores)
            print(f"Valor sorteado: {value}")
        elif comando == "criar txt":
            nome = str(input("Digite o nome do arquivo, lembrando de colocar .txt no final: "))
            conteudo = str(input("Digite o conteúdo do documento: "))
            with open(f"./files/{nome}", "w") as arquivo:
                arquivo.write(conteudo)
            print("O arquivo só é salvo quando você encerra o programa, ele vai estar salvo na pasta files")
            break
        elif comando == 'ver txt':
            nome = str(input("Digite o nome do arquivo, lembrando de falar onde o arquivo está. exemplo: (./files/nome), o ./ representa a pasta atual: "))
            with open(f"{nome}", "r") as arquivo:
                print(arquivo.readlines())
        else:
            print("Confira o que você escreveu, ou digite help para ver os comandos possíveis")
            sleep(1)
    except Exception as e:
        print("Seu programa não funcionou porque: ", e)
print(emoji.emojize('Adeus! :broken_heart:'))
print("Remember: God is always faithful, God Bless you!")