

def calc(word):

    a = [['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']]

    chars = list(word)
    l = len(chars)%2
    if l == 1:
        chars.append('X')
    print(chars)

    result = ""

    for i in range(0, len(chars),2):
        print(i,chars[i],chars[i+1])
        if chars[i] == ' ' or chars[i+1] == ' ':
            result+= chars[i]+chars[i+1]
        else:
            p1_x = -1
            p1_y = -1
            p2_x = -1
            p2_y = -1
            for x in range(0,4):
                for y in range(0,4):
                    if chars[i] == a[x][y]:
                        p1_x = x
                        p1_y = y
            for x in range(0,4):
                for y in range(0,4):
                    if chars[i+1] == a[x][y]:
                        p2_x = x
                        p2_y = y
            print(p1_x,p1_y,p2_x,p2_y)
            if p1_x == -1 or p1_y == -1 or p2_x == -1 or p2_y == -1:
                result += chars[i] + chars[i + 1]
                continue
            elif p1_x == p2_x:
                p1_y = (p1_y+1)%4
                p2_y = (p2_y + 1) % 4
                result += a[p2_x][p1_y]
                result+= a[p1_x][p2_y]


            elif p1_y == p2_y:
                p1_x = (p1_x+1)%4
                p2_x = (p2_x + 1) % 4
                result += a[p2_x][p1_y]
                result+= a[p1_x][p2_y]

            else:
                result += a[p2_x][p1_y]
                result+= a[p1_x][p2_y]



    return result

