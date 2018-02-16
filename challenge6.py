def gerund_infinitive(string):
    if string[-3:] == 'ing':
        return "to" + string[:-3]
    else:
        return "that is not a gerund"

    print gerund_infinitive("building")
    print gerund_infinitive("build")
