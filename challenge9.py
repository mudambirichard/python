from US import states

def lookup_state(abbreviation):
    return states[abbreviation]

print (lookup_state("NY"))
print (lookup_state("CA"))
