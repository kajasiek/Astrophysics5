import subprocess

#Code to automatically run through Single Star Evolution program created by J. Hurley
#Things to note: This will only work on Linux (wow)

z = [0.001, 0.02] #Two metallicities
age = 12000
for metal in z:
	print(metal)
	i = 0.1
	while(i < 100.02):
		f = open("evolve.in", "r+")
		data = f.readlines()
		convi = str(i)
		convz = str(metal)
		convage = str(age)
		data[0] = convi + ' ' + convz + ' ' + convage + '\n' #This is required to be a string
		f.seek(0)

		f.writelines(data)
		f.close()
		subprocess.run(["sse"]) #Running through SSE
		subprocess.run(["mv", "evolve.dat", f"evolve_{i:.1f}_{metal}"]) #Renaming the file so it doesnt get lost
		if(i < 0.99):
			i += 0.1
		elif(i < 9.99):
			i += 1
		elif(i < 24.99):                      #Fun and engaging way to keep the number of files low while //
			i += 2.5                      #keeping the resolution somewhat high for low mass stars
		elif(i < 49.99):
			i += 5
		else:
			i += 10

