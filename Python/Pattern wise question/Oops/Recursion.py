class Test:
	def test(self):
		print("test")

	def test1(self , number):
		#self.test()
		#print("test 1")
		print(number)
		no = number
		print(no)
	def test3(self):
		#print(no)
		#NameError: name 'no' is not defined
		#print(self.no)
		#AttributeError: 'Test' object has no attribute 'no'
		t= self.test()
		n=self.test1(55)
		
	def rec(self , ele):
		if self.ele==0:
			return 1
		return self.ele*self.rec(ele-1)

t = Test()
t.test1(10)
t.test3()
t.rec(5)


