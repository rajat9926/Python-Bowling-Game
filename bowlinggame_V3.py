class BowlingGame():
	def __init__(self):
		self.frames = 1
		self.Ball_1 = 0
		self.Ball_2 = 0
		self.Total = 0
		self.Strike_Ball_1_Count = 0
		self.Strike_On_Total_Count = 0
		self.ScoreBoard = [0]
		self.Index_val = 0
		self.Pins_Left = 10



	def ThrowBall(self):
		try:
			if self.Index_val == 9:
				self.Frame_10()
			self.Ball_1 = int(input(f"Throw First Ball -> (Pins Left : {self.Pins_Left}): "))

	# ----- INPUT CHECK START -------
			if self.Ball_1 > 10 or self.Ball_1 < 0:
				print(" Invalid Input Try Again")
				self.ThrowBall()
			self.Pins_Left = 10-self.Ball_1
	# ----- INPUT CHECK END -------

			if self.Ball_1 < 10:
				self.Ball_2 = int(input(f"Throw Second Ball -> (Pins Left : {self.Pins_Left}): "))

	# ----- INPUT CHECK START -------
				if self.Ball_2 <= self.Pins_Left and self.Ball_2 >= 0:
					self.Total = self.Ball_1+self.Ball_2
				else:
					print(" Invalid Input Try Again ")
					self.Pins_Left = 10
					self.ThrowBall()
			self.Pins_Left = 10
	# ----- INPUT CHECK END -------
			
			self.Check()
		except(ValueError) as e:
			print(e,"Try Again")
			self.ThrowBall()




	def Check(self):
		if len(self.ScoreBoard) == 11:
			self.ScoreBoard.pop(0)
			print(self.ScoreBoard)
			print(f"Your Final Score Is {self.ScoreBoard[9]} Out Of 300")
			exit()
		if self.Ball_1 == 10:
			self.Strike_On_Ball_1_Func()
		if self.Total == 10:
			self.Strike_On_Total_Func()
		if self.Total < 10:
			self.No_Strike_Func(self.Total)
			
		


	def No_Strike_Func(self,Total):
		# print("no strike func")
		if self.Strike_Ball_1_Count == 1:
			self.Strike_Ball_1_Count-=1
			self.ScoreBoard.append(self.ScoreBoard[self.Index_val]+self.Total+10)
			self.Index_val+=1
		self.CheckScore(Total)




	def Strike_On_Total_Func(self):
		if self.Strike_Ball_1_Count == 1:
			self.Strike_Ball_1_Count-=1
			self.ScoreBoard.append(self.ScoreBoard[self.Index_val]+self.Total+10)
			self.Index_val+=1
		print("Strike on Total")
		try:
			self.Ball_1 = int(input(f"Throw First Ball -> (Pins Left : {self.Pins_Left}): "))

	# ----- INPUT CHECK START -------
			if self.Ball_1 > 10 or self.Ball_1 < 0:
				print(" Invalid Input Try Again")
				self.Strike_On_Total_Func()
	# ----- INPUT CHECK END-------
				
			self.ScoreBoard.append(self.ScoreBoard[self.Index_val]+self.Ball_1+10)
			self.Index_val+=1
			print(self.ScoreBoard)
			if self.Ball_1 == 10:
				self.Ball_2 = 0
				self.Total = 10
				self.Check()
			self.Ball_2 = int(input("Throw Second Ball : "))
			self.Total = self.Ball_1 + self.Ball_2
			self.Check()
		except(ValueError) as e:
			print(e,"Try Again")
			self.Strike_On_Total_Func()




	def Strike_On_Ball_1_Func(self):
		self.Total = 10
		print("strike on ball 1")
		self.Strike_Ball_1_Count+=1
		try:
			if self.Ball_1 < 10:
				self.Ball_2 = int(input("Throw Second Ball : "))
				self.Total = self.Ball_1+self.Ball_2
				self.Check()
			if self.Strike_Ball_1_Count == 2:
				self.Ball_1 = int(input(f"Throw First Ball -> (Pins Left : {self.Pins_Left}): "))
				self.ScoreBoard.append(self.ScoreBoard[self.Index_val]+self.Ball_1+10+10)
				self.Index_val+=1
				self.Strike_Ball_1_Count-=1
				print(self.ScoreBoard)
				if self.Ball_1 < 10:
					self.Ball_2 = int(input("Throw Second Ball : "))
					self.Total = self.Ball_1+self.Ball_2
					self.Check()
				self.Check()
			self.ThrowBall()
		except(ValueError) as e:
			print(e,"Try Again")
			self.Strike_On_Ball_1_Func()



	def CheckScore(self,value):
		self.ScoreBoard.append(self.ScoreBoard[self.Index_val]+value)
		self.Index_val+=1
		print(self.ScoreBoard)
		# print("Current Index Value : " , self.Index_val)
		self.ThrowBall()


	def Frame_Inc(self):
		print("Frame : ",self.frames)
		self.frames+=1
		return
	
	def Frame_10(self):
		try:
			self.Ball_1 = int(input(f"Throw First Ball -> (Pins Left : {self.Pins_Left}): "))
			self.Ball_2 = int(input("Throw Second Ball : "))
			total =self.Ball_1+self.Ball_2
			if self.Total == 10:
				self.ScoreBoard.append(self.ScoreBoard[self.Index_val]+10+total)
				self.Index_val+=1
				print(self.ScoreBoard)
			self.Ball_3 = int(input("Throw Ball Three You Have 10 More Pins: "))
			self.ScoreBoard.append(self.ScoreBoard[self.Index_val]+self.Ball_3+total)
			self.Check()
		except(ValueError) as e:
			print(e,"Try Again")
			self.Frame_10()
			

obj = BowlingGame()
obj.ThrowBall()