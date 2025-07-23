print("ระบบคำนวณ  ประนีประนอม(สันติ) ")
Ranges = int ( input (" Please Type Your Distance "))

if (Ranges <= 5):
    print (" ERROR นะคะ ไปส่งเองเถอะค่ะ  ")
elif (Ranges < 51 ):
     print("Your deliver total is 10บาท")
elif (Ranges >= 51 and Ranges <= 100  ):
     print("  Your deliver total is 15บาท ")
elif (Ranges >= 101 and Ranges <= 300 ):
     print("  Your deliver total is 25บาท ")
elif (Ranges >= 301 and Ranges <= 500 ):
     print("  Your deliver total is 35บาท ")
elif (Ranges > 500 ):
     print("  Your deliver total is 45บาท ")
#I am sorry to be that you'd know but I never known that 