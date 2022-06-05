#Encrypting Google foo.bar 2017 encrypted message
#Algo-> Decode the message string to base64 bytes.
#       and do XOR of decoded bytes with your Google username.

import base64

#The encrypted key
message='GE8BHBABAB8fFRMPGEQPAAwSFkJATBVQWlQPDRMOBgdCTFYSFFBLFw0XBBYGQkBMFVZTXgwaBhpU Ql9MS1tdVkoGDBsLHwdCQEwVUlZ' \
        'QCg0EDB4HCxhLEgkVHxYGHgYQCQAISx4TEkoCChAABxFCTFYS FEZZBQ1VRVNFAwMDFRMPGEQfGwdSRRg='

#Your Google username
key='chrisbell2358'

decrypted_message=[]

#decode the key to base64 bytes
dec_bytes=base64.b64decode(message)

#XOR with Username
for a,b in enumerate(dec_bytes):
    decrypted_message.append(chr(b ^ ord(key[a%len(key)])))

#The encypted message
print("".join(decrypted_message))