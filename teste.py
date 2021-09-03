nome = str(input("Digite o nome do arquivo, lembrando de colocar .txt no final: "))
conteudo = str(input("Digite o conteúdo do documento: "))
with open(f"./files/{nome}", "w") as arquivo:
    arquivo.write(conteudo)