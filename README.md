# Navbar Avançada

Este é um projeto de uma **navbar avançada** desenvolvida com Flask, HTML, CSS e JavaScript. Ele inclui funcionalidades modernas como navegação responsiva, dropdowns, animações suaves e design adaptável para diferentes dispositivos.

## Funcionalidades

- **Navegação Responsiva**: Barra de navegação adaptável para desktops, tablets e celulares.
- **Dropdowns**: Itens com submenus para organizar links de forma hierárquica.
- **Animações Suaves**: Transições CSS para melhorar a experiência do usuário.
- **Design Moderno**: Cores suaves, sombreamento e tipografia elegante.
- **Backend Dinâmico**: Flask serve páginas dinâmicas para demonstrar a funcionalidade da navbar.
- **Tratamento de Erros**: Página personalizada para erros 404.

## Estrutura do Projeto
navbar-avancado/
│
├── app.py                  # Backend principal (Flask)
├── static/                 # Arquivos estáticos
│   ├── css/                # Estilos CSS
│   │   └── styles.css      # Estilos principais
│   ├── js/                 # Lógica JavaScript
│   │   └── main.js         # Interações da navbar
│   └── images/             # Imagens usadas no projeto
│
├── templates/              # Templates HTML
│   ├── base.html           # Template base
│   ├── index.html          # Página inicial
│   ├── about.html          # Página "Sobre"
│   ├── services.html       # Página "Serviços"
│   ├── contact.html        # Página "Contato"
│   └── 404.html            # Página de erro 404
│
└── README.md               # Documentação do projeto

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado.
- Pip (gerenciador de pacotes Python).

### Passos

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Brunno2269/Navbar_Avancado.git
   cd navbar-avancado