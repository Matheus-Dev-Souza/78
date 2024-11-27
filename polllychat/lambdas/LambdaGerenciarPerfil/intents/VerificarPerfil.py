# lambdas/LambdaGerenciarPerfil/intents/VerificarPerfil.py
from lambdas.LambdaGerenciarPerfil.services.telegram_service import send_message
from lambdas.LambdaGerenciarPerfil.services.dynamodb_service import get_user_profile

def handler(event, context):
    user_id = event.get('userId', '')
    chat_id = event.get('chatId', '')
    
    if not user_id or not chat_id:
        return {'statusCode': 400, 'body': 'Por favor, forneça um ID de usuário e chat ID válidos.'}
    
    profile = get_user_profile(user_id)
    if profile:
        message = f'Perfil encontrado para o usuário {user_id}.'
        send_message(chat_id, message)
        return {
            'statusCode': 200,
            'body': message
        }
    else:
        message = f'Perfil não encontrado para o usuário {user_id}.'
        send_message(chat_id, message)
        return {
            'statusCode': 404,
            'body': message
        }
