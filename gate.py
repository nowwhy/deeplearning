import numpy as np

def AND(x1, x2): 
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
           
if __name__ == '__main__':
    for xs in [(0,0), (1,0), (0,1), (1,1)]
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
        
def NAND(x1, x2): # AND와 서로 반대 # weight, bias만 바꿔주면 적절하게 기능한다.
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
        
if __name__ == '__main__':
    for xs in [(0,0), (1,0), (0,1), (1,1)]
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
        
def OR(x1, x2): 
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2 #Threshold
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
        
if __name__ == '__main__':
    for xs in [(0,0), (1,0), (0,1), (1,1)]
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
        
# 퍼셉트론의 구조는 바뀌지 않고 weight와bais만 바꿔주면 된다.

def XOR(x1, x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    s3 = AND(x1,x2)
    return y
    
if __name__ == '__main__':
    for xs in [(0,0), (1,0), (0,1), (1,1)]
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))






























