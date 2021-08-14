for i in range(1,4):
    for j in range(1,4):
        if j==i:
            continue
        # print(j,end="")
        for k in range(1,4):
            if k==j or k==i:
                continue
            print(i,j,k)
