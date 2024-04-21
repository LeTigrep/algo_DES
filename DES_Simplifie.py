# Import the necessary functions from the bitarray library
from bitarray import bitarray
from bitarray.util import ba2int
from bitarray.util import int2ba
import tkinter as tk
from tkinter import messagebox




#                        +----------------------------------+
#                        |       DES KEY GENERATION         |
#                        +----------------------------------+


#Permutation : P10(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10) = (k3, k5, k2, k7, k4, k10, k1, k9, k8, k6)
def p10(key) :
    pkey = bitarray()
    pkey.extend([key[2], key[4], key[1], key[6],key[3],key[9],key[0],key[8],key[7],key[5]])
    return pkey

# permutation : P8 : 6 3 7 4 8 5 10 9
def p8(key) :
    pkey = bitarray()
    pkey.extend([key[5], key[2], key[6], key[3],key[7],key[4],key[9],key[8]])
    return pkey

def shift1(key) :
    pkey = key[5:] + key[0:5]
    return pkey

def shift2(key) :
    pkey = key[2:5] + key[0 : 2] + key[7:] + key [5 : 7]
    return pkey

# K1 = P8 (Shift (P10 (key)))
def generate_key1(key) :
    return p8(shift1(p10(key)))

# K2 = p8(shift2(shift1(p10(key))))
def generate_key2(key) :
    return p8(shift2(shift1(p10(key))))



#########################################################################################################

#                          +----------------------------------+
#                          |          DES ENCRYPTION          |
#                          +----------------------------------+



# Permutation message ; 2 6 3 1 4 8 5 7
def p(message) :
    pmessage = bitarray()
    pmessage.extend([message[1], message[5], message[2], message[0],message[3],message[7],message[4],message[6]])
    return pmessage


# Inverse de permutation message : 4 1 3 5 7 2 8 6
def inv_p(message) :
    pmessage = bitarray()
    pmessage.extend([message[3], message[0], message[2], message[4],message[6],message[1],message[7],message[5]])
    return pmessage


# expansion : 4 1 2 3 2 3 4 1 and transform into matrice and xor key
def expansion(message, key) :
    enumber = bitarray()
    enumber.extend([message[3], message[0], message[1], message[2], message[1], message[2], message[3], message[0]])
    matrice = [enumber[0:4]^key[0:4],enumber[4:8]^key[4:8]]
    return matrice


# sbox : S-box S0 to produce a 2-bit output, and the remaining 4 bits are fed into S1 to produce another 2-bit output
# and produced by S0 and S1 undergo a further permutation as follows: 2 4 3 1
def sbox(m1,m2) :
    s0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]] 
    s1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    result_so = s0[ba2int(m1[::len(m1)-1])][ba2int(m1[1:3])]
    result_s1 = s1[ba2int(m2[::len(m2)-1])][ba2int(m2[1:3])]
    resultat = int2ba(result_so,length=2) + int2ba(result_s1,length=2)
    fresultat = bitarray()
    fresultat.extend([resultat[1], resultat[3], resultat[2], resultat[0]])
    return fresultat


# F. The input is a 4-bit number
def F(message, k) :
    m = expansion(message, k)
    return sbox(m[0],m[1])


# switch function (SW) interchanges the left and right 4 bits
def Switch(message) :
    pkey = message[4:] + message[0:4]
    return pkey


# fK, which consists of a combination of permutation and substitution functions
# fK(L,R)=(L XOR F(R,SK),R)
def fk(message,key) :
    return (message[0:4]^(F(message[4:],key)))+message[4:]


# ciphertext = IP-1(fK2(SW(fK1(IP(plaintext)))))
def encryption(plaintext, keygenerale) :
    k1=generate_key1(keygenerale)
    k2=generate_key2(keygenerale)
    return inv_p(fk(Switch(fk(p(plaintext),k1)),k2))



#########################################################################################################

#                          +----------------------------------+
#                          |        DES DECRYPTION            |
#                          +----------------------------------+



# plaintext = IP-1(fK1(SW(fK2(IP(ciphertext)))))
def decryption(ciphertext, keygenerale) :
    k1=generate_key1(keygenerale)
    k2=generate_key2(keygenerale)
    return inv_p(fk(Switch(fk(p(ciphertext),k2)),k1))


########################################################################################################

#                          +----------------------------------+
#                          |             MAIN                 |
#                          +----------------------------------+



# Fonctions pour vérifier les séquences binaires
def is_binary_sequence(s):
    return all(bit in '01' for bit in s)

def valid_key(s):
    return len(s) == 10 and is_binary_sequence(s)

def valid_message(s):
    return len(s) % 8 == 0 and is_binary_sequence(s)

# Fonction appelée pour effectuer le chiffrement/déchiffrement
def perform_action():
    key = key_entry.get()
    message = message_entry.get()
    choice = var.get()

    if not valid_key(key):
        messagebox.showerror("Erreur", "La clé doit être une séquence binaire de longueur 10.")
        return

    if not valid_message(message):
        messagebox.showerror("Erreur", "Le message doit être une séquence binaire dont la longueur est un multiple de 8.")
        return

    key_bits = bitarray(key)
    message_bits = bitarray(message)
    message_parts = [message_bits[i:i+8] for i in range(0, len(message_bits), 8)]
    results = []

    for part in message_parts:
        if choice == 1:  # Chiffrement
            results.append(encryption(part, key_bits))
        else:            # Déchiffrement
            results.append(decryption(part, key_bits))

    final_result = bitarray()
    for part in results:
        final_result += part
    result_str = final_result.to01()
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result_str)

# Création de l'interface graphique
root = tk.Tk()
root.title("DES Encryption/Decryption")

# Label pour le champ de saisie du message
message_label = tk.Label(root, text="Message (en binaire) :")
message_label.pack()

# Champ de saisie pour le message
message_entry = tk.Entry(root, width=70)
message_entry.pack()

# Label pour le champ de saisie de la clé
key_label = tk.Label(root, text="Clé (10 bits en binaire) :")
key_label.pack()

# Champ de saisie pour la clé
key_entry = tk.Entry(root, width=50)
key_entry.pack()

# Radiobuttons pour le choix de l'action
var = tk.IntVar()
encrypt_button = tk.Radiobutton(root, text="Chiffrer", variable=var, value=1)
encrypt_button.pack()
decrypt_button = tk.Radiobutton(root, text="Déchiffrer", variable=var, value=2)
decrypt_button.pack()

# Bouton pour exécuter l'action
action_button = tk.Button(root, text="Exécuter", command=perform_action)
action_button.pack()

# Champ de saisie pour afficher le résultat
result_entry = tk.Entry(root, width=50)
result_entry.pack()

root.mainloop()
