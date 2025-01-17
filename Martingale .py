import random

balance = 10000  # you can change it if you want.
starting_bet = 1 
current_bet = starting_bet
max_bet = 10000 # you can change it if you want.  
results = []

def spin_roulette():
    return random.choice(list(range(0, 37)) + ["00"])
for round_number in range(1, 1000): # you can change it if you want. this is how many times the roulette spin.
    if balance <= 0:
        print(f"Game over! Balance is depleted on round {round_number}.")
        break

    if balance < current_bet:
        print(f"Game over! Insufficient balance to continue betting on round {round_number}.")
        break

    if current_bet > max_bet:
        print(f"Game over! Bet exceeds maximum allowed bet of {max_bet} on round {round_number}.")
        break

    number = spin_roulette()
    if number == "00" or number == 0: 
        odd_even = "Zero"
        balance -= current_bet
        outcome = "Loss"
        current_bet *= 2
    else:
        odd_even = "ODD" if number % 2 == 1 else "EVEN" 

        if odd_even == "ODD": 
            balance += current_bet 
            outcome = "Win"
            current_bet = starting_bet  
        else:  # Bet lost
            balance -= current_bet 
            outcome = "Loss"
            current_bet *= 2 

    results.append({
        "Round": round_number,
        "Number": number,
        "Odd/Even": odd_even,
        "Outcome": outcome,
        "Bet": current_bet if outcome == "Loss" else starting_bet,
        "Balance": balance
    })

print("\nRoulette Betting Simulation Results:")
print("Round\tNumber\tOdd/Even\tOutcome\tBet\tBalance")
for result in results:
    print(f"{result['Round']}\t{result['Number']}\t{result['Odd/Even']}\t{result['Outcome']}\t{result['Bet']}\t{result['Balance']}")