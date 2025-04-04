import unittest
from app.validacao import validar_cpf

class TestValidarCPF(unittest.TestCase):
    
    def test_cpf_valido(self):
        print("✔ Testando CPFs válidos")
        # Esses CPFs são válidos segundo o algoritmo de verificação
        self.assertTrue(validar_cpf("529.982.247-25"))
        self.assertTrue(validar_cpf("153.400.958-70"))
        self.assertTrue(validar_cpf("862.883.667-57"))

    def test_cpf_invalido_formato(self):
        print("✔ Testando CPFs com formato inválido")
        # CPFs com quantidade errada de dígitos ou letras
        self.assertFalse(validar_cpf("1234567890"))      # Apenas 10 dígitos
        self.assertFalse(validar_cpf("123.456.789"))     # Incompleto
        self.assertFalse(validar_cpf("abc.def.ghi-jk"))  # Letras

    def test_cpf_invalido_digitos(self):
        print("✔ Testando CPFs com dígitos inválidos")
        # CPFs com todos os dígitos repetidos ou que não passam a validação
        self.assertFalse(validar_cpf("111.111.111-11"))
        self.assertFalse(validar_cpf("00000000000"))
        self.assertFalse(validar_cpf("708.251.780-30"))  # Esse parece válido, mas não é

    def test_cpf_com_zeros_a_esquerda(self):
        print("✔ Testando CPF com zeros à esquerda")
        # CPFs iniciando com zero podem ser válidos
        self.assertTrue(validar_cpf("012.345.678-90"))  # Válido de acordo com o algoritmo

    def test_cpf_string_vazia(self):
        print("✔ Testando CPF como string vazia")
        self.assertFalse(validar_cpf(""))

    def test_cpf_none(self):
        print("✔ Testando CPF como None")
        self.assertFalse(validar_cpf(None))

    def test_cpf_tipo_errado(self):
        print("✔ Testando CPF com tipos inválidos")
        self.assertFalse(validar_cpf(12345678909))  # Inteiro
        self.assertFalse(validar_cpf(['123.456.789-09']))  # Lista

    def test_cpf_com_espacos(self):
        print("✔ Testando CPF com espaços extras")
        self.assertTrue(validar_cpf(" 529.982.247-25 "))
        self.assertFalse(validar_cpf("   "))

    def test_cpf_com_caracteres_especiais(self):
        print("✔ Testando CPF com caracteres especiais")
        self.assertFalse(validar_cpf("529.982@247*25"))

if __name__ == '__main__':
    print("🔍 Iniciando testes de validação de CPF...\n")
    unittest.main()
