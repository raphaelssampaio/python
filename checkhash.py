import hashlib
import sys


def checker():
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

        if arg == '-h':
            enablemd5check = False
            enablesha1check = False
            enablesha256check = False
            help()

    if enablemd5check:
        checkmd5 = giveMeMd5(files)
        if checkmd5[2]:
            print(' The files have the same MD5 hash: {}'.format(checkmd5[0]))
            print('-' * 60)
        else:
            print(" The files don't have the same MD5 hash\n" + "-" * 60 + "\n File 1: {} \t File 2: {} "
                  .format(checkmd5[0], checkmd5[1]))
            print('-' * 100)

    elif enablesha1check:
        checksha1 = giveMeSha1(files)
        if checksha1[2]:
            print(' The files have the same SHA1 hash: {}'.format(checksha1[0]))
            print('-' * 60)
        else:
            print(
                    " The files don't have the same SHA1 hash\n" + "-" * 60 + "\n File 1: {} \t File 2: {} "
                    .format(checksha1[0], checksha1[1]))
            print('-' * 92)

    elif enablesha256check:
        checksha256 = giveMeSha256(files)
        if checksha256[2]:
            print(' The files have the same SHA256 hash: {}'.format(checksha256[0]))
            print('-' * 60)
        else:
            print(" The files don't have the same SHA256 hash\n" + "-" * 60 + "\n File 1: {} \t File 2: {} "
                  .format(checksha256[0], checksha256[1]))
            print('-' * 94)


def help():
    print("""\t\tHELP CHECK HASH
------------------------------------------------------------
 Let's understand what we are doing here in this code: 'python3 checkhash.py file1 -c file2 -s2'
 python3: \tThe interpreter Python of this app
   file1: \tThe first file we want to compare
      -c: \tThe standard argument for compare
   file2: \tThe second file we want to compare
     -s2: \tThe extra argument that indicates we want to check SHA256 hashes
 -----------------------------------------------------------------------------------------------------------        
 NOTE: If we want to compare MD5 hashes we don't need to put any extra argument. Let's see an example.
 
 'python3 checkhash.py file1 -c file2'
 >>> 
 >>> Now we are comparing MD5 hashes of file1 and file2
 -----------------------------------------------------------------------------------------------------------
 ARGUMENTS and EXTRA:
 -c: \tCompare file1 and file2
 -s1: \tCheck SHA1 hash
 -s2: \tCheck SHA256 hash""")


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

    print('-' * 60)
    print('\tDeveloped by Raphael Sampaio | SDG')
    print('-' * 60)
    for arg in sys.argv:
        if arg == '-c':
            checker()
            break
        elif arg == '-h':
            help()
            break
