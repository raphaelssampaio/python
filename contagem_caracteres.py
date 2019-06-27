def contar_caracteres(s):

    caracteres_ordenados = sorted(s)

    caractere_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caractere_anterior:
            contagem += 1
        else:
            print (f'{caractere_anterior}: {contagem}')
            caractere_anterior = caracter
            contagem = 1

    print (f'{caractere_anterior}: {contagem}')

contar_caracteres('raphael')