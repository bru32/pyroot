# Newton-Raphson method (needs the slope function).

from utils import eps


def fsolve(f, df, x, args=(), tol=1e-6, maxi=24):
  for i in range(maxi):
    xo = x
    fx = f(x, *args)
    dfx = df(x, *args)
    if abs(dfx) <= eps:
      raise Exception("Curve too flat!")
    x -= fx / dfx
    if abs(x - xo) < tol * (1.0 + abs(x)):
      return x
  raise Exception("Max its reached!")
