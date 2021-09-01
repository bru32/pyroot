# Secant root finder method (xo is a single starting guess).


def fsolve(f, xo, args=(), tol=1e-6, maxi=48):
  delta = 0.1
  fo = f(xo, *args)
  if abs(fo) <= tol:
    return xo
  h = xo * delta
  x = xo + h
  fx = f(x, *args)
  if abs(fx) > abs(fo):  # swap so that f(x) is closer to 0
    xo, x = x, xo
    fo, fx = fx, fo
  for i in range(maxi):
    dx = fx * (x - xo) / (fx - fo)
    if abs(dx) < tol * (1.0 + abs(x)):
      return x - dx
    xo, x = x, x-dx
    fo, fx = fx, f(x, *args)
  raise Exception("Max its reached!")
