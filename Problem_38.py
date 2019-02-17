#38. Count and Say
def countAndSay(n):
    lis1 = ['1', '11']
    while n > 3:
        strNumber = lis1[-1]
        newStr = strNumber + strNumber[-1]
        lis2 = []
        front = 0
        rear = 1
        for i in range(len(strNumber)):
            if newStr[i+1] == newStr[i]:
                rear += 1
            else:
                lis2.append(newStr[front, rear])
                front = rear
                rear += 1




