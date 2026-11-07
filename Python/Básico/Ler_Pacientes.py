import Calculadora_IMC
from Geral import cls, parada

cls()

#1. abre o arquivo de texto (r - read)
arquivo = open("pacientes.txt", "r")

#2. lê "todas" as linhas do arquivo de texto
linhas = arquivo.readlines()

for linha in linhas : #for each: recupera linha por linha
    partes = linha.split(";") #divide a linha em partes

    paciente = partes[0]
    pc = float(partes[1])
    alt = float(partes[2])

    print(Calculadora_IMC.toString(paciente, pc, alt))
    print()

#3. fecha o arquivo de texto
arquivo.close()
