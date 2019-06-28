import hashlib
import sys

def initial():
    files = [sys.argv[1], sys.argv[3]]
    enablemd5check = True
    enablesha1check = False
    enablesha256check = False

    for arg in sys.argv:
        if arg == '-s1':
            enablesha1check = True
            enablemd5check = False

        if arg == '-s2':
            enablesha256check = True
            enablemd5check = False

    if enablemd5check:
        checkmd5 = giveMeMd5(files)
        if checkmd5[2]:
            print('-' * 50)
            print('The files have the same MD5 hash: {}'.format(checkmd5[0]))
            print('-' * 50)
        else:
            print('-'*100)
            print("The files don't have the same MD5 hash\nFile 1: {} \t File 2: {} ".format(checkmd5[0], checkmd5[1]))
            print('-' * 100)

    if enablesha1check:
        checksha1 = giveMeSha1(files)
        if checksha1[2]:
            print('-' * 70)
            print('The files have the same SHA1 hash: {}'.format(checksha1[0]))
            print('-' * 70)
        else:
            print('-' * 92)
            print(
                "The files don't have the same SHA1 hash\nFile 1: {} \t File 2: {} ".format(checksha1[0], checksha1[1]))
            print('-' * 92)

    if enablesha256check:
        checksha256 = giveMeSha256(files)
        if checksha256[2]:
            print('-' * 72)
            print('The files have the same SHA256 hash: {}'.format(checksha256[0]))
            print('-' * 72)
        else:
            print('-' * 94)
            print("The files don't have the same SHA256 hash\nFile 1: {} \t File 2: {} ".format(checksha256[0],
                                                                                                checksha256[1]))
            print('-' * 94)

def giveMeMd5(files):
    hashmd5 = []
    for filename in files:
        md5 = hashlib.md5()
        with open(filename, 'rb') as f:
            buf = f.read()
            md5.update(buf)
            m = md5.hexdigest()
            hashmd5.append(m)
    hashmd5.append(hashmd5[0] == hashmd5[1])
    return hashmd5

def giveMeSha1(files):
    hashsha1 = []
    for filename in files:
        sha1 = hashlib.md5()
        with open(filename, 'rb') as f:
            buf = f.read()
            sha1.update(buf)
            s1 = sha1.hexdigest()
            hashsha1.append(s1)
    hashsha1.append(hashsha1[0] == hashsha1[1])
    return hashsha1

def giveMeSha256(files):
    hashsha256 = []
    for filename in files:
        sha256 = hashlib.md5()
        with open(filename, 'rb') as f:
            buf = f.read()
            sha256.update(buf)
            s2 = sha256.hexdigest()
            hashsha256.append(s2)
    hashsha256.append(hashsha256[0] == hashsha256[1])
    return hashsha256


if __name__ == '__main__':

    print('Developed by Raphael Sampaio | SDG')
    initial()








