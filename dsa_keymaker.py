from Crypto.PublicKey import DSA

import argparse

parser = argparse.ArgumentParser(description='Provide DSA components')

parser.add_argument("--y" , type=int, required=True, help="Modulus")
parser.add_argument("--p" , type=int, required=True, help="Prime factor")
parser.add_argument("--q" , type=int, required=True, help="Subgroup order")
parser.add_argument("--g" , type=int, required=True ,help="Group generator")
parser.add_argument("--x" , type=int, help="Private key")


y = args.y
p = args.p
q = args.q
g = args.g

if args.x is None:
    try:
        key = DSA.construct([y,g,p,q])
        print(key.export_key('PEM').decode())
    except ValueError:
        print("DSA key not valid !")
else:
    x = args.x
    try:
        key = DSA.construct([y,g,p,q,x])
        print(key.export_key('PEM').decode())
    except ValueError:
        print("DSA key not valid !")


