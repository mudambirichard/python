def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *=1.08
    print "with tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *=1.15
    print "with tip: %f" % bill
    return bill

meal_cost = 100
meal_with_tax = (meal_cost)
meal_with_tip = (meal_with_tax)
