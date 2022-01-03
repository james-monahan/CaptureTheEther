//hack the hash ( uint8(2**8) ) possibilities

#brownie

from web3 import Web3

answer = []
answerHash = '0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365'

for n in range(256):
    hash = Web3.solidityKeccak(['uint8'], [n]).hex()
    if hash == answerHash:
        answer.append((hash, n))

def main():
    print(hashes)
