from Crypto.PublicKey import RSA
import argparse

parser = argparse.ArgumentParser(description='Provide RSA components')

parser.add_argument("--N" , type=int, required=True, help="Modulus")
parser.add_argument("--p" , type=int, required=True, help="P prime factor of N")
parser.add_argument("--q" , type=int, required=True, help="Q prime factor of N")
parser.add_argument("--e" , type=int, required=True ,help="Public exponent")
parser.add_argument("--d" , type=int, help="Private exponent")


args = parser.parse_args()

N = args.N
e = args.e
p = args.p
q = args.q

if args.d is None:
    try:
        key = RSA.construct([N,e,p,q])
        print(key.export_key('PEM').decode())
    except ValueError:
        print("RSA key not valid !")

else:
    d = args.d
    try:
        key = RSA.construct([N,e,p,q,d])
        print(key.export_key('PEM').decode())
    except ValueError:
        print("RSA key not valid !")

