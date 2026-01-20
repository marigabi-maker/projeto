from dados import usuarios
from ia import gerar_mensagem

def main():
    print("=== Gerador de Mensagens com IA (Simulada) ===\n")

    for usuario in usuarios:
        mensagem = gerar_mensagem(usuario)
        print(mensagem)
        print("-" * 40)

if __name__ == "__main__":
    main()
