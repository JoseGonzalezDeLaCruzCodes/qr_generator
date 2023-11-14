import qrcode

img = qrcode.make('https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/')
type(img)
img.save("Qr_code.png")