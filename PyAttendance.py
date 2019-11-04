def presents(a, d, p, t):
    s = 0
    while p < t:
        p = round((a / d) * 100, 2)
        a += 1
        d += 1
        s += 1
    return s

def absents(a, d, p, t):
    s = 0
    while p > t:
        p = round((a / d) * 100, 2)
        d += 1
        s += 1
    return s

a = int(input("Attended : "))
d = int(input("Delivered : "))
p = round((a / d) * 100, 2)

print("\nCurrent Percentage : " + str(p) + " %\n")

if p >= 90 :
    print("Attend " + str(absents(a,d,p,90)) + " Classes To Remain Above 90%")
    print("Attend " + str(absents(a,d,p,75)) + " Classes To Remain Above 75%")

elif p >= 75 :
    print("Attend " + str(absents(a,d,p,75)) + " Classes To Remain Above 75%")
    print("Attend " + str(presents(a,d,p,90)) + " Classes To Attain 90%")

else :
    print("Attend " + str(presents(a,d,p,75)) + " Classes To Attain 75%")
    print("Attend " + str(presents(a,d,p,90)) + " Classes To Attain 90%")
