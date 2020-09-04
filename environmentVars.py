#! python3
import os
print ( "[*] Debugging Script: nonintegral to the function of the runner." )
print ("[*] keeping around as reference tool, PWD may not be ideal path, working for now though")
print (" ")

for key, val in os.environ.items():
	print (f' {key}={val}')

print ( " " )

pwdAbsolutePathHack = os.environ['PWD']
print (pwdAbsolutePathHack)
