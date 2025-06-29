import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def fazer_busca(pergunta):
    try:
        modelo = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Você é um especialista em...
        com base nisso responda a seguinte pergunta : {pergunta}.        
        """
        
        # Gera a resposta
        resposta = modelo.generate_content(prompt)
        return resposta.text
    
    except Exception as e:
        return f"Erro ao processar a busca: {str(e)}"

def main():
   
    while True:
            pergunta = input("\nDigite sua pergunta sobre o texto (ou 'sair' para encerrar): ")
            
            if pergunta.lower() == 'sair':
                break

            resposta = fazer_busca(conteudo, pergunta)
            print("\nResposta:", resposta)
            print("\n" + "-"*50)

if __name__ == "__main__":
    main()
