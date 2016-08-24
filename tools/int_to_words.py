ones = ["", "one ","two ","three ","four ", "five ",
    "six ","seven ","eight ","nine "]

tens = ["ten ","eleven ","twelve ","thirteen ", "fourteen ",
    "fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]

twenties = ["","","twenty ","thirty ","forty ",
    "fifty ","sixty ","seventy ","eighty ","ninety "]

thousands = ["","thousand "]

def int2word(n):
    groups = []
    ns = str(n)

    for k in range(3, 33, 3):
        r = ns[-k:]
        q = len(ns) - k

        if q < -2:
            break
        else:
            if  q >= 0:
                groups.append(int(r[:3]))
            elif q >= -1:
                groups.append(int(r[:2]))
            elif q >= -2:
                groups.append(int(r[:1]))

    nw = ""
    for i, x in enumerate(groups):
        b1 = x % 10
        b2 = (x % 100)//10
        b3 = (x % 1000)//100

        if x == 0:
            continue
        else:
            t = thousands[i]

        if b2 == 0:
            nw = ones[b1] + t + nw
        elif b2 == 1:
            nw = tens[b1] + t + nw
        elif b2 > 1:
            nw = twenties[b2] + ones[b1] + t + nw
        if b3 > 0:
            if b1 > 0 or b2 > 0:
                nw = ones[b3] + "hundred and " + nw
            else:
                nw = ones[b3] + "hundred " + nw
    return nw.strip()
