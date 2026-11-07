from Geral import cls, parada

cls()
while True:
    nomeArquivo = input("Informe o nome do arquivo de texto (ou FIM para encerrar): \n"")
    if nomeArquivo.upper() == "FIM":
        break

    print()

    arquivo = open(nomeArquivo, "r" )
    linhas = arquivo.readlines()
    print("*** Conteúdo do arquivo de texto ***")
    for linha in linhas:
        print(linha, end="")
    arquivo.close()
