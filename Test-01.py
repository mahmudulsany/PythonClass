import random
countries_data = [
    ("United Arab Emirates", "AE", "Asian"), ("Australia", "AU", "Oceanian"),
    ("Bangladesh", "BD", "Asian"), ("Brazil", "BR", "South American"),
    ("Canada", "CA", "North American"), ("China", "CN", "Asian"),
    ("Germany", "DE", "European"), ("Denmark", "DK", "European"),
    ("Spain", "ES", "European"), ("Finland", "FI", "European"),
    ("France", "FR", "European"), ("United Kingdom", "GB", "European"),
    ("India", "IN", "Asian"), ("Japan", "JP", "Asian"),
    ("Pakistan", "PK", "Asian"), ("Sweden", "SE", "European"),
    ("Singapore", "SG", "Asian"), ("Turkey", "TR", "Asian"),
    ("United States", "US", "North American"), ("South Africa", "ZA", "African")
]

master_list = []
for name, iso, cont in countries_data:
    master_list.append({"name": name, "code": iso + "1", "continent": cont})
    master_list.append({"name": name, "code": iso + "2", "continent": cont})

def start_game():
    puzzle_no = 1
    while puzzle_no <= 40:
        correct_item = random.choice(master_list)

        wrong_options = []
        other_continents = list(
            set(item['continent'] for item in master_list if item['continent'] != correct_item['continent']))

        selected_continents = random.sample(other_continents, 2)

        for cont in selected_continents:
            potential_wrong = [item for item in master_list if item['continent'] == cont]
            wrong_options.append(random.choice(potential_wrong))

        options_list = [correct_item] + wrong_options
        random.shuffle(options_list)

        options_text = " / ".join([f"{opt['name']}= {opt['code']}" for opt in options_list])

        print(
            f"\n{puzzle_no}st clue: Puzzle-{puzzle_no:02d} is located in an {correct_item['continent']} country ({options_text})")
        user_answer = input("Enter the correct code: ").strip().upper()

        if user_answer == correct_item['code']:
            print("Correct!")
            puzzle_no += 1
        else:
            print("Wrong answer. Try again.")

if __name__ == "__main__":
    start_game()