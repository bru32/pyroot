# Damped Newton method (needs a separate slope function).


def fsolve(f, df, x, args=(), tol=1e-6, maxi=24):
  for i in range(maxi):
    xo = x
    fx = f(x, *args)
    dfx = df(x, *args)
    dx = fx / dfx
    x -= dx
    if abs(dx) < tol * (1.0 + abs(x)):
      return x
    fn = f(x, *args)
    j = 0
    while (abs(fn) >= abs(fx)) and (j <= 10):
      dx *= 0.5  # take half step size
      x = xo - dx
      fn = f(x, *args)
      xo = x
      j += 1
  raise Exception("Max its reached!")
