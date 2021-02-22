def convert(number: int):
    sounds = [(3, 'Pling'), (5, 'Plang'), (7, 'Plong')]
    return_string = ''

    for sound in sounds:
        if number % sound[0] == 0:
            return_string += sound[1]

    if return_string == '':
        return_string = str(number)

    return return_string
