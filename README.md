# 📝 To-Do List em Flask

Um aplicativo web de lista de tarefas desenvolvido com o objetivo de praticar e consolidar conceitos Full-Stack, principalmente do **Flask** no back-end, autenticação de usuários com **Flask-Login** (`LoginManager`) e persistência de dados com **SQLite**, integrado a um front-end responsivo utilizando **HTML**, **CSS** e **Bootstrap**.

## 🚀 Tecnologias Utilizadas

- **Python**
- **Flask** (Microframework web)
- **Flask-SQLAlchemy** (ORM para modelagem e gerenciamento do banco de dados)
- **Flask-Login** (Gerenciamento de sessões e autenticação de usuários)
- **SQLite** (Banco de dados relacional para persistência de usuários e tarefas)
- **HTML5 & CSS3**
- **Bootstrap** (Estilização e responsividade)
- **Jinja2** (Motor de templates do Flask)

## ✨ Funcionalidades

- **Autenticação Completa:** Sistema de cadastro de novos usuários, login, logout e proteção de rotas privadas.
- **Gestão Individual de Tarefas:** Cada usuário visualiza e gerencia apenas suas próprias tarefas.
- **Adicionar Tarefas:** Insira novas pendências na sua lista com facilidade.
- **Gerenciar Estado:** Marque tarefas como concluídas ou remova-as quando necessário.
- **Persistência de Dados:** Armazenamento relacional (Usuários ↔ Tarefas) utilizando SQLite integrado via SQLAlchemy.
- **Design Responsivo:** Interface adaptada para diferentes tamanhos de tela graças ao Bootstrap.

## ⚙️ Como Rodar o Aplicativo

### Pré-requisitos

* **Python 3.8+** instalado
* **Git** instalado

### Passo a passo

1. **Clone o repositório e entre na pasta do projeto:**
```bash
git clone [https://github.com/Limaster98/to-do-list-project.git](https://github.com/Limaster98/to-do-list-project.git)
cd to-do-list-project

```

2. **Crie e ative um ambiente virtual (`venv`):**
* **Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate

```

* **Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate

```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt

```

4. **Execute a aplicação:**
```bash
python app.py

```

5. **Acesse no navegador:**
Abra o endereço abaixo, crie uma conta na tela de cadastro e faça login para começar a usar:
```text
http://127.0.0.1:5000/

```
