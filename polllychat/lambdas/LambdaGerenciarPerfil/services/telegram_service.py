# lambdas/LambdaGerenciarPerfil/services/telegram_service.py
import requests
import json

TELEGRAM_API_URL = 'https://api.telegram.org/bot<SEU_TOKEN>/sendMessage'

def send_message(chat_id, text):
    """
    Função para enviar uma mensagem para o Telegram usando o bot.
    :param chat_id: ID do chat (usuário ou grupo) para enviar a mensagem.
    :param text: Texto da mensagem que será enviada.
    :return: Resposta da API do Telegram ou erro.
    """
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    try:
        response = requests.post(TELEGRAM_API_URL, data=payload)
        return response.json()  # Retorna a resposta da API do Telegram.
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar mensagem para o Telegram: {e}")
        return {'error': str(e)}
