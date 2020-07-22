import time
ina = int(input('Enter the value of m when m^n.: '))
inb = int(input('Enter the value of n when m^n.: '))
start_time = time.time()
out = 1
for i in range(0, inb):
	out = out * ina
print(out)
print(len(str(out)), "digits")
print("Total elapsed time: ", (time.time() - start_time))
