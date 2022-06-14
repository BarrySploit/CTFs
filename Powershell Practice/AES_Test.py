#better version of the Powershell Password Generator
#Uses AES encryption to secure stored passwords. Plaintext password is not stored in program.
#Tracks account information and passwords
import string
import random
import base64
import csv
import pandas as pd
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import hashlib

#define lists of possible characters
char_list = []
char_string = string.ascii_letters + string.digits + '!@#$%^&*()?'
for i in char_string:
        char_list.append(i)

#make sure key is 16 in length. Encrypt passwords with secret key. Save in format of IV:CipherText
def aes_encryption(string, key):
        while len(key) < 16:
                key += "A"
        if len(key) > 16:
                key = key[:16]
        cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC)
        ciphertext= cipher.encrypt(pad(string.encode('utf-8'),AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ciphertext).decode('utf-8')
        result = iv + ":"+ct
        return result

#Use IV and Ciphertext with secret key to decrypt the passwords
def aes_decryption(string, key):
        while len(key) < 16:
                key += "A"
        if len(key) > 16:
                key = key[:16]
        encrypted = string.split(':')
        iv = base64.b64decode(encrypted[0])
        ct = base64.b64decode(encrypted[1])
        cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC,iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt

#Generate random password of given length (at least 12)
def Gen_Password():
        password = ''
        count = input("How long would you like your password to be?\n")
        while int(count) < 12:
                count = input("Password must be at least 12 characters in length. How long would you like your password to be?\n")
        for i in range(0,int(count)):
                char = random.choice(char_list)
                password+=char
        return password

#add new entry to CSV file
def new_account():
        email = input("What is your email?\n")
        website = input("What website is this for?\n")
        own_password = input("Are you using your own password? Yes/No.'No' will generate a secure password for you!\n")
        with open(path,"a", newline ='') as file:
                fieldnames = ['Email', 'Website', 'Password']
                writer = csv.DictWriter(file, fieldnames = fieldnames)
                if own_password.lower() == "yes":
                        password = input("What password do you want to use?\n")
                        password = aes_encryption(password,key)
                        writer.writerow({'Email':email, 'Website':website, 'Password':password})
                if own_password.lower() == "no":
                        password = Gen_Password()
                        print("Your password is "+ password+"\n")
                        password = aes_encryption(password,key)
                        writer.writerow({'Email':email, 'Website':website, 'Password':password})

#Change password of existing entry
def change_password():
        website = input("What website do you want to change the password for?\n")
        GenPassOrNah = input("Are you using your own password? Yes/No.'No' will generate a secure password for you!\n")
        with open(path, 'r', newline='') as file:
                fieldnames = ['Email', 'Website', 'Password']
                reader = csv.DictReader(file, fieldnames=fieldnames)
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for row in reader:
                        if row['Website'] == website:
                                password = row['Password']
                                if GenPassOrNah.lower() == 'yes':
                                        user_pass = input("What is the password you want to use?\n")
                                if GenPassOrNah.lower() =='no':
                                        user_pass = Gen_Password()
                                encrypted = aes_encryption(user_pass,key)
                                break   
        df = pd.read_csv(path)
        df['Password'] = df['Password'].replace({password:encrypted})
        df.to_csv(path, index=False)

#Retrieve stored password
def check_password():
        website = input("What website do you want to check the password for?\n")
        with open(path, 'r', newline='') as file:
                fieldnames = ['Email', 'Website', 'Password']
                reader = csv.DictReader(file, fieldnames=fieldnames)
                for row in reader:
                        if row['Website'] == website:
                                password = row['Password']
                                decrypted = aes_decryption(password,key).decode('utf-8')
                                print("The password for "+str(website)+" equals "+str(decrypted)+"\n")
                                break
                                
#Continuously loop until user decides to exit
def main():
        while True:
                to_do = input("What would you like to do? \n1) Add a new account. \n2) Change an existing password. \n3) Check a password. \n4) Exit the program.\n")
                if to_do == "1":
                        new_account()
                elif to_do == "2":
                        change_password()
                elif to_do == "3":
                        check_password()
                elif to_do == "4":
                        exit()
                main()

                
if __name__ == "__main__":
        existing_file = input("Do you currently have an existing password sheet? Yes/No\n")
        #Get existing CSV file
        if existing_file.lower() == 'yes':
                path = input("What is the path to your password file?\n")
                #Enter secret key and compare to stored hash in hash.txt
                key = input("What is the secret key?\n")
                secret_path = "hash.txt"
                with open(secret_path, 'r') as f:
                        secret = f.read()
                        secret_hash = hashlib.sha256(key.encode('utf-8')).hexdigest()
                        if secret_hash != secret:
                                print("Wrong secret key!!!")
                                print(secret_hash)
                                exit()

        else:
                path = input("Enter the path of where you want to save your new password file.\n")
                with open(path, 'a', newline='') as file:
                        fieldnames = ['Email', 'Website', 'Password']
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        writer.writeheader()
                with open("hash.txt",'w') as f:
                        key = input("What do you want your secret key to be? WARNING: This will overwrite current hash.txt if it exists.\nOld Passwords will be unrecoverable.\n")
                        secret_hash = hashlib.sha256(key.encode('utf-8')).hexdigest()
                        f.write(secret_hash)
        main()
