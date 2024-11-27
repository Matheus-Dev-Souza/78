def transcrever_audio(event):
    # Lógica para transcrição de áudio
    audio_url = event['currentIntent']['slots']['AudioUrl']
    
    # Simulação de transcrição (só para exemplo)
    transcricao = "Texto transcrito do áudio"
    
    return {
        'dialogAction': {
            'type': 'Close',
            'message': {
                'contentType': 'PlainText',
                'content': f'A transcrição do áudio foi: {transcricao}'
            }
        }
    }
