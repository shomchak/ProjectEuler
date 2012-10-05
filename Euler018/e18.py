# Works from the bottom up.

def getTriangle(file_name):
    f = open(file_name)
    triangle = f.readlines()
    f.close()
    triangle = [line.split() for line in triangle]
    for line in triangle:
        for i in range(0,len(line)):
            line[i] = int(line[i])
    return triangle

def maxPath(triangle):
    N = len(triangle)-2
    while(N >= 0):
        for i in range(0,len(triangle[N])):
            n = triangle[N][i]
            left = triangle[N+1][i]
            right = triangle[N+1][i+1]
            if(left<=right):
                triangle[N][i] = right + n
            else:
                triangle[N][i] = left + n
        N -= 1
    print triangle[0][0]

maxPath(getTriangle('triangle18.txt'))

