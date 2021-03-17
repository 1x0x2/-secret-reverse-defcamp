from subprocess import check_output
from hashlib import sha256
from string import ascii_lowercase
from itertools import permutations

ciphertext = '46004746409548141804243297904243125193404843946697460795444349'
def run(s):
    with open("message.txt","w") as fd: fd.write(s)
    try:
        out = check_output(["./rev_secret_secret.o"])
        out = out.strip().split(b"Encoded:  ")[1].decode()
        return out
    except:
        return ""

c = 0
flag = ''
new_cipher = ''
checker = ascii_lowercase
checker = list(checker)

step = 0
ok = 0
while 1:
    comb = permutations(checker, 2)
    # Print the obtained combinations 
    for i in list(comb):
        flag1 = flag
        flag1 += ''.join(i)
        str1 = run(flag1)
        if str1 == (new_cipher + ciphertext[c:c+2+step]):
            new_cipher += ciphertext[c:c+2 + step]
            c = c + 2 + step
            flag = flag1
            print(flag)
            ok = 1
            break
    if ok == 0:
        step += 1
    else:
        ok = 0
        step = 0
        
    if run(flag) == ciphertext:
        flag = flag.replace('x','_')
        print(sha256(flag.encode()).hexdigest())
        break
