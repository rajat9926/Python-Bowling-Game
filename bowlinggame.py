import random

class Bowlinggame():
	def __init__(self):
		self.player1 = ""
		self.score = []
		self.finalscore = 0
		self.frames = 10
		self.a = 0
		self.round=1
		self.trdball= 0
		self.total = 0+self.trdball
		self.allpinsdown = 0

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
			st = random.randint(0,ft) if t2p == "y" else exit()
			self.total = ftr+st
			self.round+=1

			if self.round == 11:
				self.trdball = random.randint(0,10)
				self.score.append(self.score[self.a]+self.total+self.trdball)
				self.a+=1
				print(f"1st Throw - {ftr}|",f"2nd Throw - {st}|",f"3nd Throw - {self.trdball}", f"--> Total {self.total+self.trdball}")
				self.checkscore()

			if ftr == 10 or st == 10 or self.total == 10:
				self.allpinsdown = 10
				self.all_pin_down()

			if len(self.score) == 0:
				self.score.append(self.total)
				print(f"1st Throw-{ftr}|",f"2nd Throw-{st}", f"-->total {self.total}")
				self.checkscore()
			if len(self.score) >= 1:
					if self.total == 0:
						self.score.append(0)
					else:
						self.score.append(self.score[self.a]+self.total)
						self.a+=1
			print(f"1st Throw - {ftr}|",f"2nd Throw - {st}", f"--> Total {self.total}")
			self.checkscore()
		if permission == "n":
			print(" ** Thank You Have A Good Day...Bye Bye ** ")
			exit()
		else:
			print("Invalid Input Try Again :-(")
			self.throwball()

	def checkscore(self):
		if len(self.score) == 10:
			self.finalscore = self.score[self.a]
			print(self.score)
			print(f" Your Final Score Is =>  {self.finalscore} OUT OF 300")
			print(" ** Thanks For Playing ** ")
			exit()
		else:
			print(f"ScOrE BoArD -> {self.score}")
			self.throwball()

	def all_pin_down (self):
			print("  * * Congratulations Its A All Pin Down * *  ")
			tb = input("Throw 1st Ball (y/n) : ")
			sb = input("Throw 2st Ball (y/n) : ")
			fbr = random.randint(0,10) if tb == "y" else self.all_pin_down()
			fb = 10-fbr
			sbr = random.randint(0,fb) if sb == "y" else self.all_pin_down()
			print(f"Your First Ball Score Is --> {fbr} So WE Will Add {fbr} + 10 In Your Previous Score ")
			print(f"Your Second Ball Score Is --> {sbr} ")
			self.score.append(self.score[self.a]+fbr+self.allpinsdown)
			self.a+=1
			self.score.append(self.score[self.a]+fbr+sbr)
			self.a+=1
			self.frames-=1
			self.round+=1
			self.checkscore()

a = Bowlinggame()
a.playername()
a.throwball()
a.checkscore()