from collections import Counter

# Part 1: (J)acks
HAND_TYPES = {
    (5,): 6,  # five of a kind
    (1, 4): 5,  # four of a kind
    (2, 3): 4,  # full house
    (1, 1, 3): 3,  # three of a kind
    (1, 2, 2): 2,  # two pair
    (1, 1, 1, 2): 1,  # one pair
    (1, 1, 1, 1, 1): 0,  # high card
}


def parse_hand(line):
    hand, bid = line.split()
    hand = hand.translate(str.maketrans("TJQKA", "BCDEF"))
    counts = tuple(sorted(Counter(hand).values()))
    hand_type = HAND_TYPES[counts]
    hand = str(hand_type) + hand
    hand = int(hand, 16)
    bid = int(bid)
    return hand, bid


hands = dict(parse_hand(l) for l in open("./7.txt"))
print(sum([(r + 1) * hands[h] for r, h in enumerate(sorted(hands.keys()))]))

# Part 2: (J)okers removed
HAND_TYPES_WILD = {
    (5,): 6,  # five of a kind
    (4,): 6,
    (3,): 6,
    (2,): 6,
    (1,): 6,
    tuple(): 6,
    (1, 4): 5,  # four of a kind
    (1, 3): 5,
    (1, 2): 5,
    (1, 1): 5,
    (2, 3): 4,  # full house
    (2, 2): 4,
    (1, 1, 3): 3,  # three of a kind
    (1, 1, 2): 3,
    (1, 1, 1): 3,
    (1, 2, 2): 2,  # two pair
    (1, 1, 1, 2): 1,  # one pair
    (1, 1, 1, 1): 1,
    (1, 1, 1, 1, 1): 0,  # high card
}

def parse_hand_wild(line):
    hand, bid = line.split()
    hand = hand.translate(str.maketrans("TJQKA", "B1DEF"))
    hand_wild = hand.replace("1","")
    counts = tuple(sorted(Counter(hand_wild).values()))
    hand_type = HAND_TYPES_WILD[counts]
    hand = str(hand_type) + hand
    hand = int(hand, 16)
    bid = int(bid)
    return hand, bid

hands_wild = dict(parse_hand_wild(l) for l in open("./7.txt"))
print(sum([(r + 1) * hands_wild[h] for r, h in enumerate(sorted(hands_wild.keys()))]))