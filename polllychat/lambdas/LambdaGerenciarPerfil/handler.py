import json
from lambdas.LambdaGerenciarPerfil.intents.Saudacao import saudacao
from lambdas.LambdaGerenciarPerfil.intents.VerificarPerfil import verificar_perfil
from lambdas.LambdaGerenciarPerfil.intents.CriarPerfil import criar_perfil

def handler(event, context):
    if event.get('httpMethod'):
        # O evento veio de um API Gateway (requisição HTTP)
        return handle_http(event)

    # O evento veio do Lex
    intent_name = event['currentIntent']['name']

    if intent_name == 'Saudacao':
        return saudacao(event)
    elif intent_name == 'VerificarPerfil':
        return verificar_perfil(event)
    elif intent_name == 'CriarPerfil':
        return criar_perfil(event)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Intent não reconhecida'})
        }

def handle_http(event):
    # Tratar a requisição HTTP
    path = event['path']

    if path == '/perfil' and event['httpMethod'] == 'POST':
        # Processar os dados recebidos para criar ou verificar perfil
        body = json.loads(event['body'])
        telefone = body.get('telefone')

        # Simulação de resposta com o número de telefone
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Perfil de telefone {telefone} processado com sucesso!'})
        }

    # Caso o path não seja reconhecido
    return {
        'statusCode': 404,
        'body': json.dumps({'message': 'Rota não encontrada'})
    }
