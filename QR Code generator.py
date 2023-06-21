import qrcode as qr
img = qr.make("https://www.youtube.com/channel/UCQqL4xD0O3ezLORg4CSc5Pg")
img.save("dk_youtube.png")