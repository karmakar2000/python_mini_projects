import pikepdf

old_pdf = pikepdf.Pdf.open("Deep Karmakar.pdf")

extract = pikepdf.Permissions(extract=False)
old_pdf.save("new_pdf.pdf",
             encryption=pikepdf.Encryption(user="123dk",
                                           owner="dk",
                                           allow=extract))