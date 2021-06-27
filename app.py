import zipfile as zf

def cracker(passlist,file):
    with open(passlist,"rb") as pl:
        for line in pl:
            for word in line.split():
                try:
                    file.extractall(pwd=word)
                    print(f'Password is {word.decode()}')
                    return True
                except:
                    pass
    return False
print('Welcome to Dictionary Attack engine\n')
passlist = "passlist.txt"
file="file.zip"

file=zf.ZipFile(file)

if cracker(passlist,file)==False:
    print('No Password Matched')
