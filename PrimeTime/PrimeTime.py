allPrimes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
allPrimeCount=95

def BinarySearch(num):
  left=0
  right=allPrimeCount-1
  mid = 0
  while(left<=right):
    if(allPrimes[left]==num or allPrimes[right]==num):
      return True
    mid=(left+right)//2
    if(allPrimes[mid]==num):
      return True
    elif(allPrimes[mid]<num):
      left=mid+1
    elif(allPrimes[mid]>num):
      right=mid-1
  return False
  
def checkRow(start,diff,p):
  start=start+diff
  for i in range(1,p):
    if(not BinarySearch(start)):
      return False
    start=start+diff
  return True
  
indexStart=[1]
D,p=map(int,input().split(" "))
diff=D//p
count=0
for i in allPrimes:
  if(i>diff):
    break
  if(checkRow(i,diff,p)):
    count+=1
print(count,end="")
