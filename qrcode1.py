import qrcode
# qr=qrcode.make("https://www.youtube.com/")

# qr.save("youtube.png")
# qr=qrcode.make("hello, manik reddy")
# qr.save("manik.png")
# qr.show()

qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name=input("Enter your name: ")
age=int(input("Enter your age: "))
email=input("Enter your email: ")
mobile=int(input("Enter your mobile number: "))
data={"name":name,"age":age,"email":email,"mobile":mobile}
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save("details.png")
img.show()