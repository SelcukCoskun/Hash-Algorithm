import hashlib

while True:
 text=input("Enter the text you want to hash =")

 text_utf=text.encode('utf-8')#We converted the data to utf-8.

 choice=input("Which hash algorithm do you want to use?/md-5/sha-1/sha-256/sha-512=")

 if choice =="md5":
      hash=hashlib.md5(text_utf)#We got the hash of the utf-8 type data
      hash2=hash.hexdigest()#Then we made it hexadecimal
      print(hash2)
      break

 elif choice=="sha-1":
     hash=hashlib.sha1(text_utf)
     hash2=hash.hexdigest()
     print(hash2)
     break

 elif choice=="sha-256":
     hash=hashlib.sha256(text_utf)
     hash2=hash.hexdigest()
     print(hash2)
     break

 elif choice=="sha-512":
     hash=hashlib.sha512(text_utf)
     hash2=hash.hexdigest()
     print(hash2)
     break

 else:
     print("Enter a valid hash algorithm")
