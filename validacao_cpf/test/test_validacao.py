import unittest
from app.validacao import validar_cpf

class TestValidarCPF(unittest.TestCase):

    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("529.982.247-25"))
        self.assertTrue(validar_cpf("03723044806"))
        self.assertTrue(validar_cpf("708.251.780-30"))

    def test_cpf_invalido_formato(self):
        self.assertFalse(validar_cpf("1234567890"))  
        self.assertFalse(validar_cpf("123.456.789"))   
        self.assertFalse(validar_cpf("abc.def.ghi-jk")) 

    def test_cpf_invalido_digitos(self):
        self.assertFalse(validar_cpf("111.111.111-11")) 
        self.assertFalse(validar_cpf("12345678910")) 
        self.assertFalse(validar_cpf("00000000000"))

    def test_cpf_com_zeros_a_esquerda(self):
        self.assertFalse(validar_cpf("000.000.000-00"))  
        self.assertTrue(validar_cpf("012.345.678-90"))

    def test_cpf_com_espacos(self):
        self.assertTrue(validar_cpf(" 529.982.247-25 "))
        self.assertFalse(validar_cpf(" 111.111.111-11 "))

    def test_cpf_string_vazia(self):
        self.assertFalse(validar_cpf(""))

    def test_cpf_none(self):
        self.assertFalse(validar_cpf(None))

    def test_cpf_tipo_errado(self):
        self.assertFalse(validar_cpf(12345678909))  
        self.assertFalse(validar_cpf(["123.456.789-09"]))  

    def test_cpf_com_caracteres_especiais(self):
        self.assertFalse(validar_cpf("529.982@247*25"))

if __name__ == '__main__':
    unittest.main()
