wg_lb=[]
wg_kgs=[]
cfactor=0.453492
i=1
N=int(input("number of students:\n"))
while i<= N:
    x=int(input('weight of the student:\n'))
    wg_lb.append(x)
    i=i+1
for i in wg_lb:
    wg_kgs.append(i*cfactor)
print(wg_kgs)
