def inverter_string(string):
    invertida = ""
    for i in range(len(dtring)-1, -1, -1):
        invertida += string[i]
    return invertida

def main():
    palavra = input("Digite uma palavra: ")
    print(f"A palavra invertida é: {inverter_string(palavra)}")

if __name__ == "__main__":
    main()
    