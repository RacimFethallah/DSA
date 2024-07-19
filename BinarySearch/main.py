test = {
    'input': {
        'cards': [13, 12, 11 , 7 , 5 , 3 , 1],
        'query': 12, 
    },
    'output': 1,
}

def locate_card_bs(cards, query, b, e):
    if b > e:
        return -1
    
    middle = (b + e) // 2

    if cards[middle] == query:
        return middle
    elif cards[middle] > query:
        return locate_card_bs(cards, query, middle + 1, e )
    else:
        return locate_card_bs(cards, query, b, middle - 1 )
    


result = locate_card_bs(test['input']['cards'], test['input']['query'], 0, len(test['input']['cards']) - 1)
print(result == test['output'])

