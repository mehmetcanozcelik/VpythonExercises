import math

f= open("leibiniz2.txt", "w")
def leibiniz(n):

    sum =0
    j = 0
    for i in range(n):
        calc = (-1)** i / (2*i+1)
        sum = sum + calc
        if(i<100 or i==999 or i==9999 or i==99999 or i==999999 or i==9999999):
            j=j+1
            f.write(str(i+1) + ")" + str(sum*4) + " , " + str((sum*4)/math.pi) + " " + "\n")

leibiniz(10000000)

f.close()
