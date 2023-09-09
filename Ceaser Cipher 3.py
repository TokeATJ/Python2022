##GitHub Toke Atijosan ##


def getEncryption (user_txt, key):

    encrypted = ""

    for wip in user_txt:

        if wip.islower():

            wip_index = ord(wip) - ord('a')

            wip_scramble = (wip_index + key) % 26 + ord('a')

            wip_newscramble = chr (wip_scramble)

            encrypted += wip_newscramble

        elif wip.isupper():

            wip_index = ord(wip) - ord('A')

            wip_scramble = (wip_index + key) % 26 + ord('A')

            wip_newscramble = chr (wip_scramble)

            encrypted += wip_newscramble


        else:
            
            encrypted += wip

    return encrypted

def getDecryption(ciphertext, key):

    decrypted = ""

    for wip in ciphertext:

        if wip.islower():

            wip_index = ord(wip) - ord('a')

            wip_org_pos = (wip_index - key) % 26 + ord('a')

            wip_org = chr(wip_org_pos)

            decrypted += wip_org

        elif wip.isupper():

            wip_index = ord(wip) - ord('A')

            wip_org_pos = (wip_index - key) % 26 + ord('A')

            wip_org = chr(wip_org_pos)

            decrypted += wip_org



        else:

            decrypted += wip

    return decrypted

key = int(input('Enter your encryption key: '))

message = input('Enter your message: ')


ciphertext = getEncryption (message, key)
print()
print('Your encrypted message is:', ciphertext)
print('Your decrypted message is:', getDecryption (ciphertext, key))
