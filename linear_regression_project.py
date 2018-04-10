I=[[1,2,3,4],
   [2,3,4,5],
   [3,4,5,6],
   [4,5,6,7]]

def shape(M):
    return len(M),len(M[0]);

def matxRound(M,decPts=4):
    for i in range(0,len(M)):
        for j in range(0,len(M[i])):
            M[i][j]=round(M[i][j],decPts);


def transpose(M):
    pair=shape(M)
    grid=[[0*pair[1]]*[pair[0]]]
    for i in range(0,pair[0]):
        for j in range(0,pair[1]):
            grid[j][i]=pair[i][j]
    return grid
  
def matxMultiply(A,B):
    if(len(A[0])!=len(B)):
        return None
    multiplyLen=len(B);
    column=len(B[0])
    row=len(A)
    grid=[[0 for i in range(column)] for i in range(row)]
    for i in range(0,row):
        for j in range(0,column):
            res=0
            for k in range(0,multiplyLen):
                res+=A[i][k]*B[k][j]
            grid[i][j]=res;
    return grid;

def augmentMatrix(A,b):
    column=len(A[0])+1
    row=len(A)
    grid=[[0 for i in range(column)] for i in range(row)]
    for i in range(0,row):
        grid[i]=A[i][:]+b[i]
    return grid

def swapRows(M,r1,r2):
    temp=M[r1]
    M[r1]=M[r2]
    M[r2]=temp

def scaleRow(M,r,scale):
    if(scale==0):
        raise ValueError('illegal value')
        return None
    for i in range(0,len(M[r])):
        M[r][i]=scale*M[r][i]

def addScaledRow(M,r1,r2,scale):
    for i in range(0,len(M[r1])):
        M[r1][i]=M[r2][i]*scale+M[r1][i]

def gj_Solve(A, b, decPts=4, epsilon = 1.0e-16):
    n=len(A)
    M=augmentMatrix(A,b)
    print(A)
    print(b)
    #adjust order
    for k in range(n):
        for i in range(k,n):
            #find min m(_,k),switch it to m[k]
            if abs(M[i][k])>abs(M[k][k]):
                M[k],M[i]=M[i],M[k]
            else:
                pass

        for j in range(k+1,n):
            #eliminate all M[J][_]
            q=float(M[j][k])/M[k][k]
            for m in range(k,n+1):
                M[j][m]-=q*M[k][m]
    #check rank
    rank=0
    for i in range(n):
        rowCount=0
        for j in range(n):
            if abs(M[i][j])>epsilon:
                rowCount=1
                break
        rank+=rowCount
    if rank<n:
        return None
    x=[0 for i in range(n)]
    x[n-1]=float(M[n-1][n])/M[n-1][n-1]
    for i in range(n-1,-1,-1):
        z=0
        for j in range(i+1,n):
            z=z+float(M[i][j]*x[j])
        x[i]=float(M[i][n]-z)/M[i][i]
    res=[[x[i]] for i in range(n)];
    matxRound(res);
    return res



def linearRegression(points):
    X=[[points[i][0],1] for i in range(len(points))]
    Y=[points[i][1] for i in range(len(points))]
    XT=[[points[i][0] for i in range(len(points))],[1 for i in range(len(points))]]
    XXT=matxMultiply(X,XT)
    XTY=matxMultiply(XT,Y)
    gj_Solve(XXT,XTY)
    return 0,0