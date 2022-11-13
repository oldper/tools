import qrcode

url = input("url?")
img = qrcode.make(url)
print(type(img))
img.save("qrcode.png")
print("done!")

