class Dice:
	def __init__(self,name,*listOfNumbers):
		"""Initializes the data."""
		self.name = name
		self.numbering = []
		for num in listOfNumbers:
			self.numbering.append(num)
		self.numbering.sort()
		print "Initialized the dice {}".format(self.numbering)

	@classmethod
	def prob_of_one_beat_another(cls,A,B):
		totalcases = len(A.numbering)*len(B.numbering)
		A_over_B = 0
		for num1 in A.numbering:
			for num2 in B.numbering:
				if(num1 > num2):
					A_over_B += 1
		return float(A_over_B)/totalcases
	
	@classmethod
	def prob_of_Win(cls,dice1,dice2,dice3):
		return cls.prob_of_one_beat_another(dice1,dice2)*0.5 \
		+ cls.prob_of_one_beat_another(dice1,dice3)*0.5




if __name__ == "__main__":
	a = Dice('1',3,5,6,9,15,18)
	b = Dice('2',2,4,8,13,14,16)
	c = Dice('3',1,7,10,11,12,17)
	print "The probability of Dice {} beat Dice {} is {}".format(a.name,b.name,Dice.prob_of_one_beat_another(a,b))
	print "The probability of Dice {} beat Dice {} is {}".format(b.name,c.name,Dice.prob_of_one_beat_another(b,c))
	print "The probability of Dice {} beat Dice {} is {}".format(c.name,a.name,Dice.prob_of_one_beat_another(c,a))

	print

	print "The probability to win by choosing Dice {} is {}".format(a.name,Dice.prob_of_Win(a,b,c))
	print "The probability to win by choosing Dice {} is {}".format(b.name,Dice.prob_of_Win(b,a,c))
	print "The probability to win by choosing Dice {} is {}".format(c.name,Dice.prob_of_Win(c,b,a))




