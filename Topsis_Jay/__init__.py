import math
import pandas as pd

def TOPSIS(Fn, W, I, Yu):
    try:
        F = pd.read_csv(Fn)
    except:
        print("******************    Can't read File ",
              Fn, " ***********************")
        exit(0)

    T = Fn.split('.csv')
    T = T[0]

    W = W.split(',')
    I = I.split(',')

    if not F.shape[1] >= 3:
        print("********* MIN 3 Columns Are requires **********")
        exit(0)

    if not F.shape[1]-1 == len(W) == len(I):
        print("********* Weights,Impacts,Columns are Not Equal *************")
        exit(0)

    Impacts = list(map(lambda x: x == "+" or x == "-", I))
    if not all(Impacts):
        print("Unknown Input in Impacts")
        exit(0)

    try:
        W = list(map(lambda x: float(x), W))
    except:
        print("Unknown Input in Weights")
        exit(0)

    N = list(F.columns)
    ER = 0

    for i in range(1, len(N)):
        G = F[pd.to_numeric(F[N[i]], errors='coerce').isnull()]
        ER += G.shape[0]
        for index in G.iterrows():
            F = F.drop(index)

    if not ER == 0:
        print("--------- CAUTION DUE TO NON NUMERIC ENTRIES -----------")
        print(T + ' - NON_Numeric Rows ', "--> ", ER)
        exit(0)

    Total = []

    for i in range(1, len(N)):
        T = 0
        for j in F[N[i]]:
            T += j*j
        T = math.sqrt(T)
        Total.append(T)

    E = 0
    Vp = []
    Vn = []
    cols = F.shape[1]
    rows = F.shape[0]

    arr = [[0 for i in range(cols-1)] for j in range(rows)]
    Final = [[0 for i in range(5)] for j in range(rows)]

    for z in range(rows):
        Final[z][4] = z

    for i in range(1, len(N)):
        max = -9999
        min = 10000
        t = 0
        for j in F[N[i]]:
            j /= Total[E]
            j *= W[E]
            arr[t][i-1] = j
            t += 1
            if max < j:
                max = j
            if min > j:
                min = j
        if I[E] == "+":
            Vp.append(max)
            Vn.append(min)
        else:
            Vn.append(max)
            Vp.append(min)
        E += 1

    for i in range(rows):
        Sp = 0
        Sn = 0
        for j in range(cols-1):
            Sp += (arr[i][j]-Vp[j])**2
            Sn += (arr[i][j]-Vn[j])**2

        Final[i][0] = math.sqrt(Sp)
        Final[i][1] = math.sqrt(Sn)
        Final[i][2] = Final[i][0] + Final[i][1]
        Final[i][3] = Final[i][1]/Final[i][2]

    sorted_list = sorted(Final, key=lambda x: x[3])

    TS = [None] * rows
    Ra = [None] * rows

    R = 1
    for i in range(rows-1, -1, -1):
        TS[sorted_list[i][4]] = sorted_list[i][3]
        Ra[sorted_list[i][4]] = R
        R += 1

    F['TOPSIS SCORE'] = TS
    F['RANK'] = Ra

    F.to_csv(Yu, index=False)
    print("Result File Saved as : ", Yu)

