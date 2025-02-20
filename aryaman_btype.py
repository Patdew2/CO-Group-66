def binary(number):
    if number >= 0:
        binary = ""
        while number > 0:
            binary = str(number % 2) + binary
            number = number // 2

        binary = binary.zfill(12)
    else:
        max_value = 1 << 12
        positive_number = max_value + number
        binary = ""
        while positive_number > 0:
            binary = str(positive_number % 2) + binary
            positive_number = positive_number // 2
        binary = binary.zfill(12)
    
    return binary

def btype(x):
    enc = 0
    defi = 0
    op = "1100011"
    f = ["000",'001','100']
    inst = list(x.split())

    if inst[0] == "beq":
        x,y,z = inst[1].split(',')
        if x==y=='zero':
                reg1 = registers["zero"]
                reg2 = registers["zero"]
        else:
            for i in registers:
                if i==x:
                    reg2 = registers[x]
                elif i==y:
                    reg1 = registers[y]

        if z.isdigit():
            imm = binary(int(z))
        elif "-" in z:
            imm = binary(int(z[1:])*-1)
        elif z in registers:
            cat = registers[z]
            imm = cat.zfill(12)
        else:
            if z.strip() in labels.keys():
                for i in linenum.keys():
                    if z in i[:10]:
                        g = linenum[i]
                    elif z in i[10:]:
                        h = linenum[i]
            else:
                with open("testcase.txt",'r') as f2:
                    for line in f2:
                        if z in line[:10]:
                           star = line.strip()
                           g = linenum[star]
                        elif z in line[10:]:
                            star = line.strip()
                            h = linenum[star]
            imm = binary((g-h)*4)
        final = imm[0] + imm[2:8] + reg1 + reg2 + f[0] + imm[7:11] + imm[1] + op
        return final
        
    elif inst[0] == "bne":
        a,b,c = inst[1].split(',')
        for j in registers:
            if j==a:
                reg2 = registers[a]
            elif j==b:
                reg1 = registers[b]
        if c.isdigit():
            imm = binary(int(c))
        elif "-" in c:
            imm = binary(int(c[1:])*-1)
        elif c in registers:
            cat = registers[c]
            imm = cat.zfill(12)
        else:
            if c.strip() in labels.keys():
                for i in linenum.keys():
                    if c in i[:10]:
                        g = linenum[i]
                    elif c in i[10:]:
                        h = linenum[i]
            else:
                with open("testcase.txt",'r') as f2:
                    for line in f2:
                        if c in line[:10]:
                           star = line.strip()
                           g = linenum[star]
                        elif c in line[10:]:
                            star = line.strip()
                            h = linenum[star]
            imm = binary((g-h)*4)
        final = imm[0] + imm[2:8] + reg1 + reg2 + f[1] + imm[7:11] + imm[1] + op
        return final

    elif inst[0] == "blt":
        p,q,r = inst[1].split(',')
        for k in registers:
            if k==p:
                reg2 = registers[p]
            elif k==q:
                reg1 = registers[q]
        if r.isdigit():
            imm = binary(int(r))
        elif "-" in r:
            imm = binary(int(r[1:])*-1)
        elif r in registers:
            cat = registers[r]
            imm = cat.zfill(12)
        else:
            if r.strip() in labels.keys():
                for i in linenum.keys():
                    if r in i[:10]:
                        g = linenum[i]
                    elif r in i[10:]:
                        h = linenum[i]
            else:
                with open("testcase.txt",'r') as f2:
                    for line in f2:
                        if r in line[:10]:
                           star = line.strip()
                           g = linenum[star]
                        elif r in line[10:]:
                            star = line.strip()
                            h = linenum[star]
                imm = binary((g-h)*4)
        final = imm[0] + imm[2:8] + reg1 + reg2 + f[2] + imm[7:11] + imm[1] + op
        return final

registers = {"zero": "00000", "ra": "00001", "sp": "00010", "gp": "00011", "tp": "00100", "t0": "00101", "t1": "00110",
             "t2": "00111", "s0": "01000", "s1": "01001", "a0": "01010", "a1": "01011", "a2": "01100", "a3": "01101",
             "a4": "01110", "a5": "01111", "a6": "10000", "a7": "10001", "s2": "10010", "s3": "10011", "s4": "10100",
             "s5": "10101", "s6": "10110", "s7": "10111", "s8": "11000", "s9": "11001", "s10": "11010", "s11": "11011",
             "t3": "11100", "t4": "11101", "t5": "11110", "t6": "11111"}
labels = {}
linenum = {}

file = open('testcase.txt','r')
k = 1
for j in file.readlines():
    linenum[j.strip()] = k
    k+=1
file.close()
