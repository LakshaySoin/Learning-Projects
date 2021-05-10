def l100kmtompg(liters):
    mi = 100000 / 1609.344
    g = liters / 3.785411784
    return mi / g


def mpgtol100km(miles):
    km = (miles * 1609.344) / 100000
    L = 3.785411784
    return L / km


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))


