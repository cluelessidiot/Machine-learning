def mergersort(arr):
	l=len(arr)
	if len(arr)>1:
		mid=l//2	
		L=arr[:mid]
		R=arr[mid:]
		mergersort(L)
		mergersort(R)
		i=j=k=0
		while i<len(L) and j<len(R):
			if L[i]<R[j]:
				arr[k]=L[i]
				i=i+1
			else :
				arr[k]=R[j]	  
				j=j+1
				k=k+1
		while i<len(L):
			arr[k]=L[i]
			k=k+1
			i=i+1	  
		while j<len(R):
			arr[k]=R[j]
			k=k+1
			j=j+1
def printarray(arr):
	for i in range(len(arr)):
	   print(arr[i])
if __name__=='__main__':
  arr=[9,8,7,6,5,4,3,2,1]
  mergersort(arr)
  printarray(arr)
  	   			
