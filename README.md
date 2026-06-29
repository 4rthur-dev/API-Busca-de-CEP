# 📮 Verificação de CEP

Aplicação desktop desenvolvida em Python com interface gráfica (PyQt5) para consulta de endereços a partir do CEP, utilizando a API pública [ViaCEP](https://viacep.com.br/).

---

## 🖥️ Demonstração

A interface permite informar um CEP e retorna automaticamente os dados de endereço: rua, bairro, cidade e UF.

---

## ✨ Funcionalidades

- Consulta de endereço via CEP usando a API ViaCEP
- Validação do campo CEP antes da requisição
- Máscara de entrada no formato `00000-000`
- Exibição dos campos: Rua, Bairro, Cidade e UF
- Botão para limpar os campos e realizar nova busca
- Tratamento de erros (CEP inválido, falha na requisição, exceções)

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| Python 3.x | Linguagem principal |
| PyQt5 | Interface gráfica |
| Requests | Requisições HTTP |
| ViaCEP API | Fonte dos dados de endereço |

---

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip

---

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Instale as dependências:
```bash
pip install requests PyQt5
```

3. Execute a aplicação:
```bash
python main.py
```

---

## 🚀 Como Usar

1. Informe o CEP no campo correspondente (formato: `00000-000`)
2. Clique em **Buscar CEP**
3. O endereço será preenchido automaticamente nos campos abaixo
4. Para realizar uma nova busca, clique em **Limpar busca**

---

## 📡 API Utilizada

Este projeto utiliza a [ViaCEP](https://viacep.com.br/), uma API REST gratuita para consulta de CEPs brasileiros.

Exemplo de requisição:
```
GET https://viacep.com.br/ws/01310100/json/
```

---

## 📂 Estrutura do Projeto

```
📁 seu-repositorio/
├── main.py       # Arquivo principal da aplicação
└── README.md     # Documentação do projeto
```
