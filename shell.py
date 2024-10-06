import sys, os

if len(sys.argv) < 2:
    print('usage: ' + sys.argv[0] + ' file.exe\n Wrong_Byte_(optional) ')
    sys.exit(0)

shellcode = ''
bytes = 0


for b in open(sys.argv[1], 'rb').read():
 
    shellcode += '\\'+hex(b)[1:]
    if (b == 0):   
        print('Zero Byte at: '+ str(bytes) + '\n')
    if (len(sys.argv) > 2):
        if (b == int(sys.argv[2])):    
            print('Wrong Byte ' +sys.argv[2] + ' (\\'+ hex(b)[1:] +') at: '+ str(bytes) + '\n')
    bytes += 1
    

print('Number of bytes for file ' + sys.argv[1] + ': ' + str(bytes) + '\n')

fp=open("shell.txt", "w")
fp.write(shellcode)
fp.close()

print("Done!")