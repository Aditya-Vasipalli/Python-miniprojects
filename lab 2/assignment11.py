def missing_card():
    new_deck=[]
    for i in range(N-1):
        remaining_card=int(input('enter the number on the remaining cards: '))
        new_deck.append(remaining_card)
    for i in card_deck:
        if i not in new_deck:
            print(f'card number {i} was lost')
try:
    N=int(input('what is the Nth Card'))
    card_deck=[i for i in range(1,N+1)]
    missing_card()
except ValueError:
    print('please enter an integer')