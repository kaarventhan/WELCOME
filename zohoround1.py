text = input()
length = len(text)
mid = length // 2
outlen = 1
end = 0
for i in range(0,length):
    space = length - i
    tempmid = mid
    templen = outlen
    for j in range(0,space):
        print("",end = " ")
    if(end == 0):
        while(templen > 0):
            print(text[tempmid],end = "")
            templen -= 1
            tempmid +=1
            if(tempmid == length):
                tempmid = 0
        if(mid != length-1):
            tempmid +=1
        else:
            tempmid = 0
            end = 1
    print()
    outlen += 1

