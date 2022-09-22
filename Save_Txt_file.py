import method_1.Program as pr
m = ''
f = open(r'C:\Users\amirm\OneDrive\Рабочий стол\Project\chisla.txt','w')
for ch in pr.mas:
    for ch2 in ch:
        f.write(str(ch2) + "\n")
    m = ''
f.close()