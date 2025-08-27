# 🐍 PyMesseger

PyMesseger é um **aplicativo de mensagens simples** desenvolvido em **Python** utilizando o [Streamlit](https://streamlit.io/).  
O objetivo do projeto é permitir que múltiplos usuários possam se registrar, autenticar e trocar mensagens em tempo real em uma interface amigável e minimalista.

---

## ✨ Funcionalidades

- 👤 **Cadastro de usuários**  
- 🔑 **Login com autenticação de senha**  
- 💬 **Envio e recebimento de mensagens em tempo real**  
- 📂 **Armazenamento local de usuários e mensagens** (usando `pickle`)  
- 📝 **Interface interativa** com [Streamlit](https://streamlit.io/)  

---

## 📦 Tecnologias Utilizadas

- [Python 3.9+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – Interface Web  
- [Unidecode](https://pypi.org/project/Unidecode/) – Normalização de nomes de usuário  
- [Pathlib](https://docs.python.org/3/library/pathlib.html) – Manipulação de diretórios  
- [Pickle](https://docs.python.org/3/library/pickle.html) – Persistência de dados  

---

## 🚀 Como Executar

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/pymesseger.git
cd pymesseger


### 2️⃣ Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

*(caso não exista o arquivo `requirements.txt`, instale manualmente:)*

```bash
pip install streamlit unidecode
```

### 4️⃣ Executar o projeto

```bash
streamlit run app.py
```

---

## 📂 Estrutura do Projeto

```
pymesseger/
│── app.py              # Arquivo principal da aplicação
│── users/              # Diretório de usuários cadastrados
│── mensagens/          # Diretório de mensagens armazenadas
│── requirements.txt    # Dependências do projeto
│── README.md           # Documentação do projeto
```

---

## 📸 Demonstração

* Tela de **Login / Cadastro**
* Seleção de **usuário para conversar**
* Interface de **chat em tempo real**

*(adicione aqui prints de tela quando disponível)*

---

## 🛠 Melhorias Futuras

* 🔒 Criptografia de senhas armazenadas
* 🌐 Implementação de banco de dados real (SQLite ou PostgreSQL)
* 📱 Layout responsivo e otimizado para mobile
* ☁️ Deploy em plataformas como **Streamlit Cloud**, **Heroku** ou **Railway**

---

## 🤝 Contribuição

Sinta-se à vontade para abrir **issues** e enviar **pull requests**.
Toda ajuda é bem-vinda para melhorar o projeto! 🚀

---

## 📜 Licença

Este projeto é distribuído sob a licença **MIT**.
Você pode usá-lo, modificá-lo e distribuí-lo livremente, desde que mantenha os créditos.

---

💡 Criado com ❤️ usando **Python + Streamlit**

```


Quer que eu também gere um **requirements.txt** para você com as dependências exatas do projeto?
```
## Author:
Desenvolvido por DanAliCode ❤️
