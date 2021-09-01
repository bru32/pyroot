# Modified Regula-Falsi (False Position method).


def fsolve(f, x, args=(), tol=1e-5, maxi=48):
  if len(x) != 2:
    raise Exception('Need teo guesses!')
  a, b = x
  fa = f(a, *args)
  fb = f(b, *args)
  if fa * fb >= 0.0:
    raise Exception('No bracket!')
  if fb < 0.0:
    a, b = b, a
    fa, fb = fb, fa
  for i in range(maxi):
    c = (a * fb - b * fa) / (fb - fa)
    fc = f(c, *args)
    if fa * fc < 0.0:
      k = abs(2 * fc / (b - c))
      d = ((1 + k) * a * fb - b * fa) / ((1 + k) * fb - fa)
      fd = f(d, *args)
      if fd * fa < 0.0:
        b = d
      else:
        b = c
        a = d
    elif fa * fc > 0.0:
      k = abs(0.5 * fc / (b - c))
      d = ((1 + k) * b * fa - a * fb) / ((1 + k) * fa - fb)
      fd = f(d, *args)
      if fd * fa > 0:
        a = d
      else:
        a = c
        b = d
    if abs(fd) <= tol:
      return d
  raise Exception('Max its reached')
