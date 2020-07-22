ina = int(input('m^n을 할 때, m의 값: '))
inb = int(input('m^n을 할 때, n의 값: '))
out = 1
for i in range(0, inb):
	out = out * ina
print(out)
print(len(str(out)), "digits")
