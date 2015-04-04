class Person:
	def parse(self,line):
		fields=line.split('\t')
		self.name=fields[0]
		self.gender=fields[1]
		self.age=int(fields[2])
		self.favorite_language=fields[3]
		return self

	def __repr__(self):
		return "Person( %s, gender=%s, %d years old, likes %s)"%(self.name,self.gender,self.age,self.favorite_language)
