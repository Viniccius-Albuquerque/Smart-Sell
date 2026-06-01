def validar_numero_positivo(valor, tipo="int"):
    """Valida se o número é positivo"""
    try:
        if tipo == "int":
            num = int(valor)
        else:
            num = float(valor)
        
        if num < 0:
            return None, "Valor não pode ser negativo!"
        return num, None
    except ValueError:
        return None, f"Digite um número {'inteiro' if tipo == 'int' else 'válido'}!"

def validar_preco(preco):
    """Valida preço do produto"""
    try:
        preco = float(preco)
        if preco <= 0:
            return None, "Preço deve ser maior que zero!"
        return preco, None
    except ValueError:
        return None, "Digite um preço válido!"

def validar_quantidade(quantidade):
    """Valida quantidade do produto"""
    try:
        quantidade = int(quantidade)
        if quantidade <= 0:
            return None, "Quantidade deve ser maior que zero!"
        return quantidade, None
    except ValueError:
        return None, "Digite uma quantidade válida!"

def validar_desconto(desconto):
    """Valida desconto (0-100)"""
    try:
        desconto = float(desconto)
        if desconto < 0 or desconto > 100:
            return None, "Desconto deve estar entre 0 e 100%!"
        return desconto, None
    except ValueError:
        return None, "Digite um desconto válido!"