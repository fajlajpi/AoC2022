with open("data/input_02.txt") as f:
    rps_data = list(map(str.strip, f.readlines()))

def rps(matchup: str):

    # constants for hands
    R = "rock"
    P = "paper"
    S = "scissors"

    if len(matchup) != 3:
        print(f"Unexpected input length. Expected 3, received {len(matchup)}.")
    
    # A is Rock, B is Paper, C is Scissors
    choice_opponent = matchup[0:1]
    if choice_opponent == "A":
        choice_opponent = R
    elif choice_opponent == "B":
        choice_opponent = P
    elif choice_opponent == "C":
        choice_opponent = S
    else:
        print(f"Unexpected opponent's hand, received: {choice_opponent}, expected A or B or C.")

    # X is Rock, Y is Paper, Z is Scissors
    choice_player = matchup[2:3]
    if choice_player == "X":
        choice_player = R
    elif choice_player == "Y":
        choice_player = P
    elif choice_player == "Z":
        choice_player = S
    else:
        print(f"Unexpected player's hand, received: {choice_player}, expected X or Y or Z.")
    
    points_match = 0
    points_hand = 0

    if choice_player == R:
        points_hand = 1
    elif choice_player == P:
        points_hand = 2
    elif choice_player == S:
        points_hand = 3
    else:
        print("Unexpected player hand.")
    
    if choice_player == choice_opponent:
        points_match = 3 # DRAW
    elif choice_player == R:
        if choice_opponent == P:
            points_match = 0 # LOSS
        elif choice_opponent == S:
            points_match = 6 # WIN
    elif choice_player == P:
        if choice_opponent == S:
            points_match = 0 # LOSS
        elif choice_opponent == R:
            points_match = 6 # WIN
    elif choice_player == S:
        if choice_opponent == R:
            points_match = 0 # LOSS
        elif choice_opponent == P:
            points_match = 6 # WIN
    
    return points_match + points_hand

result = 0

for line in rps_data:
    result += rps(line)

print(f"Part one: {result}")

def rps2(matchup: str):

    # constants for hands
    R = "rock"
    P = "paper"
    S = "scissors"

    LOSS = "loss"
    DRAW = "draw"
    WIN = "win"

    if len(matchup) != 3:
        print(f"Unexpected input length. Expected 3, received {len(matchup)}.")
    
    # A is Rock, B is Paper, C is Scissors
    choice_opponent = matchup[0:1]
    if choice_opponent == "A":
        choice_opponent = R
    elif choice_opponent == "B":
        choice_opponent = P
    elif choice_opponent == "C":
        choice_opponent = S
    else:
        print(f"Unexpected opponent's hand, received: {choice_opponent}, expected A or B or C.")

    # X is LOSS, Y is DRAW, Z is WIN
    outcome = matchup[2:3]
    if outcome == "X":
        outcome = LOSS
    elif outcome == "Y":
        outcome = DRAW
    elif outcome == "Z":
        outcome = WIN
    else:
        print(f"Unexpected outcome, received: {choice_player}, expected X or Y or Z.")
    
    choice_player = ""
    if outcome == DRAW:
        points_match = 3 # DRAW
        choice_player = choice_opponent
    elif outcome == WIN:
        points_match = 6 # WIN
        if choice_opponent == R:
            choice_player = P
        elif choice_opponent == P:
            choice_player = S
        elif choice_opponent == S:
            choice_player = R
    elif outcome == LOSS:
        points_match = 0 # LOSS
        if choice_opponent == R:
            choice_player = S
        elif choice_opponent == P:
            choice_player = R
        elif choice_opponent == S:
            choice_player = P

    points_hand = 0

    if choice_player == R:
        points_hand = 1
    elif choice_player == P:
        points_hand = 2
    elif choice_player == S:
        points_hand = 3
    else:
        print("Unexpected player hand.")
    
    return points_match + points_hand

result2 = 0

for line in rps_data:
    result2 += rps2(line)

print(f"Part two: {result2}")