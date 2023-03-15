import random
from collections import Counter

# Define the Monopoly board
board = [
    "Go", "Mediterranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax",
    "Reading Railroad", "Oriental Avenue", "Chance", "Vermont Avenue",
    "Connecticut Avenue", "Jail", "St. Charles Place", "Electric Company",
    "States Avenue", "Virginia Avenue", "Pennsylvania Railroad", "St. James Place",
    "Community Chest", "Tennessee Avenue", "New York Avenue", "Free Parking",
    "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue", "B&O Railroad",
    "Atlantic Avenue", "Ventnor Avenue", "Water Works", "Marvin Gardens", "Go To Jail",
    "Pacific Avenue", "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue",
    "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk"
]

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def simulate_game(turns):
    position = 0
    visit_counts = Counter()

    for _ in range(turns):
        roll = roll_dice()
        position = (position + roll) % len(board)
        
        if board[position] == "Go To Jail":
            position = board.index("Jail")
        
        visit_counts[position] += 1
    
    return visit_counts

def main():
    num_simulations = 1000000
    turns_per_simulation = 100
    
    total_counts = Counter()
    
    for _ in range(num_simulations):
        visit_counts = simulate_game(turns_per_simulation)
        total_counts.update(visit_counts)
    
    for space, count in total_counts.most_common():
        print(f"{board[space]}: {count/num_simulations:.2f}%")

if __name__ == "__main__":
    main()
