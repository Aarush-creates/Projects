from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("C:/Users/ashis/Downloads/volunteer.pdf")

writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

password = input("Choose a password for encryption: ")

writer.encrypt(password)

with open("blockchain.pdf", "wb") as f:
     writer.write(f)
 
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("mykey.key", "wb") as mykey:
    mykey.write(key)

f = Fernet(key)

with open("C:/Users/ashis/Downloads/volunteer.pdf", "rb") as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)
