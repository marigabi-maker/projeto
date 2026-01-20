def gerar_mensagem(usuario):
    nome = usuario["nome"]
    interesse = usuario["interesse"]

    mensagem = (
        f"Olá {nome}! 👋\n"
        f"Percebemos que você se interessa por {interesse}. "
        "Temos novidades que combinam com você!"
    )

    return mensagem
