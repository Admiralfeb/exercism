
def is_pangram(sentence: str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alph_values = {}.fromkeys(alphabet, False)
    for c in sentence.lower():
        if c in alph_values:
            alph_values[c] = True
    if False in alph_values.values():
        return False
    else:
        return True
