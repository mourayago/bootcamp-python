transacao = {'valor': 12000, 'hora': 20}

val_trx = transacao["valor"]
hora_trx = transacao["hora"]

if val_trx > 10000 or hora_trx < 9 or hora_trx > 18:
    print('transacao suspeita')
else: 
    print('transação ok')