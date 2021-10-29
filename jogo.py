def atualiza_palavra(palavra: str, letra: str, indices: list):
    letra = letra.upper()
    palavra = list(palavra.upper())

    for index in indices:
        palavra[index] = letra

    palavra = "".join(palavra)

    return palavra
