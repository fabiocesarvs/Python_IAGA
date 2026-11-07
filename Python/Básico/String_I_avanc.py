def matriz_String(s):
    n = len(s)
    for i in range(n):
        print(f"linha{i}: | ", end="")
        for j in range(i+1):
            print(f"{s[j]}", end=" ")
        print(" |")

        for j in range(i+1):
            print(f"", end="")


# módulo principal (main)
s = input("Informe uma String?\n")

print()

matriz_String(s)


