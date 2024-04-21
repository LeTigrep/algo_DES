from bitarray import bitarray
import math

def IP(block):
    output_block=bitarray()
    for i in range(0, 8, 2):
        for j in range(0, 64, 8):
            output_block.append(block[58 + i - j-1])
            


    for i in range(0, 8, 2):
        for j in range(0, 64, 8):
            output_block.append(block[57 + i - j-1])

    return output_block

def IP1(Block):
    result=bitarray()
    temp1=40
    jtemp1=0
    jtemp2=0
    temp2=8
    for i in range(8):
        for j in range(8):
            if j%2==0:
                result.append(Block[temp1-i+(8*jtemp1)-1])
                jtemp1+=1
            else:
                result.append(Block[temp2-i+(8*jtemp2)-1])
                jtemp2+=1
        jtemp1=0
        jtemp2=0
    return result


def perm(block):
    temp=bitarray()
    temp.extend([block[15],block[6],block[19],block[20],block[28],block[11],block[27],block[16],block[0],block[14],block[22],block[25],block[4],block[17],block[30],block[9],block[1],block[7],block[23],block[13],block[31],block[26],block[2],block[8],block[18],block[12],block[29],block[5],block[21],block[10],block[3],block[24]])
    return temp


def expand(block):
    temp=bitarray()
    temp.append(block[31])
    for i in range(4,32,4):
        temp+=block[i-4:i]
        temp.append(block[i])
        temp.append(block[i-1])
    temp+=block[28:]
    temp.append(block[0])
    return temp


def shift(block):
    temp=block[1:]+block[:1]
    return temp


def S_box(n):
    temp=''
    sboxes=[]
    S1=[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
    S2=[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
    S3=[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
    S4=[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
    S5=[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
    S6=[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
    S7=[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13 ,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
    S8=[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
    for j in range(0,48,6):
      for i in range(0+j,6+j):
        temp+=str(n[i])
      sboxes.append(temp)
      temp=''
    sb=bitarray()
    sb+=(bin(S1[int(sboxes[0][0]+sboxes[0][5],2)][int(sboxes[0][1:5],2)])[2:]).zfill(4)
    sb+=(bin(S2[int(sboxes[1][0]+sboxes[1][5],2)][int(sboxes[1][1:5],2)])[2:]).zfill(4)
    sb+=(bin(S3[int(sboxes[2][0]+sboxes[2][5],2)][int(sboxes[2][1:5],2)])[2:]).zfill(4)
    sb+=(bin(S4[int(sboxes[3][0]+sboxes[3][5],2)][int(sboxes[3][1:5],2)])[2:]).zfill(4)
    sb+=(bin(S5[int(sboxes[4][0]+sboxes[4][5],2)][int(sboxes[4][1:5],2)])[2:]).zfill(4)
    sb+=(bin(S6[int(sboxes[5][0]+sboxes[5][5],2)][int(sboxes[5][1:5],2)])[2:]).zfill(4)
    sb+=(bin(S7[int(sboxes[6][0]+sboxes[6][5],2)][int(sboxes[6][1:5],2)])[2:]).zfill(4)
    sb+=(bin(S8[int(sboxes[7][0]+sboxes[7][5],2)][int(sboxes[7][1:5],2)])[2:]).zfill(4)
    return sb
        
        
def circular_shift(left,right,number):
      temp1=shift(left)
      temp2=shift(right)
      for i in range(number-1):
        temp1=shift(temp1)
        temp2=shift(temp2)
      return (temp1,temp2)
  
  
def XOR(e1,e2):
    temp=bitarray()
    for i in len(e1):
        temp.append(e1[i]^e2[i])
    return temp


def Initial_Key(Key,taille):
    for i in range(taille-1,taille,taille*8):
        del Key[i]
        
        
def PC_1(Key):
    Left=bitarray()
    Right=bitarray()
    temp_left_lign=48
    temp_right_lign=54
    for i in range(4):
       temp_left_lign+=9
       if temp_left_lign+9>65:
           temp_left_lign-=65  
       temp_left_column=temp_left_lign   
       for j in range(7):
         if temp_left_column-(8*j)<0:
           temp_left_column+=65  
         Left.append(Key[temp_left_column-(8*j)-1])
    for i in range(4):
       if temp_right_lign==7 or temp_right_lign==14:
           temp_right_lign+=7
       else:    
           temp_right_lign+=9
           if temp_right_lign>65:
               temp_right_lign-=65
       
       temp_right_column=temp_right_lign
       for j in range(7):
         Right.append(Key[temp_right_column-1])
         if temp_right_column==5:
             temp_right_column+=23
         else:    
             temp_right_column-=8
             if temp_right_column<0:
               temp_right_column+=63
    return(Left,Right)


def PC_2(Key):
    pc2=bitarray()
    pc2.extend([Key[13],Key[16],Key[10],Key[23],Key[0],Key[4],Key[2],Key[27],Key[14],Key[5],Key[20],Key[9],Key[22],Key[18],Key[11],Key[3],Key[25],Key[7],Key[15],Key[6],Key[26],Key[19],Key[12],Key[1],Key[40],Key[51],Key[30],Key[36],Key[46],Key[54],Key[29],Key[39],Key[50],Key[44],Key[32],Key[47],Key[43],Key[48],Key[38],Key[55],Key[33],Key[52],Key[45],Key[41],Key[49],Key[35],Key[28],Key[31]])
    return pc2

def F(right,key):
    temp_right=expand(right)
    xor=temp_right^key
    sbox_result=S_box(xor)
    permutation_result=perm(sbox_result)
    return permutation_result
    
    
def encryption(P):
    IP_P=IP(P)
    left_encry=IP_P[:32]
    right_encry=IP_P[32:]
    for i in range(16):
        temp=right_encry
        right_encry=left_encry^F(temp,key_rounds[i])
        left_encry=temp
    temp=right_encry
    right_encry=left_encry
    left_encry=temp
    IP1_result=IP1(left_encry+right_encry)
    return IP1_result



def decryption(C):
    IP_result=IP(C)
    left_decry=IP_result[:32]
    right_decry=IP_result[32:]
    temp=left_decry
    left_decry=right_decry
    right_decry=temp
    for i in range(15,-1,-1):
        temp=left_decry
        left_decry=right_decry^F(temp,key_rounds[i])
        right_decry=temp
    IP1_P=IP1(left_decry+right_decry)
    return IP1_P


def string_to_binary_ascii(input_string):
    binary_result = ""
    for char in input_string:
        ascii_value = ord(char)
        binary_representation = bin(ascii_value)[2:].zfill(8)
        binary_result += binary_representation
    return binary_result



def binary_to_ascii(binary_str):
    temp = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

    ascii_chars = [chr(int(temp, 2)) for temp in temp]

    ascii_string = ''.join(ascii_chars)

    return ascii_string

#main
test=True
while test:
    try:
        key=bitarray(input("donner key"))
        if len(key)==64:
            test=False
            key_temp=key
            PC1_left,PC1_right=PC_1(key_temp)
            keys=[]
            keys.append(circular_shift(PC1_left,PC1_right,1))
            for i in range(1,16):
                if i not in [1,8,15]:
                    keys.append(circular_shift(keys[i-1][0],keys[i-1][1],2))
                else:
                    keys.append(circular_shift(keys[i-1][0],keys[i-1][1],1))
                            
            key_rounds=[]
            for i in range(16):
                key_rounds.append(PC_2(keys[i][0]+keys[i][1]))
            bol=True
            while(bol):
                try:
                    Question=int(input("do you want to encrypt or decrypt? 1 for encrypt ,2 for decrypt"))
                    if Question==1:
                        bol=False
                        plaintext=(input("plaintext"))
                        plaintext_enc=string_to_binary_ascii(plaintext)
                        plaintext_bin=plaintext_enc.zfill(((len(plaintext_enc)//64)+1)*64)
                        temp=[]
                        for i in range((len(plaintext_bin)//64)):
                            temp.append(plaintext_bin[0+64*i:64+64*i])

                        result=bitarray()
                        for i in temp:
                            result+=encryption(bitarray(i))
                        ciphertext=hex(int(result.to01(),2))[2:]
                        print("le ciphertext est :",ciphertext)
                        poll=input(" Do you want to keep encrypting/decrypting,Y/N?")
                        if poll=="Y":
                            test=True
                        
                    elif Question==2:
                        bol=False
                        ciphertext=(input("ciphertext"))
                        cipher_bin_input=bin(int(ciphertext,16))[2:]
                        cipher_bin=cipher_bin_input.zfill((math.ceil(len(cipher_bin_input)/8)*8))
                        temp2=[]
                        for i in range((len(cipher_bin)//64)):
                            temp2.append(cipher_bin[0+64*i:64+64*i])
                        result_dec=bitarray()
                        for i in temp2:
                            result_dec+=decryption(bitarray(i))
                        temp_while=True
                        inc=0
                        while inc<len(result_dec) and temp_while:
                                if result_dec[inc]==1:
                                    temp_while=False
                                else:
                                    del result_dec[inc]

                        plainte=binary_to_ascii((result_dec.to01()).zfill(((len(result_dec)//8)+1)*8))
                        print("le plaintext est:",plainte)
                        poll=input(" Do you want to keep encrypting/decrypting,Y/N?")
                        if poll=="Y":
                            test=True
                    else:
                        print("please give 1 if you want to encrypt or 2 if you want to decrypt")
                except:
                    print("this is not a number!.please give 1 if you want to encrypt or 2 if you want to decrypt")
                # else:

        else:
              print("the length of the key is not 64 bits!")
    except:
          print("The key should be formed from zeros and ones only")
          
 




    




    



