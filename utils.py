from decimal import Decimal, ROUND_HALF_UP

def round_decimal(val:float, n_digits:int = 0)->float:

    d:Decimal = Decimal(str(val))

    n:str = "1"
    for i in range(n_digits):
        if i == 0:
            n += "."
        n += "0"
    return float(d.quantize(Decimal(n), ROUND_HALF_UP))
