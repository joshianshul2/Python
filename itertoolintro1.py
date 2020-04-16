from itertools import combinations
def subset(arr,a):
  return (list(combinations(arr,r)))


if __name__=="__main__":
 arr=[1,2,3,4,5]
 r=3
 print(subset(arr,r))
