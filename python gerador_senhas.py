import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senhas Seguras ===")
    tamanho = int(input("Digite o tamanho da senha (mínimo 8): "))
    
    if tamanho < 8:
        print("⚠️ A senha deve ter pelo menos 8 caracteres!")
    else:
        senha = gerar_senha(tamanho)
        print(f"Sua senha gerada é: {senha}")

if __name__ == "__main__":
    main()
import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senhas Seguras ===")
    tamanho = int(input("Digite o tamanho da senha (mínimo 8): "))
    
    if tamanho < 8:
        print("⚠️ A senha deve ter pelo menos 8 caracteres!")
    else:
        senha = gerar_senha(tamanho)
        print(f"Sua senha gerada é: {senha}")

if __name__ == "__main__":
    main()
