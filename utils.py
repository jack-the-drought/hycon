def digit_sum(n):
  return sum([int(c) for c in str(n)])

def visualize(str, newline=None):
    if newline:
        print str
    else:
        print str,

def nop(str, newline=None):
    pass

def decorated_sum(x, y, decorated=nop):
  step = (x + y) * 100
  # delta is the diagonal translation factor
  delta = 140 + step - (x+y) * 10
  k = 0
  # iterating over a block matrix of 100x100
  for i in range(x*100, (x+1)*100):
    for j in range(y*100, (y+1)*100):
      # we're safe
      if (digit_sum(i) + digit_sum(j)) <= 21:
        decorated("-")
        if ((j < -1 * i + delta)):
            # if the point is part of either of the x or y axis then it will only be duplicated for the final solution
            if i == 0 or j==0:
              k += 1/2
            else:
              k+=1

      # bomb found!!
      else:
        decorated("*")
    decorated("", True)
  # minus 1 to remove the initial position of (0, 0)
  return k - 1

def blocksum(x, y, vis=None):
  if vis:
      return decorated_sum(x, y, visualize)
  return decorated_sum(x, y)
