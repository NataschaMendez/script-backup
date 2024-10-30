pergunta = str(input("deseja calcular um numero? ").strip().lower())
while (pergunta != "não") and (pergunta != "nao"):
    if pergunta == "sim":
        while True:
            try:
                numero1 = int(input("digite o primeiro numero: ").strip())
                numero2 = int(input("digite outro numero: ").strip())
                if numero1 > 0 and numero2 > 0:
                    break
                else:
                    print ("os numeros precisam ser maiores que 0 ")
            except ValueError:
                print ("algo deu errado, voce precisa digitar dois numeros inteiros!")

        resultado = numero1 * numero2
        print (f"O resultado da multiplicação dos numeros é: {resultado}")

    else:
        print("Voce precisa digitar sim ou não!")
    
    print(100 * "-")
    pergunta = str(input("deseja calcular um numero? ").strip().lower())

print("Programa finalizado!")                               
