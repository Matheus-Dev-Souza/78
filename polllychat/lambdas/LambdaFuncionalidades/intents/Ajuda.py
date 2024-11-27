# lambdas/LambdaFuncionalidades/intents/Ajuda.py

def handler(event, context):
    return {
        'statusCode': 200,
        'body': '''Comandos disponíveis:
        /help - Exibe esta mensagem de ajuda.
        /transcribe - Transcreve um áudio.
        /translate - Traduz seu texto.
        /procurarEncontros - Procura encontros de idiomas.'''
    }
