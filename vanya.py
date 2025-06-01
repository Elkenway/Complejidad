def zero_cards(n, x, cards):
    cards_sum = sum(cards)
    
    if cards_sum == 0:
        return 0
        
    if abs(cards_sum) > x * n:
        return -1
        
    if abs(cards_sum) <= x:
        return 1
        
    return 2

n, x = map(int, input().split())
cards = list(map(int, input().split()))

print(zero_cards(n, x, cards))