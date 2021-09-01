# Aitken's del squared process (from Lawrence Atkinson).

from utils import SQR


def fixpoint(f, x, args=(), tol=1e-6, maxi=48):
  delta = 1e-4
  i, j = 0, 0
  hist = [x, 0.0, 0.0]
  while 1:
    if abs(hist[j]) <= delta:
      return x
    xo = hist[j]
    i += 1
    if i > maxi:
      raise Exception('Max its reached!')
    j = i % 3
    if j == 0:
      hist[0] -= SQR(hist[1] - hist[0]) / (hist[2] - 2.0 * hist[1] + hist[0])
    else:
      hist[j] = f(hist[j-1], *args)
    x = hist[j]
    if abs((xo - hist[j]) / hist[j]) <= tol:
      return x
