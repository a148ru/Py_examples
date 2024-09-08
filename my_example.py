import random

# Константы
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

NCARDS = 8

#Проходим по колоде, и эта функция возввращает случайную карту из колоды
def getCard(deckListIn):
    thisCard = deckListIn.pop() #Снимаем одну каарту с верней части колоды и возвращаем
    return thisCard

# Проходим по колоде, и эта функция возвращает перемешанную копию колоды
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # Создаем копию старой колоды
    random.shuffle(deckListOut)
    return deckListOut
