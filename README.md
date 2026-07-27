# 🌦️ API de Clima com Python

Um projeto simples em Python que consulta a previsão do tempo utilizando o serviço **wttr.in** e exibe as informações diretamente no terminal.

## 📌 Objetivo

Este projeto foi desenvolvido para praticar:

* Consumo de APIs com Python.
* Requisições HTTP utilizando a biblioteca `requests`.
* Manipulação de respostas da API.

## 🚀 Tecnologias

* Python 3
* Requests
* wttr.in

## 📂 Estrutura do Projeto

```text
api-clima/
├── main.py
├── requirements.txt
└── README.md
```

## 📥 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/api-clima.git
```

Entre na pasta do projeto:

```bash
cd api-clima
```

Instale a dependência:

```bash
pip install requests
```

Ou utilize o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## ▶️ Como executar

Execute o programa com:

```bash
python main.py
```

## 💻 Exemplo de código

```python
import requests

url = "https://wttr.in/Belo+Horizonte"

response = requests.get(url)
data = response.text

print(data)
```

## 📋 Exemplo de saída

```text
Weather report: Belo Horizonte

🌡️ Temperature: 22°C
☁️ Condition: Partly cloudy
💨 Wind: 8 km/h
💧 Humidity: 68%
```

> A saída pode variar conforme as condições climáticas no momento da consulta.

## 📄 Licença

Este projeto é destinado para estudos e aprendizado de consumo de APIs em Python.
