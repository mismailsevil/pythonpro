#bu uygulama rastgele şifre oluşturur
import random

karakterler="abcdefghıijklmnoöprsştuüvyz0123456789"
uzunluk=16


sifre="".join(random.choice(karakterler) for _ in range(uzunluk))






print("syın kulanıcı sana hazırladıgım şifre",sifre)
