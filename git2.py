username = "Daspro2023"
password = "Latihan"

kesempatanLog = 3
print ("LOGIN!")
while kesempatanLog < 0 :
    usn = input (" username: ")
    pw = input (" password: ")

    if usn == username and pw == password :
        print (" login berhasil! selamat datang di lab komputer SMAN 2 Harapan")
        break
    else: 
        kesempatanLog -= 1
        if kesempatanLog > 0:
            print ("login salah! kesempatan {kesempatanLog}x lagi. ")
        else:
            print("kesempatan habis,anda tidak dapat login.")

username = "Daspro2023"
password = "Latihan"