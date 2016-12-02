input = open('input', 'r')

x,y,code = 2,1,''

def pad(x,y):
    return x+3*y

for line in input:
    for m in line:
        if m == 'U':
            y -= (y>0)*1
        elif m == 'D':
            y += (y<2)*1
        elif m == 'L':
            x -= (x>1)*1
        elif m == 'R':
            x += (x<3)*1
    code += str(pad(x,y))

print(code)
