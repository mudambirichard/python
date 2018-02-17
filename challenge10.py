from morse import morse_code

def morsify(string):
    final_string = ''
    for letter in string:
        final_string = final_string + morse_code[letter]
    return final_string

print (morsify("TRINKET"))
