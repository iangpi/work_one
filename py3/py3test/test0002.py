class Test():
	def myadd(self,a,b):
		self.a=a
		self.b=b
		return a+b
if __name__=='__main__':
	res=Test()
	a=res.myadd(1,2)
	print (a)