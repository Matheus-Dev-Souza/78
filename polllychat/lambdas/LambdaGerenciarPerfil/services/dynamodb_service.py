# lambdas/LambdaGerenciarPerfil/services/dynamodb_service.py
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UsuarioPerfil')

def get_user_profile(user_id):
    """
    Função para recuperar o perfil do usuário do DynamoDB.
    :param user_id: O ID do usuário que está sendo procurado.
    :return: O perfil do usuário ou None se não encontrado.
    """
    try:
        response = table.get_item(Key={'id': user_id})
        return response.get('Item')
    except ClientError as e:
        print(f"Erro ao recuperar perfil: {e}")
        return None

def save_user_profile(user_id, name, languages, photo_url):
    """
    Função para salvar o perfil de um usuário no DynamoDB.
    :param user_id: O ID do usuário.
    :param name: O nome do usuário.
    :param languages: Lista de idiomas que o usuário está aprendendo.
    :param photo_url: URL da foto do perfil do usuário.
    :return: Nenhum retorno, apenas faz a operação de gravação.
    """
    try:
        table.put_item(
            Item={
                'id': user_id,
                'name': name,
                'languages': languages,
                'photo_url': photo_url
            }
        )
    except ClientError as e:
        print(f"Erro ao salvar perfil: {e}")
