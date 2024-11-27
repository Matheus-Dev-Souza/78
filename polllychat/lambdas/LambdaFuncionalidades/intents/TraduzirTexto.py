def traduzir_texto(event):
    # Lógica para tradução de texto
    texto_original = event['currentIntent']['slots']['Texto']
    
    # Simulação de tradução (só para exemplo)
    traducao = "Texto traduzido"
    
    return {
        'dialogAction': {
            'type': 'Close',
            'message': {
                'contentType': 'PlainText',
                'content': f'A tradução do texto foi: {traducao}'
            }
        }
    }
