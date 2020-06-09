import sys 
sys.setrecursionlimit(10**6) 
def getInput():
    input()
    menu = [int(i) for i in input().split(' ')]
    input()
    orders = [int(i) for i in input().split(' ')]
    return menu, orders

def combinationSum(candidates, target):
  result = []
  unique={}
  candidates = list(set(candidates))
  solve(candidates,target,result,unique)
  return result
def solve(candidates,target,result,unique,i = 0,current=[]):
    if target == 0:
        temp = [i for i in current]
        temp1 = temp
        temp.sort()
        temp = tuple(temp)
        if temp not in unique:
            unique[temp] = 1
            result.append(temp1)
        return
    if target <0:
        return
    for x in range(i,len(candidates)):
        current.append(candidates[x])
        solve(candidates,target-candidates[x],result,unique,i,current)
        current.pop(len(current)-1)
    return

def listUtil(menu,listInput):
    for item in listInput:
        print(menu.index(item)+1, end = ' ')
    print()
    return
    
def main():
    menu, orders = getInput()
    for order in orders:
        temp = combinationSum(menu, order)
        if len(temp)>1:
            print('Ambiguous')
        elif len(temp)==1:
            listUtil(menu, temp[0])
        else:
            print('Impossible')
    return
main()