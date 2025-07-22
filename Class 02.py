print("ระบบคำนวณ  ประนีประนอม(สันติ) ")
pint = int ( input (" Please Type Your Distance "))

if (pint <= 0):
    print (" ERROR นะคะ ไปส่งเองเถอะค่ะ  ")
elif (pint <= 51 ):
     print("Your deliver total is 10บาท")
elif (pint >= 51 and pint <= 100  ):
     print("  Your deliver total is 15บาท ")
elif (pint >= 101 and pint <= 300 ):
     print("  Your deliver total is 25บาท ")
elif (pint >= 301 and pint <= 500 ):
     print("  Your deliver total is 35บาท ")
elif (pint >= 500 ):
     print("  Your deliver total is 45บาท ")
