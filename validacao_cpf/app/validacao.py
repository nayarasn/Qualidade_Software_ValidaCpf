import re

def validar_cpf(cpf: str) -> bool:
    """
    Valida um CPF brasileiro.

    :param cpf: CPF como string (somente números ou no formato xxx.xxx.xxx-xx)
    :return: True se for válido, False caso contrário
    """
    cpf = re.sub(r'\D', '', cpf)  # Remove caracteres não numéricos

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False  # CPF inválido se não tiver 11 dígitos ou todos forem iguais

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])