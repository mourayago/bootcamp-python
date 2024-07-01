log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

log_level = log["level"]
log_message = log["message"]

if log_level == "ERROR":
    print(log_message)