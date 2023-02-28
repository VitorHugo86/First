import string
import secrets

def generate_password(length, use_uppercase=False, use_special_chars=False, use_numbers=False):
    """Função para gerar senhas aleatórias"""
    if length <= 0:
        print("O tamanho da senha deve ser maior que zero.")
        return ""
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_special_chars:
        chars += string.punctuation
    if use_numbers:
        chars += string.digits
    password = ''.join(secrets.choice(chars) for i in range(length))
    return password

def generate_passwords(num_passwords, length, use_uppercase=False, use_special_chars=False, use_numbers=False):
    """Função para gerar várias senhas aleatórias"""
    if num_passwords <= 0:
        print("O número de senhas deve ser maior que zero.")
        return
    for i in range(num_passwords):
        password = generate_password(length, use_uppercase, use_special_chars, use_numbers)
        if password:
            complexity = "com letras minúsculas"
            if use_uppercase:
                complexity += ", letras maiúsculas"
            if use_special_chars:
                complexity += ", caracteres especiais"
            if use_numbers:
                complexity += ", números"
            name = f"Senha {i+1} ({length} caracteres, {complexity})"
            print(f"{name}: {password}")
        else:
            print("Erro ao gerar a senha.")

# Exemplo de uso
num_passwords = int(input("Digite o número de senhas que deseja gerar: "))
length = int(input("Digite o tamanho da(s) senha(s): "))
use_uppercase = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
use_special_chars = input("Incluir caracteres especiais? (s/n): ").lower() == 's'
use_numbers = input("Incluir números? (s/n): ").lower() == 's'

generate_passwords(num_passwords, length, use_uppercase, use_special_chars, use_numbers)
