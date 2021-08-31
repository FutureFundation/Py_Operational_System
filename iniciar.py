from games import jogo_da_velha
from time import sleep
from datetime import date
from apps import Notepad
import emoji
print("\033[1;32;40m Bem Vindo, esse é o Py_Operational_System, um sistema operacional totalmente desenvolvido em python.")
print(emoji.emojize(" Eu sou o criador, me chamo Daniel Matos :thumbs_up: :snake: :smile: ", use_aliases=True))
criação = '31/08/2021'
sleep(3)
while True:
    data_atual = (f'{date.today().day}/{date.today().month}/{date.today().year}')
    try:
        comando = str(input("Digite o comando(help para ajuda): "))
    except ValueError:
        print("Você deve digitar uma string")
        continue

    if comando == 'exit':
        break
    if comando == 'help':
        print("""Comandos possíveis: 
            games
            exit
            data
            notepad""")
    elif comando == 'games':
        jogo_selecionado = str(input("""Jogos disponíveis:
            jogo da velha"""))
        if jogo_selecionado == 'jogo da velha':
            jogo_da_velha.velha_game()
    elif comando == 'data':
        print(data_atual)
    elif comando == 'notepad':
        print("Recomendamos salvar os dados na pasta files")
        Notepad.Notepad_start()
print(emoji.emojize('Adeus! :broken_heart:'))