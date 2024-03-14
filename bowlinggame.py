import random

class Bowlinggame():
	def __init__(self):
		self.player1 = ""
		self.score = []
		self.finalscore = 0
		self.frames = 10
		self.a = 0
		self.round=1

	def playername(self):
		self.player1 = input("***Enter Your Name*** : ").capitalize()
		print(f" :-) Welcome In Game {self.player1}")

	def throwball(self):
		permission = input(f"---- Round {self.round} ---- (Frames Left => {self.frames}) (y/n) : ")
		if permission == "y":
			self.frames-=1
			t1p = input("Throw 1st Ball (y/n) : ")
			t2p = input("Throw 2st Ball (y/n) : ")
			ftr = random.randint(0,10) if t1p == "y" else exit()
			ft = 10-ftr
			st = random.randint(0,ft) if t1p == "y" else exit()
			total = ftr+st
			self.round+=1
			if len(self.score) == 0:
				self.score.append(total)
				print(f"1st Throw-{ftr}|",f"2nd Throw-{st}", f"-->total {total}")
				self.checkscore()
			if len(self.score) >= 1:
					if total == 0:
						self.score.append(0)
					else:
							self.score.append(self.score[self.a]+total)
							self.a+=1
			print(f"1st Throw - {ftr}|",f"2nd Throw - {st}", f"--> Total {total}")
			self.checkscore()
		if permission == "n":
			print(" ** Thank You Have A Good Day...Bye Bye ** ")
			exit()
		else:
			print("Invalid Input Try Again :-(")
			self.throwball()

	def checkscore(self):
		if len(self.score) == 10:
			self.finalscore = sum(self.score)
			print(self.score)
			print(f" Your Final Score Is =>  {self.finalscore} ")
			print(" ** Thanks For Playing ** ")
			exit()
		else:
			print(f"ScOrE BoArD -> {self.score}")
			self.throwball()


a = Bowlinggame()
a.playername()
a.throwball()
a.checkscore()