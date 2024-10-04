import random
ch = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
şifrelen = int(input("şifrenizin uzunluğunu girin"))
şifre = ""
for i in range(şifrelen):
    şifre += random.choice(ch)

print(şifre)