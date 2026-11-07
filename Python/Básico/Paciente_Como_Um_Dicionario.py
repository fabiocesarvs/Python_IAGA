from Calculadora_IMC import toString
from Geral import cls, parada

# declarando o dicionário de dados do paciente

meu_Paciente = {"paciente": "",   # nome do paciente
                "pc": 0.0,        # peso corporal em kgs
                "alt": 0.0 }      # altura em metros

while True:
    cls()
    meu_Paciente["paciente"] = input("Informe o nome do paciente......: ")
    if (meu_Paciente["paciente"].upper() == "FIM"):
        break

    print()
    meu_Paciente["pc"] = float(input("Informe o peso corporal (em kgs): "))
    meu_Paciente["alt"] = float(input("Informe a altura (em metros)...: "))

    print()
    print(toString(meu_Paciente["paciente"], meu_Paciente["pc"], meu_Paciente["alt"]))
    print()


