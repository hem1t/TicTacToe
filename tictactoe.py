#! /usr/bin/python3

import os

# Extra Functions to help
def isNum(num):
	try:
		int(num)
	except ValueError:
		return False
	else:
		return True

# Main class to run the code
class main():
	def __init__(self):
		# Create board
		# if 0 then its not yet choosed 
		self.board = [str(i) for i in range(1,10)]
		self.player1 = ""
		self.player2 = ""
		self.Start()


	def Start(self):
		# Will interact to others
		# while loop for first player.
		while True:
			try:
				self.player1 = input("player1 tell your name: ")
				ack = input("Are you ok with your name(y/n)").lower()
				if ack == "y":
					break
				if ack == "n":
					continue
			except:
				pass

		# while loop for second player.
		while True:
			try:
				self.player2 = input("player2 tell your name: ")
				ack = input("Are you ok with your name(y/n)").lower()
				if ack == "y":
					break
				if ack == "n":
					continue
			except:
				pass
		print("Thank you two and {} is 'x' and {} is 'o'.\n".format(self.player1, self.player2))


	def Reset(self):
		# Resets the game except names
		self.board = [str(i) for i in range(1,10)]
		self.draw()

### Main logic PROGRAM ###
	def check(self):
		# TODO Make a logic to check the game status
		# This will return 0 if no one wins and 1 if player1 wins and 2 if player two wins
		# 4 if its a draw.
		countX_O = 0
		draw_count = 0
		countX = 0
		countO = 0
		# if count goes to 3 its win
		# Checking for win.
		win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
						  [0, 3, 6], [1, 4, 7], [2, 5, 8],
						  [0, 4, 8], [2, 4, 6]]

		# Checking for win between x and o.
		for win in win_conditions:
			for i in win:
				if self.board[i] == "x":
					countX += 1
					countX_O += 1
				elif self.board[i] == "o":
					countO += 1
					countX_O += 1 
			if countX_O == 3:
				draw_count += 1
			# checking for win number 3; if not reset them; for next WIN check
			if countX == 3:
				return 1
			if countO == 3:
				return 2
			#reseting counts
			countX_O = 0
			countO = 0
			countX = 0
		if draw_count == 8:
			return 4


	def draw(self):
		# TODO Make this to draw and clear first the screen
		os.system("clear")

		brek ="\t*************"
		line1 ="\n\t  "+self.board[0]+" | "+self.board[1]+" | "+self.board[2]+"\n"+brek
		line2 ="\n\t  "+self.board[3]+" | "+self.board[4]+" | "+self.board[5]+"\n"+brek
		line3 ="\n\t  "+self.board[6]+" | "+self.board[7]+" | "+self.board[8]+"\n"
		draw = line1+line2+line3
		print(self.board)
		print(draw)


	def play(self):
		# Will change the board according to players choice
		# In short, will run the game.
		win_status = 0
		place = 0
		while True:
			# First step; putting the board on the screen
			self.draw()
			# Second Step; Asking for place to place the symbol.
			while True:
				try:
					place = int(input(self.player1+":"))
					if place < 1 or place > 9:
						print("Please Enter something in between 1 and 9.")
						continue
				except:
					print("Please enter a valid number.")
					continue
				else:
					place -= 1 
					if isNum(self.board[place]):
						self.board[place] = "x"
					else:
						print("Position is already taken.")
						continue

					self.draw()
					win_status = self.check()
					break

			# End of player Loop; decision is made; now announce
			self.draw()
			if win_status == 1:
				print(self.player1+" You win! ")
				ack = input("Wanna play again(y/n):").lower()
				if ack == "y":
					self.Reset()
					continue
				else:
					break
			elif win_status == 2:
				print(self.player2+" You win! ")
				ack = input("Wanna play again(y/n):").lower()
				if ack == "y":
					self.Reset()
					continue
			elif win_status == 4:
				print("It's a draw...")
				ack = input("Wanna play again(y/n):").lower()
				if ack == "y":
					self.Reset()
					continue
				else:
					break

			while True:
				try:
					place = int(input(self.player2+":"))
					if place < 1 or place > 9:
						print("Please Enter something in between 1 and 9.")
						continue
				except:
					print("Please enter a valid number.")
					continue
				else:
					place -= 1 
					if isNum(self.board[place]):
						self.board[place] = "o"
					else:
						print("Position is already taken.")
						continue

					self.draw()
					win_status = self.check()
					break
			# End of main Loop; decision is made; now announce
			self.draw()
			if win_status == 1:
				print(self.player1+" You win! ")
				ack = input("Wanna play again(y/n):").lower()
				if ack == "y":
					self.Reset()
					continue
				else:
					break
			elif win_status == 2:
				print(self.player2+" You win! ")
				ack = input("Wanna play again(y/n):").lower()
				if ack == "y":
					self.Reset()
					continue
			elif win_status == 4:
				print("It's a draw...")
				ack = input("Wanna play again(y/n):").lower()
				if ack == "y":
					self.Reset()
					continue
				else:
					break
		del self

	def __del__(self):
		os.system("clear")


#### PROGRAM TO RUN ####
if __name__ == "__main__":
	game = main()

	start = """Rules to play:
    Just tell your name and give the number where you want to put your x or o.
    Note: o is 'o' not zero."""
	print(start)
	game.play()