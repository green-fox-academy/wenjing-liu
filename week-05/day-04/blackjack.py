def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    if player_high_aces == 1 and player_total <= 17:
      return True
    elif player_high_aces == 1 and player_total == 18 and dealer_total >=9:
      return True
    elif player_total >= 17:
      return False
    elif (player_total >= 13 and player_total <= 16) and (dealer_total >=2 and dealer_total <= 6):
      return False
    elif (player_total >= 13 and player_total <= 16) and (dealer_total >=7 and dealer_total <= 11):
      return True
    elif (player_total == 12) and ((dealer_total >=2 and dealer_total <=3) or (dealer_total >=7 and dealer_total <= 11)):
      return True
    else:
      return True
