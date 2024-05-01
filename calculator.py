from logger import logging

def addition(num1, num2):
    sum = num1 + num2
    logging.info(f'{num1} + {num2 } = {sum}')
    return sum

def substraction(num1,num2):
    sub = num1 -num2
    logging.info(f'{num1} + {num2} = {sub}')
    return sub

def multiplication(num1, num2):
    mul = num1 * num2
    logging.info(f'{num1} + {num2} = {mul}')
    return mul

def division(num1, num2):
    try:
        div = num1 / num2
        logging.info(f'{num1} + {num2} = {div}')
        return div
    except ZeroDivisionError:
        logging.error("Division by zero is now allowed")
        return None

