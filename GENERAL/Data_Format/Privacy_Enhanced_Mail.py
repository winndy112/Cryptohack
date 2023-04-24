import Crypto
from Crypto.PublicKey import RSA

# đọc khóa từ file và lưu trữ vào biến key
with open(r'D:\Cryptohack\GENERAL\Data_Format\privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r') as file:
    key = file.read()
    rsa_key = RSA.importKey(key)
    print(rsa_key.d)
