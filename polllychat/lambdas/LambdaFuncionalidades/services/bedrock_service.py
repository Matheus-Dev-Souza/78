import json
import os
import boto3
# traduzir
def generate_language_tips(language):
    """
    Gera dicas úteis e práticas para o aprendizado de um idioma específico, usando o Amazon Bedrock.

    Args:
        language (str): O nome do idioma (ex: "Inglês") para o qual gerar as dicas.

    Returns:
        str: Texto gerado com informações sobre nível de dificuldade, aspectos culturais, técnicas de aprendizado e desafios comuns.
    """
    
    # Configuração do cliente Bedrock
    bedrock_runtime = boto3.client(
        service_name='bedrock-runtime', 
        region_name='us-east-1'
    )

    # Prompt para o modelo Bedrock
    prompt = f"""
    Forneça informações úteis sobre o aprendizado do idioma {language} no seguinte formato específico, mantendo exatamente estas seções:

    Dicas para aprender {language}:
    Nível de Dificuldade: [Descreva o nível de dificuldade (baixo/médio/alto) e aspectos que podem facilitar ou dificultar o aprendizado]
    Aspectos Culturais e Linguísticos: [Descreva características culturais importantes e traços linguísticos únicos do idioma]
    Técnicas e Métodos de Aprendizado: [Sugira métodos práticos para o aprendizado, como prática de conversação, leitura de livros específicos, etc.]
    Desafios Comuns: [Liste desafios comuns enfrentados por alunos ao aprender o idioma, como pronúncia ou gramática]

    Mantenha as respostas concisas, focando em informações práticas, curtas, diretas e úteis para alunos iniciantes e intermediários.
    """

    # Corpo da requisição
    request_body = json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 4096,
            "stopSequences": [],
            "temperature": 0.2,  # Ajuste a temperatura conforme necessário
            "topP": 0.9
        }
    })

    # Parâmetros da requisição
    modelId = 'amazon.titan-tg1-large'
    accept = 'application/json'
    contentType = 'application/json'

    try:
        model_response = bedrock_runtime.invoke_model(
            body=request_body,
            modelId=modelId,
            accept=accept,
            contentType=contentType
        )
        response_contents = json.loads(model_response.get('body').read().decode('utf-8'))

        generated_text = response_contents.get('results')[0].get('outputText')
        return generated_text

    except Exception as e:
        print(f"Erro ao gerar dicas para o idioma: {str(e)}")
        raise e

# Exemplo de uso da função
languages = [{"Name": "Espanhol"}]  # Exemplo de idiomas
main_language = languages[-1]['Name'] if len(languages) > 1 else languages[0]['Name']
tips = generate_language_tips(main_language)

# Retorna lista com dicionário contendo o idioma e as dicas formatadas
result = [{
    "idioma": languages,
    "Dicas": tips
}]

print(result)