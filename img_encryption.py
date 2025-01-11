from cryptography.fernet import Fernet

enc = input("Are you here to encrypt or decrypt an image file? (E/D): ").strip().upper()

if enc == "E":
    try:
        path = input("Enter the path of your image: ").strip()

        key = Fernet.generate_key()

        with open("filekey.key", "wb") as filekey:
            filekey.write(key)

        fernet = Fernet(key)

        with open(path, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)
        
        # Save the encrypted file
        with open(path, "wb") as encrypted_file:
            encrypted_file.write(encrypted)

        print("File encrypted successfully. Key saved to 'filekey.key'.")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

elif enc == "D":
    try:
        path = input("Enter the path of the image: ").strip()

        with open("filekey.key", "rb") as filekey:
            key = filekey.read()

        fernet = Fernet(key)

        with open(path, "rb") as enc_file:
            encrypted = enc_file.read()
        
        decrypted = fernet.decrypt(encrypted)
        
        with open(path, "wb") as dec_file:
            dec_file.write(decrypted)

        print("File decrypted successfully.")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Invalid input. Please enter 'E' to encrypt or 'D' to decrypt.")
