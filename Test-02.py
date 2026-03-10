elif key == "3":
if current_puzzle >= len(puzzles):
    print("All puzzle clues answered!")
    return current_puzzle
continent = puzzles[current_puzzle]
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(f"One puzzle piece is located in: {continent[0]} continent.")
return current_puzzle
return current_puzzle






def get_puzzle_clues(connection):
    sql= "SELECT continent FROM airport where puzzle_piece IS NOT null"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    clues = []
    for i in result:
        clues.append(i)
    cursor.close()
    return clues
























