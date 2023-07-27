import json


with open('./data.json', 'r') as file:
    values = json.load(file)


def convert(frm, to, val):
    scl = values[frm]['val']
    inr = scl * val
    scl = values[to]['val']
    return inr / scl


frm, to, val = 'usd', 'ued', 5


res_curr = convert(frm, to, val)


print(f'{values[to]["sym"]} {"%.2f" % res_curr}')