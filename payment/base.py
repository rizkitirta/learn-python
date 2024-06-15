def import_payment_module(payment_name):
    try:
        module = __import__(f'payment.{payment_name}', fromlist=['pay'])
        return module
    except ImportError:
        return None



def get_payment_name(payment_name):
    payment = import_payment_module(payment_name)
    return payment.pay() if payment else 'Payment module not found'