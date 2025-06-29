# Assistente de Busca com IA Gemini

## Descrição
Este projeto implementa um assistente de busca inteligente utilizando a API do Google Gemini, adicionando uma especialidade configurável a ferramenta. O sistema permite fazer consultas de texto usando linguagem natural, onde o modelo de IA analisa e responde às perguntas do usuário.

## Funcionalidades
- Processamento de texto usando IA Gemini
- Frontend acoplado ao projeto
- Respostas contextualizadas baseadas na especialidade configurada.

## Pré-requisitos
- Python 3.10+
- pip

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/marcelquin/Python-Ia-Expecialista.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd projeto-ia/app
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```


## Configuração
1. Crie o arquivo .env com a variavel GOOGLE_API_KEY
2. Adicione sua chave de API:
   ```
   GOOGLE_API_KEY=sua_chave_aqui
   ```
3. No arquivo ia_Treinamento.py na área prompt do código defina a especialidade do assistente.
4. Para fazer o deploy utilizando a imagem salva no Docker Hub faça p push e utilize com todas as configurações realizadas, inclusive a adição do nome da mesma no deployment.yaml.
