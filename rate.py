def month_rate(month):
    
    month_rate = 50
    total_cost = month_rate * month
   
    if month >= 6:
      total_cost == total_cost - 10
    
    if month >= 12:
      total_cost == total_cost - 25
    return  total_cost
    
