from hashlib import sha256
import csv

def hash_password_hack(input_file, output_file):
    with open(input_file) as fin:
        reader = csv.reader(fin)
        hsh = dict()
        hsh2 = dict()

        for ps in range(1000, 10000):
            hash = sha256(str(ps).encode()).hexdigest()
            hsh[hash] = ps
        for each in reader:
            pas = each[0]
            reader_hash = each[1]
            for hsh_hash in list(hsh.keys()):
                if hsh_hash == reader_hash:
                    hsh2[pas] = hsh.get(hsh_hash)
    with open(output_file, 'w') as fout:
        for each in hsh2:
            fout.write('%s,%i\n' %(each, hsh2[each]))
            
