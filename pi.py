from math import pi, e

def outer(num, denom, target, scale, iters):
	while (iters > 0):
		iters -= 1

		num *= scale
		denom *= scale
		
		num = improveNum(num, denom, target)
		denom = improveDenom(num, denom, target)
		# print ("New fraction is {0}/{1}".format(num,denom))
	# num, denom = reduceFrac(num, denom)
	print("{0}/{1} - {2} = {3}".format(num,denom,target,num/denom - target))
	return num, denom

def improveNum(num, denom, target):
	while num / denom >= target:
		num -= 1
	return num

def improveDenom(num, denom, target):
	while num / denom <= target:
		denom -= 1
	return denom

# def reduceFrac(num, denom):
# 	i = 2
# 	while i <= num and i <= denom:
# 		if num % i == 0 and denom % i == 0:
# 			num = num / i
# 			denom = denom / i
# 		i += 1
# 	return num, denom


num, denom = outer(1.,1.,pi,10.,10)
