from random import randint
game_field = [
	[0,0,0],
	[0,0,0],
	[0,0,0]
]

def pretty_print(game_field):	
	for i in range(3):
		print(*game_field[i])


pretty_print(game_field)
def bot_step(game_field):
	while True:
		rand_int_row = randint(0,2)
		rand_int_column = randint(0,2)
		if game_field[rand_int_row][rand_int_column] == 0:
			if check_empty_field(game_field, rand_int_row, rand_int_column):
				game_field[rand_int_row][rand_int_column] = "Z"
				break;


def player_step():
	while True:
		field_num = int(input("Выберите точку:"))
		if field_num<4 and field_num<5:
			row, column = 0, field_num-4
		if field_num>3 and field_num<7:
			row, column = 1, field_num-4
		if field_num>6 and field_num<10:
			row, column = 2, field_num-7
		if game_field[row][column] == 0:
			game_field[row][column] = "X"
			break;
		print("Место занято!")



def check_empty_field(game_field, row, column):
	if game_field[row][column] == 0:
		return True
	return False


def check_win(game_field):
	win = None
	for i in range(3):
		win = check_row_win(game_field, i, True)
		if win:
			break;
		win = check_row_win(game_field, i, False)
		if win:
			break;

		win = check_column_win(game_field, i, True)
		if win:
			break;
		win = check_column_win(game_field, i, False)
		if win:
			break;

		win = check_diagonal_win(game_field, i, True)
		if win:
			break;
		win = check_diagonal_win(game_field, i, False)
	return win


def check_row_win(game_field, row, player):
	user = "Bot"
	symbol = "Z"
	if player:
		user = "Player"
		symbol = "X"
	if game_field[row][0] == symbol:
		if game_field[row][1] == symbol:
			if game_field[row][2] == symbol:
				return f"{user} WIN!"


def check_column_win(game_field, column, player):
	user = "Bot"
	symbol = "Z"
	if player:
		user = "Player"
		symbol = "X"
	if game_field[0][column] == symbol:
		if game_field[1][column] == symbol:
			if game_field[2][column] == symbol:
				return f"{user} WIN!"


def check_diagonal_win(game_field, column, player):
	user = "Bot"
	symbol = "Z"
	if player:
		user = "Player"
		symbol = "X"
	if game_field[1][1] == symbol:
		if game_field[0][0] == symbol:
			if game_field[2][2] == symbol:
				return f"{user} WIN!"
	if game_field[1][1] == symbol:
		if game_field[2][0] == symbol:
			if game_field[0][2] == symbol:
				return f"{user} WIN!"


while True:
	player_step()
	bot_step(game_field)
	pretty_print(game_field)
	end = check_win(game_field)
	if end:
		print(end)
		break;
