import random

class Bowlinggame():
	def __init__(self):
		self.player1 = ""
		self.score = []
		self.finalscore = 0
		self.rolls = 10

	def playername(self):
		self.player1 = input("Enter Your Name : ").capitalize()
		print(f"Welcome in Game {self.player1}")

	def throwball(self):
		permission = input(f"throw ball (Rolls Left {self.rolls}) (y/n) : ")
		if permission == "y":
			self.rolls-=1
			ft = random.randint(0,10)
			st = random.randint(0,ft)
			total = ft+st
			if len(self.score) == 0:
				self.score.append(total)
				self.checkscore()
			if len(self.score) >= 1:
				for i in range(0,1):
					self.score.append(sum(self.score)+total)
			print(f"1st Throw-{ft}|",f"2nd Throw-{st}", f"-->total {total}")
			self.checkscore()
		if permission == "n":
			print("Thank You Have A Good Day...Bye Bye")
			exit()
		else:
			print("Invalid Input Try Again")
			self.throwball()

	def checkscore(self):
		if len(self.score) == 10:
			self.finalscore = sum(self.score)
			print(self.score)
			print(f"Your Final Score Is {self.finalscore}")
			print("**Thanks For Playing**")
			exit()
		else:
			print(self.score)
			self.throwball()


a = Bowlinggame()
a.playername()
a.throwball()
a.checkscore()