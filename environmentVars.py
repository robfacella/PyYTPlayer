#! python3
import os

for key, val in os.environ.items():
	print (f' {key}={val}')

print ( " " )

pwdAbsolutePathHack = os.environ['PWD']
print (pwdAbsolutePathHack)
