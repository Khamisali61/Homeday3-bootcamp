def find_missing(List1, List2):
    longerList = []
    shorterList = []
    if len(List1) > len(List2):
        longerList = List1
        shorterList = List2
    else:
        longerList = List2
        shorterList = List1
    extraNum = [x for x in longerList if x not in shorterList]
    if len(extraNum) == 0:
      return 0
    return extraNum.pop()
