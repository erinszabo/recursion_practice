

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]


if __name__ == '__main__':
    print("")
    print(listsum([1, 3, 5, 7, 9]))  # same as (1 + (3 + (5 + (7 + (9)))))
    print(toStr(1453, 16))  #

