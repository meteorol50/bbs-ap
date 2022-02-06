from cryptography.fernet import Fernet

def create_key() -> bytes:
  key = Fernet.generate_key()

  with open('key.key', 'wb') as file: #wb = write bytes
    file.write(key)

  return key

def encrypt(password: str) -> bytes:
  with open('key.key', 'rb') as file: # rb = read bytes
    key = file.read()
  if key.decode("utf-8") == "":
    key = create_key()

  f = Fernet(key)

  return f.encrypt(password.encode("utf-8"))

def decrypt(encrypted: bytes) -> str:
  with open('key.key', 'rb') as file: # rb = read bytes
    key = file.read()

  f = Fernet(key)

  return f.decrypt(encrypted).decode("utf-8")
