def search_p1(limite_p1, limite_p2, d1, d2):
    b = 2
    r = 2
    p1 = 1 - (1 - (1-d1)**r)**b
    for b in range(1, 60):
        for r in range(1,60):
            p1 = 1 - (1 - (1-d1)**r)**b
            p2 = 1 - (1 - (1-d2)**r)**b

            p1_m = 1 - (1 - (1-d1)**r+1)**b+1
            p2_m = 1 - (1 - (1-d2)**r+1)**b+1

            
            
            print("r = {}, b = {}".format(r,b))
            if (p1 >= limite_p1 and p2 <= limite_p2) and (p1_m < limite_p1 or p2_m > limite_p2):
                return r,b,p1,p2        



print(search_p1(0.88, 0.16, 0.2, 0.8))
