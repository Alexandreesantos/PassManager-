# Sistema de Login com Flask 🚀  

Um sistema de login simples utilizando Flask. Este projeto inclui um formulário de autenticação, sistema de sessão e uma página protegida (dashboard) acessível apenas para usuários autenticados.  

## Funcionalidades ✨  
- Formulário de login moderno e responsivo  
- Validação de usuários com autenticação manual  
- Sessões para gerenciar usuários logados  
- Página de dashboard acessível após login  
- Botão "Esqueci a senha" (em desenvolvimento)  

## Tecnologias Utilizadas 🛠️  
- **Backend:** Flask (Python)  
- **Frontend:** HTML5 + CSS3  
- **Templates:** Jinja2  

## Como Executar o Projeto 🏃  
1. **Clone o repositório**  
```bash  
git clone https://github.com/Alexandreesantos/PassManager-.git  
cd PassManager- 

python -m venv venv  
source venv/bin/activate  # (Linux/Mac)  
venv\\Scripts\\activate    # (Windows)  

pip install flask  

python app.py  

http://127.0.0.1:5000

/nome-do-repositorio  
│  
├── app.py               # Arquivo principal do Flask  
├── /templates           # Arquivos HTML  
│   └── login.html       # Página de login  
├── /static              # (Opcional) Arquivos CSS e JS  
└── README.md            # Este arquivo  


Melhorias Futuras 🚧
Integração com banco de dados (SQLite ou PostgreSQL)
Sistema de redefinição de senha funcional
Cadastro de novos usuários
Contribuição 🤝
Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades!
