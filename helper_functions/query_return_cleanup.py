
def clean_string_spaces(portfolio):
    for index, position in enumerate(portfolio):
        portfolio[index][1] = position[1].split(' ')[0]
    return portfolio

def convert_float(portfolio):
    for index, position in enumerate(portfolio):
        portfolio[index][2] = float(position[2])
    return portfolio
