# Kiusalaas root find method (Brent type).
# Faster than NR and Wikipedia algorithm

from utils import eps


def fsolve(f, x, args=(), tol=1.0e-6, maxi=48):
  a, b = x
  x1, x2 = x
  f1 = f(x1, *args)
  if abs(f1) < tol:
    return x1
  f2 = f(x2, *args)
  if abs(f2) < tol:
    return x2
  if f1 * f2 > 0.0:
    raise Exception('No bracket!')
  x3 = 0.5 * (x1 + x2)
  for i in range(maxi):
    f3 = f(x3, *args)
    if abs(f3) < tol:
      return x3
    if f1 * f3 < 0.0:
      b = x3
    else:
      a = x3
    if (b - a) < tol * max(abs(b), 1.0):
      return 0.5*(a + b)

    P = x3*(f1 - f2)*(f2 - f3 + f1) + f2*x1*(f2 - f3) + f1*x2*(f3 - f1)
    Q = (f2 - f1)*(f3 - f1)*(f2 - f3)

    if abs(Q) < eps:
      dx = b - a
    else:
      dx = f3 * P/Q
    x = x3 + dx
    if (b - x)*(x - a) < 0.0:
      dx = 0.5*(b - a)
      x = a + dx
    if x < x3:
      x2 = x3
      f2 = f3
    else:
      x1 = x3
      f1 = f3
    x3 = x
  raise Exception('Max its reached!')
