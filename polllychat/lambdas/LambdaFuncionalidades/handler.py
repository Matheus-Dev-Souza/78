import json
from lambdas.LambdaFuncionalidades.intents.TranscreverAudio import transcrever_audio
from lambdas.LambdaFuncionalidades.intents.TraduzirTexto import traduzir_texto

def handler(event, context):
    if event.get('httpMethod'):
        # O evento veio de um API Gateway (requisição HTTP)
        return handle_http(event)

    # O evento veio do Lex
    intent_name = event['currentIntent']['name']

    if intent_name == 'TranscreverAudio':
        return transcrever_audio(event)
    elif intent_name == 'TraduzirTexto':
        return traduzir_texto(event)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Intent não reconhecida'})
        }

def handle_http(event):
    # Tratar a requisição HTTP
    path = event['path']

    if path == '/funcionalidades' and event['httpMethod'] == 'POST':
        # Processar as funcionalidades, como transcrição ou tradução de texto
        body = json.loads(event['body'])
        texto = body.get('texto')

        # Simulação de resposta para transcrição ou tradução
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'O texto processado foi: {texto}'})
        }

    # Caso o path não seja reconhecido
    return {
        'statusCode': 404,
        'body': json.dumps({'message': 'Rota não encontrada'})
    }
