from dh import AlphaDHE
from MASHHASH import MASH
import sys

try:
    mode = sys.argv[1]
except IndexError as ier:
   mode = None

dhe = AlphaDHE()
g, p, secret = dhe.init()
if mode == "init":
    sys.stdout.write("Initial step: Send g and p to your peer\n")
    sys.stdout.write("g: "+g+"\n")
    sys.stdout.write("p: "+p+"\n")
else:
    g = raw_input("Enter your peer's g value: ")
    p = raw_input("Enter your peer's p value: ")

mystep1 = dhe._step1(g, p, secret)
sys.stdout.write("Step 1: Send this to your peer\n")
sys.stdout.write(mystep1+"\n")
peerstep1 = raw_input("Enter peer's step 1: ")
key = dhe._step2(peerstep1, p, secret)
session_key = MASH(length=16).digest(key)
sys.stdout.write("Secret Session key: "+session_key+"\n")
