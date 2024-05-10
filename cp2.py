import hashlib

alfabeto_ordenado = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ,.!?')

def gerar_rotor_refletor(chave):
    hash_chave = hashlib.sha256(chave.encode()).hexdigest()
    indices = list(range(len(alfabeto_ordenado)))
    # Embaralhar com base no hash da chave
    indices.sort(key=lambda x: (hash_chave[x % len(hash_chave)]))
    rotor = {alfabeto_ordenado[i]: alfabeto_ordenado[indices[i]] for i in range(len(alfabeto_ordenado))}
    # Gerar refletor como inversão do rotor
    refletor = {v: k for k, v in rotor.items()}
    return rotor, refletor

def cifrar_palavra(palavra, chave):
    rotor, refletor = gerar_rotor_refletor(chave)
    palavra_cifrada = ''
    for i, caracter in enumerate(palavra):
        if caracter in alfabeto_ordenado:
            indice = alfabeto_ordenado.index(caracter)
            # Saltos não lineares usando fórmula quadrática
            salto = (indice + i**2 + 1) % len(alfabeto_ordenado)
            caracter_rotor = alfabeto_ordenado[salto]
            caracter_refletor = refletor.get(caracter_rotor, caracter_rotor)
            palavra_cifrada += caracter_refletor
        else:
            palavra_cifrada += caracter
    return palavra_cifrada

def descriptografar_palavra(palavra_cifrada, chave):
    rotor, refletor = gerar_rotor_refletor(chave)
    refletor_inverso = {v: k for k, v in refletor.items()}
    palavra_descriptografada = ''
    for i, caracter in enumerate(palavra_cifrada):
        if caracter in alfabeto_ordenado:
            caracter_rotor = refletor_inverso[caracter]
            indice_rotor = alfabeto_ordenado.index(caracter_rotor)
            # Reverter os saltos não lineares
            indice_original = (indice_rotor - i**2 - 1) % len(alfabeto_ordenado)
            caracter_original = alfabeto_ordenado[indice_original]
            palavra_descriptografada += caracter_original
        else:
            palavra_descriptografada += caracter
    return palavra_descriptografada


chave_usuario = input("Digite a chave para criptografia/descriptografia: ")
palavra_usuario = input("Digite a palavra ou frase para criptografar: ")
palavra_cifrada = cifrar_palavra(palavra_usuario, chave_usuario)
palavra_descifrada = descriptografar_palavra(palavra_cifrada, chave_usuario)


print(f'Palavra original: {palavra_usuario}')
print(f'Palavra cifrada: {palavra_cifrada}')
print(f'Palavra descriptografada: {palavra_descifrada}')
