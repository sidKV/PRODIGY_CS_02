# -*- coding: utf-8 -*-
"""Intership.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ot0KpvOR4Lh6XhY-zWMKtVfrBnsej4Yz
"""


from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    # Encrypt by modifying each pixel using the key
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save("encrypted_DOG.png")
    print("Image encrypted and saved as 'encrypted_DOG.png'.")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    # Decrypt by reversing the encryption process using the same key
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save("decrypted_DOG.png")
    print("Image decrypted and saved as 'decrypted_DOG.png'.")

def main():
    image_path = "/mnt/data/DOG.jfif"
    key = int(input("Enter the encryption/decryption key (integer value): "))

    encrypt_image(image_path, key)
    decrypt_image("encrypted_DOG.png", key)

if __name__ == "__main__":
    main()
