import subprocess


z = [0.001, 0.02]
for metal in z:
	print(metal)
	i = 0.1
	while(i < 100.02):
		f = open("evolve.in", "r+")
		data = f.readlines()
		age = 12000
		convi = str(i)
		convz = str(metal)
		convage = str(age)
		data[0] = convi + ' ' + convz + ' ' + convage + '\n'
		f.seek(0)

		f.writelines(data)
		f.close()
		subprocess.run(["sse"])
		subprocess.run(["mv", "evolve.dat", f"evolve_{i:.1f}_{metal}"])
		if(i < 0.99):
			i += 0.1
		elif(i < 9.99):
			i += 1
		elif(i < 24.99):
			i += 2.5
		elif(i < 49.99):
			i += 5
		else:
			i += 10

