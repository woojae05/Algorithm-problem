def getScore(alpa):
    dir={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0}
    return dir[alpa]


sumSchoolScore = 0
sumMajorScore = 0
for i in range(0, 20): 
    name,score,alpa = input().split(' ')
    if(alpa == "P"): 
        continue
    sumMajorScore+= float(score) * getScore(alpa)
    sumSchoolScore+= float(score)

print(round(sumMajorScore/sumSchoolScore,6))