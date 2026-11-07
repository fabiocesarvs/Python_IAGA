from os import system
from time import sleep

def cls():
    system("cls") # limpa a tela do terminal

def delay(tmp): # tmp em segundos
    sleep(tmp) # pausa a execução do programa por tmp segundos

def parada():
    print("\nPressione <Enter> para continuar...")
    input()

def confirmou (rotulo):
    op = input(rotulo)
    if ((op == "s") or (op == "S")):
        return True
    else:
        return False

def linha(tipo="-", tam=20):
    result = ""
    for i in range(tam):
        result = result + tipo

    return(result)
