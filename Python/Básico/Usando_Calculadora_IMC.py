from Geral import confirmou, cls
from Calculadora_IMC import toString

while True:
    paciente = inptut("Digite o nome do paciente: ")
    if paciente.upper() == "FIM":
        break

    print()
    pc = float(input("Digite o peso do paciente (em kg):...... "))
    alt = float(input("Digite a altura do paciente (em metros): "))
    print()

    if confirmou("Deseja calcular o IMC para este paciente? (s/n): "):
        toString(paciente, pc, alt)

    print()
