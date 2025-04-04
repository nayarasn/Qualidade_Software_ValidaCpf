# ✅ Validador de CPF com Interface Gráfica e Testes Unitários

Este projeto é um **mini sistema de validação de CPF brasileiro** com **interface gráfica usando Tkinter**. Ele também possui uma **série de testes unitários** para garantir a correta validação dos dados.

---

## 🧠 O que foi desenvolvido?

- Uma **função de validação de CPF** em Python que segue as regras do algoritmo oficial.
- Uma **interface gráfica (GUI)** feita com Tkinter:
  - Permite digitar o CPF.
  - Mostra uma **saudação personalizada** no topo: _"Bom dia, Boa tarde, Boa noite meu povo"_.
  - Exibe uma mensagem informando se o CPF é válido ou inválido.
- **Testes unitários** com `unittest` para cobrir diferentes cenários:
  - CPFs válidos.
  - CPFs inválidos por dígito, formato ou tipo.
  - CPFs com caracteres especiais, espaços, etc.
- Geração de relatório de testes em HTML com `pytest-html`.

---

## 🖥️ Como executar o sistema

1. Clone o repositório ou baixe os arquivos.
2. Execute o script principal:

```bash
python app/main.py
```

> Isso abrirá a janela da interface gráfica.

---

## 🧪 Como rodar os testes

### 1. Usando `unittest` (saída no terminal):

```bash
python -m test.test_validacao
```

### 2. Usando `pytest` com relatório HTML (opcional):

Instale as dependências:

```bash
pip install pytest pytest-html
```

Gere o relatório:

```bash
pytest test/ --html=relatorio_cpf.html
```

---

## 🧬 Sobre os testes unitários

Os testes estão no arquivo `test/test_validacao.py` e cobrem os seguintes cenários:

### ✅ Testes que devem passar:
- CPF válido (ex: `153.509.460-56`)
- CPF com espaços e zeros à esquerda
- CPF com formato incorreto
- CPF como string vazia, None ou tipo incorreto

### ❌ Testes que devem falhar (de propósito, para validação):
- CPF com caracteres especiais inválidos (`@`, `*`, etc)
- CPF com dígitos inválidos (`111.111.111-11`, etc)
- CPF incorreto mas com aparência válida

Esses testes mostram **casos reais de sucesso e falha**, reforçando a importância da verificação completa.

---

## 📂 Estrutura do projeto

```
validacao_cpf/
├── app/
│   ├── main.py              # Interface gráfica com Tkinter
│   └── validacao.py         # Função para validar CPF
├── test/
│   └── test_validacao.py    # Testes unitários com unittest
├── relatorio_cpf.html       # (gerado) Relatório dos testes em HTML
└── .gitignore               # Arquivos ignorados pelo Git
```

---

## 🤓 Importância dos testes unitários

Testes unitários são **essenciais** para garantir que as funcionalidades funcionem como o esperado em diferentes condições. Eles ajudam a:
- Evitar bugs antes que o sistema chegue ao usuário.
- Garantir que alterações futuras não quebrem funcionalidades existentes.
- Validar entradas críticas como CPF, que envolvem regras específicas.

---

## 💡 Tecnologias usadas

- Python 3.11
- Tkinter
- Unittest
- Pytest + Pytest-HTML

---

