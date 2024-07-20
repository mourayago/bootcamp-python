from loguru import logger
from utils_log import log_decorator

logger.add("app.log")

def soma(x,y):
    logger.info(x)
    logger.info(y)
    logger.info(x+y)
    return x + y

def soma_1():
    x = input("digite um num")
    y = input("digite um num")
    try:
        soma = int(x) + int(y)
        logger.info(f"Soma realizada igual a {soma}")
        return soma
    except Exception as e:
        logger.error(e)

@log_decorator
def soma_2():
    x = input("digite um num")
    y = input("digite um num")
    soma = x + y
    return soma

if __name__ == "__main__":
    # var = soma(2,3)
    # var = soma_1()
    var = soma_2()
    print(var)