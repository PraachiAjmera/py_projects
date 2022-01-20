class fibo:
	def __init__(self):
		self.a=0
		self.b=1

	def printSeries(self,n):
		print(str(self.a)+" "+str(self.b),end=" ")
		for i in range(0,n-2):
			c=self.a+self.b
			print(c,end=" ")
			self.a=self.b
			self.b=c
	def printElementAt(self,pos):
		pass

if __name__ = '__main__':
	n=int(input('Enter size of series: '))
	obj=fibo()
	obj.printSeries(n)
	print("\n"+str(obj.a))