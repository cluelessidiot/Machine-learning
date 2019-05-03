def dictionary():
	print("1")
	ab={'a':'z','b':'x','c':'y','aathil':'nasi'}
	print("aathil is ",ab['aathil'])
	print("there are {} elements in dictionary and {} crosses to {}".format(len(ab),"aathil",ab['aathil']))
	print(ab.keys())
	l=list(ab.keys())
	#listing keys......
	for i in range(len(l)):
	   print(l[i])
	if 'aathil'not in l:
	   print('yaaay')
	q=set(['aathil','3'])
	print(l& q)      
if __name__=='__main__':
	dictionary()	
