def should_hit(player_total, dealer_card_val, player_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay. player_aces is the number of aces the player has.
    """
    if player_total <= 12 and player_aces <=1:
        return True
    if player_total == 12 and dealer_card_val !=5:
        return True
    if (player_total <= 16 and player_aces <=1) and (dealer_card_val > 6):
        return True
    if (player_total == 17 and player_aces == 0) and (dealer_card_val == 1):
        return True
    if player_total > 17:
        return False
    if player_aces == 2:
        return False
    
blackjack.simulate(n_games=50000)