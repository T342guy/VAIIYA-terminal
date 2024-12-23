
import bcrypt 
  #no password 4 u
# example password 
password = ' '
  
# converting password to array of bytes 
bytes = password.encode('utf-8') 
  
# generating the salt 
salt = bcrypt.gensalt() 
  
# Hashing the password 
hash = bcrypt.hashpw(bytes, salt) 
  
print(hash)

#this is the bcrypt hash genorator, where i get the hashes for the passwords. 