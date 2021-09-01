# root finder utils

import sys
import math

eps = sys.float_info.epsilon


def MIN(a, b):
  if a < b:
    return a
  return b


def SQR(x):
  t = x
  return t * t


def SIGN(a, b):
  if b >= 0.0:
    return abs(a)
  return -abs(a)


def signum(a, b):
  "signed number"
  if b < 0.0:
    return -abs(a)
  return abs(a)


def iqf(a, c, b, fa, fc, fb):
  """inverse quadratic factor"""
  return fa*fc/(fb-fa)/(fb-fc) + (c-a)/(b-a)*fa*fb/(fc-fa)/(fc-fb)


def dydx(f, x, *args):
  """f(x) and df/dx"""
  e = 0.1
  xo = x
  fo = f(xo, *args)
  h = e * abs(xo)
  if h <= eps:
    h = e
  x = xo + h
  fx = f(x, *args)
  return fo, (fx-fo)/(x-xo)


def dydx2(f, x, *args):
  """f(x), df/dx and d2f/dx2 (2nd derivative)"""
  e = 0.01
  h = e * abs(x)
  if h <= eps:
    h = e
  fo, df = dydx(f, x, *args)
  df2 = (f(x+h, *args) - 2.0*fo + f(x-h, *args)) / h / h
  return fo, df, df2


def dxdy(f, x, *args):
  """f(x) and slope inverse dx/df"""
  e = 0.1
  xo = x
  fo = f(xo, *args)
  h = e * abs(xo)
  if h <= eps:
    h = e
  x = xo + h
  fx = f(x, *args)
  return fo, (x-xo)/(fx-fo)


def zbrac(f, x, args=()):
  """Given a range [x1,x2], Expand the range geometrically
     until a root is bracketed.  If successful, it returns
     the bracket tuple x1,x2.
     If not successful, return None
  """
  g = 1.6
  maxi = 12
  x1, x2 = x
  if x1 == x2:
    h = 0.1
    dx = h * x1
    if abs(dx) <= eps:
      dx = h
    x2 = x1 + dx
  f1 = f(x1, *args)
  f2 = f(x2, *args)
  for _ in range(maxi):
    if f1 * f2 < 0.0:
      return x1, x2
    dx = g * (x1 - x2)
    if abs(f1) < abs(f2):
      x1 += dx
      f1 = f(x1, *args)
    else:
      x2 -= dx
      f2 = f(x2, *args)
  return None


def autobrac(f, x, args=(), step=1.0):
  """Starting from a single guess x,
     expand the range geometrically until
     we bracket the root.
  """
  x0 = (x-eps, x+step)
  return zbrac(f, x0, *args)


def zbrak(f, x, n, args=()):
  """Take n steps over given range [x0,x1] with function f.
     If a root exists in step, add it to root bracket list rb.
  """
  rb = []  # root brackets
  dx = (x[1] - x[0]) / n
  a, fa = x[0], f(x[0], *args)
  for _ in range(n - 1):
    b = a + dx
    fb = f(b, *args)
    if fa * fb <= 0.0:
      rb.append((a, b))
    a, fa = b, fb
  return rb


def ConvRate(a):
  """Convergence Rate
     [a] is a list containing successive guesses in finding
     a root. There must be at least 3 values in the list for
     it to work.
  """
  result = []
  for i in range(2, len(a)):
    r = math.log(a[i] - a[i-1]) / math.log(a[i-1] - a[i-2])
    result.append(r)
  return result
