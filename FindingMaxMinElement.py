def findNMax(a,n):
    #Technique 1:
    #Sort then pull element len(a) - n

    #a.sort()
    #return(a[len(a) - n]);

    #Technique 2:
    checkVal = a[0]






def findMax(a):


    try:
        maxVal = a[0]


        for i in range(1,len(list),1):

            maxVal = max(maxVal,a[i])


        return maxVal
    except IndexError:
        return "Invalid List"


list = [100,4,3,2,54,23,22,23,99]
val = findNMax(list,2)

print(val)

val = findMax("monkey")
print(val)

