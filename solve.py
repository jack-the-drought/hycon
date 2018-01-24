from utils import blocksum

if __name__ == "__main__":
    total = 0
    for k in range(0, 5):
      for l in range(0, 5):
        if (k + l > 4):
          continue
        total += blocksum(k, l)
    total = total * 4
    print "the number of points john can access while making his map is : {}"\
            .format(total)
