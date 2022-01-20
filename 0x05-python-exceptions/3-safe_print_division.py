#!/usr/bin/python3
def safe_print_division(a, b):
    respuesta = 0
    try:
        respuesta = a / b
    except ZeroDivisionError:
        respuesta = None
    finally:
        print("Inside result: {}".format(respuesta))
    return respuesta

