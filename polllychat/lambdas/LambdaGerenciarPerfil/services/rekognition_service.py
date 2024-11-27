# lambdas/LambdaGerenciarPerfil/services/rekognition_service.py
import boto3
from botocore.exceptions import ClientError

rekognition_client = boto3.client('rekognition')

def analyze_image(image_bytes):
    """
    Função para analisar uma imagem usando o AWS Rekognition.
    :param image_bytes: O conteúdo da imagem em bytes.
    :return: Resultados da análise da imagem, ou uma mensagem de erro.
    """
    try:
        # Envia a imagem para o Rekognition para análise
        response = rekognition_client.detect_labels(
            Image={'Bytes': image_bytes},
            MaxLabels=10,
            MinConfidence=75
        )
        return response['Labels']
    except ClientError as e:
        print(f"Erro ao processar a imagem: {e}")
        return {'error': str(e)}
