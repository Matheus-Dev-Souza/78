# lambdas/LambdaGerenciarPerfil/intents/CriarPerfil.py
import boto3
from lambdas.LambdaGerenciarPerfil.services.dynamodb_service import save_user_profile

def handler(event, context):
    user_id = event.get('userId', '')
    name = event.get('name', '')
    languages = event.get('languages', [])
    photo_url = event.get('photo_url', '')
    
    if not user_id or not name or not languages:
        return {'statusCode': 400, 'body': 'Todos os dados são obrigatórios.'}
    
    # Salva o perfil no DynamoDB
    save_user_profile(user_id, name, languages, photo_url)
    
    return {
        'statusCode': 201,
        'body': f'Perfil criado com sucesso para o usuário {user_id}.'
    }
