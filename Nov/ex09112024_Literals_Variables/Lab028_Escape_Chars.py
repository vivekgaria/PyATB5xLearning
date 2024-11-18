#Escape Sequence

# Diff between " " & ''
c = 'C'
c1 = "C"

dir = 'C:\Vivek\n.txt'
dir1 = "C:\Vivek\n.txt"
print(dir) #SyntaxWarning: invalid escape sequence '\A'
print(dir1) #SyntaxWarning: invalid escape sequence '\A'

# r (or raw string) is resolving this issue
dir = r'C:\Vivek\n.txt'
dir1 = r"C:\Vivek\n.txt"
print(dir)
print(dir1)