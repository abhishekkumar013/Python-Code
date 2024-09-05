import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.array([[9,8,7],[6,5,4],[3,2,1]])
print("additon:\n",arr1+arr2)
print("substract:\n",arr1-arr2)
print("multiply:\n",arr1*arr2)
print("divide:\n",arr1/arr2)
print("matmul:\n",np.matmul(arr1,arr2)) 

print(arr1.reshape(9,1))  
print(arr1.reshape(1,9))  

