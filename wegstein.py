# Wegstein's fixed point method.


def fixpoint(f, a, args=(), tol=1e-5, maxi=48):
  b = a
  c = f(b, *args)
  g = c
  if c == a:
    return g
  d, b, e = a, c, c
  for i in range(maxi):
    c = f(b, *args)
    g = (d * c - b * e) / (c - e - b + d)
    if abs((g - b) / g) <= tol:
      return g
    e, d, b = c, b, g
  raise Exception("Max its reached!")
