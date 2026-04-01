def safe_response(resp):
    try:
        return resp.content
    except:
        try:
            return str(resp)
        except:
            return "Erro ao gerar resposta"
