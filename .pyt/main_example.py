from py_template import l, genv, senv, logi

l.critical('Ez egy példa log üzenet')

print(genv('user')) # a .env fájlban a user változó értékét olvassa ki
senv('user', 'Johni') # a .env fájlban a user változó értékét átírja Johnira
print(logi()) # kiírja a hívó függvény nevét