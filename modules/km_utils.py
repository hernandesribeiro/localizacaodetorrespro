def encontrar_torres(km_alvo, km_list):
    """Retorna (torre anterior, torre posterior) com base no KM informado."""
    anterior = None
    posterior = None

    for i in range(len(km_list) - 1):
        if km_list[i] <= km_alvo <= km_list[i + 1]:
            anterior = i
            posterior = i + 1
            break

    return anterior, posterior
