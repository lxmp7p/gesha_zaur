import keyboard
import random


def pretty_print(mas):
	print("="*10)
	for row in mas:
		print(*row)
	print("="*10)


def get_number_for_index(i, j):
	return i*4+j+1


def get_index_from_number(num):
	num-=-1
	x,y = num//4, num%4
	return x, y


def insert_2_or_4(mas,x,y):
	if x == 4:
		x-=1
	if y == 4:
		y-=1
	mas[x][y] = random.choice([2,4])
	return mas


def get_empty_list(mas):
	empty = []
	for i in range(4):
		for j in range(4):
			if mas[i][j]==0:
				num = get_number_for_index(i,j)
				empty.append(num)
	return empty


def check_correct(a, b):
	if a == b:
		return a+b

def sum_up(mas, i, j):
	if mas[i][j] == mas[i-1][j]:
		mas[i-1][j] += mas[i][j]
		mas[i][j] = 0
	elif mas[i][j] != mas[i-1][j] and mas[i-1][j] != 0:
		pass
	if mas[i-1][j] == 0:
		mas[i-1][j] = mas[i][j]
		mas[i][j] = 0


def sum_down(mas, i, j):
	if mas[i][j] == mas[i+1][j]:
		mas[i+1][j] += mas[i][j]
		mas[i][j] = 0
	elif mas[i][j] != mas[i+1][j] and mas[i+1][j] != 0:
		pass
	if mas[i+1][j] == 0:
		mas[i+1][j] = mas[i][j]
		mas[i][j] = 0


def sum_left(mas, i, j):
	if mas[i][j] == mas[i][j-1]:
		mas[i][j-1] += mas[i][j]
		mas[i][j] = 0
	elif mas[i][j] != mas[i][j-1] and mas[i][j-1] != 0:
		pass
	if mas[i][j-1] == 0:
		mas[i][j-1] = mas[i][j]
		mas[i][j] = 0


def sum_right(mas, i, j):
	if mas[i][j] == mas[i][j+1]:
		mas[i][j+1] += mas[i][j]
		mas[i][j] = 0
	elif mas[i][j] != mas[i][j+1] and mas[i][j+1] != 0:
		pass
	if mas[i][j+1] == 0:
		mas[i][j+1] = mas[i][j]
		mas[i][j] = 0


def up(mas):
	for i in range(4):
		for j in range(4):
			if mas[i][j] != 0 and i>0:
				sum_up(mas, i, j)


def down(mas):
	for i in range(4):
		for j in range(4):
			if mas[i][j] != 0 and i<3:
				sum_down(mas, i, j)


def left(mas):
	for i in range(4):
		for j in range(4):
			if mas[i][j] != 0  and j!=0 :
				sum_left(mas, i, j)


def right(mas):
	for i in range(4):
		for j in range(4):
			if mas[i][j] != 0 and j!=3:
				sum_right(mas, i, j)

mas = [
		[2,0,0,0],
		[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]
	]

mas[1][2] = 2
mas[3][0] = 4


while True:
	pretty_print(mas)
	check = input()
	if check == "w":
		up(mas)
	if check == "a":
		left(mas)
	if check == "d":
		right(mas)
	if check == "s":
		down(mas)
	empty = random.choice(get_empty_list(mas))
	x, y = get_index_from_number(empty)
	insert_2_or_4(mas, x, y)
		
