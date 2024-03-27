import random

class Bowlinggame():
	def __init__(self):
		self.player1 = ""
		self.score = []
		self.finalscore = 0
		self.frames = 10
		self.a = 0
		self.round = 1
		self.trdball= 0
		self.total = 0 + self.trdball
		self.allpinsdown = 0
		self.strike3 = False

	def playername(self):
		self.player1 = input("***Enter Your Name*** : ").capitalize()
		print(f" :-) Welcome In Game {self.player1}")

	def throwball(self):
		permission = input(f"---- Round {self.round} ---- (Frames Left => {self.frames}) (y/n) : ")
		if permission == "y":
			try:
				t1p = int(input("Throw 1st Ball (0 to 10) : "))
				if t1p <= 10:
					if self.strike3 == True:
						self.score.append(self.score[self.a] + 10 + t1p)
						self.a+=1
						self.strike3 = False
						self.round+=1
						self.frames-=1
						print(f" your previous score + 10 + {t1p}")
						self.checkscore()
					ftr = t1p
					ft = 10-ftr
					t2p = int(input(f"Throw 2st Ball (0 to {ft}) : ")) if ft != 0 else 0
					st = t2p  
					if t2p <= ft:
						self.total = ftr+st
						self.round+=1
						self.frames-=1
					else:
						print(" *** --- Please Give Correct Input. Try Again --- *** ")
						self.throwball()
				else:
					print("invalid input try again")
					self.throwball()
			except ValueError:
				print("invalid input. Please enter a number")
				self.throwball()

			if self.round == 11:
				try:
					self.trdball = int(input("Throw 3rd Ball (10 Pins) : "))
					if self.trdball <= 10 :
						self.score.append(self.score[self.a]+self.total+self.trdball)
						self.a+=1
						print(f"1st Throw - {ftr}|",f"2nd Throw - {st}|",f"3nd Throw - {self.trdball}", f"--> Total {self.total+self.trdball}")
						self.checkscore()
					else:
						print ("invalid input")
						self.throwball()
				except ValueError:
					print("invalid input")
					self.throwball()

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
						self.a+=1
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
			if len(self.score) == 0:
				print("  * * Congratulations Its A All Pin Down * *  ")
				tb = int(input("Throw 1st Ball (0 to 10) : "))
				fbr = tb if tb <= 10 else self.all_pin_down()
				print(f"Your First Ball Score Is --> {fbr} ")
				self.score.append(fbr+self.allpinsdown)
				self.checkscore()
			else:
				print("  * * Congratulations Its A All Pin Down * *  ")
				tb = int(input("Throw 1st Ball (0 to 10) : "))
				fbr = tb if tb <= 10 else self.all_pin_down()
				fb = 10-fbr
				if tb != 10:
					sb = int(input(f"Throw 2st Ball (0 to {fb}) : "))
					sbr = sb if sb <= fb else self.all_pin_down()
					tot = tb + sbr
				if tb == 10 or tot == 10:
					self.score.append(self.score[self.a] + 10 + 10 )
					print("10 + 10 + previous score")
					self.a+=1
					self.strike3 = True
					self.checkscore()
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