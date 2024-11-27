# lambdas/LambdaGerenciarPerfil/intents/Saudacao.py

def handler(event, context):
    user_id = event.get('userId', 'desconhecido')
    return {
        'statusCode': 200,
        'body': f'Olá, {user_id}! Como posso ajudá-lo no aprendizado de idiomas?'
    }
