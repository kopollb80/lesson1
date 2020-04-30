def get_vat(payment):
    vat = payment / 100*18
    return round(vat,2)


print("Сумма НДС {}".format(get_vat(0.09)))