class testing():
	def __init__(self):
		self.a=0
		self.b=1
		self.c=[]

	def test(self):              #------i think this is the code to calculate bowling score
		permi=input("give permi to run (y/n):")
		if permi == "y":
			for i in range(self.a,self.b):
				print(f"new val{self.a},{self.b}")
				self.c.append(self.a+self.b)#-----we will do some adjustments HERE
				print(self.c)
				self.a+=1
				self.b+=1
			self.test()

m = testing()
m.test()