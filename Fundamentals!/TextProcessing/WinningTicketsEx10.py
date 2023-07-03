def is_winning_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$','^']
    lef_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10,5,-1):
            winning_symbol_repetitions = match_symbol * uninterrupted_match_length
            if winning_symbol_repetitions in lef_part and winning_symbol_repetitions in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'

tickets = [ticket.strip() for ticket in input().split(",")]

for ticket in tickets:
    print(is_winning_ticket(ticket))