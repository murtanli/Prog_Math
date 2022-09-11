import Program as pr
m = ''
f = open(r'C:\Users\amirm\OneDrive\Рабочий стол\Project\chisla.txt','w')
f.write('x    |    y|' + "\n")
for ch in pr.mas:
    for ch2 in ch:
        if float(ch2) >= 0.0:
            m = m + ch2 + ' |'
        else:
            m = m + ch2 + '|'
    f.write(str(m) + "\n")
    m = ''
    print(ch)
f.close()