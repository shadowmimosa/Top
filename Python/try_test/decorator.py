def decorate(func):
	def iner(num):
		print("start ---")
		ret = func(num)
		print("return is ",ret)
	return iner
	
def glor(num):
	if num >5:
		return num
	else:
		return 0
 
glor = decorate(glor)
glor(4)
glor(8)