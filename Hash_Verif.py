import hashlib

# file path input from user
file_path = input("Enter the file path: ")

try:
    with open(file_path, "rb") as f:
        file_data = f.read()
        sha256 = hashlib.sha256(file_data).hexdigest()
        sha512 = hashlib.sha512(file_data).hexdigest()
        md5 = hashlib.md5(file_data).hexdigest()

        print(f"SHA-256: {sha256}")
        print(f"SHA-512: {sha512}")
        print(f"MD5: {md5}")

except FileNotFoundError:
    print("File not found. Please check the path and try again.")
except Exception as e:
    print(f"Error : {e}")
