#DD Period 7 For Fun :D

def print_board(board):
	# ASCII art for big X and O
	big_X = [
		"\\   /",
		"  X  ",
		"/   \\"
	]
	big_O = [
		" /*\\ ",
		"| O |",
		" \\_/ "
	]

	for big_row in range(3):
		for small_row in range(3):
			row = []
			for big_col in range(3):
				sub = board[big_row][big_col]
				winner = check_win(sub)
				if winner:
					art = big_X if winner == 'X' else big_O
					row.append(art[small_row])
				else:
					row.append(' '.join(sub[small_row]))
			print(' | '.join(row))
		if big_row < 2:
			print('-' * 21)

def check_win(sub_board):
	# Check win for a 3x3 board
	for i in range(3):
		if sub_board[i][0] == sub_board[i][1] == sub_board[i][2] != ' ':
			return sub_board[i][0]
		if sub_board[0][i] == sub_board[1][i] == sub_board[2][i] != ' ':
			return sub_board[0][i]
	if sub_board[0][0] == sub_board[1][1] == sub_board[2][2] != ' ':
		return sub_board[0][0]
	if sub_board[0][2] == sub_board[1][1] == sub_board[2][0] != ' ':
		return sub_board[0][2]
	return None

def is_full(sub_board):
	return all(cell != ' ' for row in sub_board for cell in row)

def get_move(player, next_board, board, sub_wins):
	while True:
		if next_board is None:
			print(f"{player}'s turn. Choose sub-board (row col, 1-3): ")
			try:
				br, bc = map(int, input().split())
				br -= 1
				bc -= 1
				if not (0 <= br < 3 and 0 <= bc < 3):
					print("Invalid sub-board. Enter numbers 1-3.")
					continue
				if sub_wins[br][bc] is not None or is_full(board[br][bc]):
					print("Sub-board already won or full. Choose another.")
					continue
			except:
				print("Invalid input. Enter two numbers 1-3 separated by a space.")
				continue
		else:
			br, bc = next_board
			print(f"{player}'s turn in sub-board ({br+1} {bc+1})")
		print(f"Choose cell in sub-board ({br+1} {bc+1}) (row col, 1-3): ")
		try:
			sr, sc = map(int, input().split())
			sr -= 1
			sc -= 1
			if not (0 <= sr < 3 and 0 <= sc < 3):
				print("Invalid cell. Enter numbers 1-3.")
				continue
			if board[br][bc][sr][sc] != ' ':
				print("Cell already taken. Try again.")
				continue
			return br, bc, sr, sc
		except:
			print("Invalid input. Enter two numbers 1-3 separated by a space.")

def main():
	# Initialize 3x3 of 3x3 boards
	board = [[[[' ' for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
	sub_wins = [[None for _ in range(3)] for _ in range(3)]
	main_win = None
	player = 'X'
	next_board = None
	while not main_win and any(sub_wins[r][c] is None and not is_full(board[r][c]) for r in range(3) for c in range(3)):
		print_board(board)
		br, bc, sr, sc = get_move(player, next_board, board, sub_wins)
		board[br][bc][sr][sc] = player
		# Check sub-board win
		winner = check_win(board[br][bc])
		if winner:
			sub_wins[br][bc] = winner
			print(f"Player {winner} has claimed cell ({br+1}, {bc+1})!")
		# Check main board win
		main_win = check_win(sub_wins)
		if main_win:
			print_board(board)
			print(f"Player {main_win} wins the game!")
			return
		# Next board is determined by last move
		if sub_wins[sr][sc] is None and not is_full(board[sr][sc]):
			next_board = (sr, sc)
		else:
			next_board = None
		player = 'O' if player == 'X' else 'X'
	print_board(board)
	print("Game over! It's a draw.")

if __name__ == "__main__":
	main()