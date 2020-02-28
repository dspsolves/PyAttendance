import sys
import json
import pyperclip

def main():
    global att
    try :
        att = json.loads(pyperclip.paste())
    except :
        print("Clipboard Contains Irrelevant Data")
        sys.exit()

def presents(a, d, p, t):
    s = 0
    while p < t:
        a += 1
        d += 1
        p = round((a / d) * 100, 2)
        s += 1
    return s

def absents(a, d, p, t):
    s = 0
    while True:
        d += 1
        p = round((a / d) * 100, 2)
        if p > t:
            s += 1
            continue
        else :
            break
    return s

if __name__ == '__main__' :
    main()

print("\nATTENDANCE CALCULATOR\n")

for sub in att['attendance'] :
    a = int(sub['Eligible Attended'])
    d = int(sub['Eligible Delivered'])
    p = float(sub['Eligible Percentage'])
    print(f"{sub['Title']} : {str(p)}%\n")

    if p >= 90 :
        print("- Can Leave " + str(absents(a,d,p,75)) + " Lectures And Still Remain Above 75%")
        print("- Can Leave " + str(absents(a,d,p,90)) + " Lectures And Still Remain Above 90%")

    elif p >= 75 :
        print("- Can Leave " + str(absents(a,d,p,75)) + " Lectures And Still Remain Above 75%")
        print("- Attend " + str(presents(a,d,p,90)) + " Lectures To Attain 90%")

    else :
        print("- Attend " + str(presents(a,d,p,75)) + " Lectures To Attain 75%")
        print("- Attend " + str(presents(a,d,p,90)) + " Lectures To Attain 90%")
    print()

