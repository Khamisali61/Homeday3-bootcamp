class BinarySearch(list):

  def __init__(self, a, b):
    self.a = a
    self.b = b
         
    for i in range(self.a):
      list.append(self, self.b)
      self.b +=b
      i +=1
  
    self.length = i

  def search(self,value):
    firstvalue = 0
    lastvalue = self.length-1
    isfound = False
    count = 0
    in_list = False
    try:
      index = self.index(value)
      in_list = True
    except ValueError:
      index = -1
      in_list = False

    while firstvalue<=lastvalue and not isfound and in_list and value != self[lastvalue]:
        midpoint = (firstvalue+lastvalue)//2
        mid_value = self[midpoint]
        if mid_value == value:
            isfound = True
            count +=1
            index = midpoint
        else:
            if value < mid_value:
                lastvalue = midpoint - 1
                count +=1
            else:
                firstvalue = midpoint + 1
                count +=1
    
    
    return {"count": count, "index": index}
