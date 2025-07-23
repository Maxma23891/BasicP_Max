import time
print("สวัสดีท่านผู้กล้า")
time.sleep(3)
print("ท่าน่าจะเดินทางมาไกลเลยสินะ")
time.sleep(3)
print("เตรียมสู้ซะไอ้ผู้กล้าโง่ เลือดข้า200 หรือ จะหนี ว่ะ55555")

pareetoo = 200 
selection = int (input("โปรดเลือก 1 สู้ หรือ 2 ออก")) 
player = 0
if selection == 1 :
   player = int(input ( "จะโจมตีเท่าไหร่"))
else:
    print ("Die" )
   
while  player > 0 : 
   weapon = int (input ("เลือกsaberกด 1 กดตัวเลข2 เพื่อไปเลือก (Sword)" ))
   if weapon == 1:
       pareetoo -= 40
       player -= 1
   elif weapon == 2 :
       sw = int (input ("เลือกsword กด 1 กดตัวเลข3 เพื่อใช้ Arrow)" ))
       pareetoo -= 15
       player -= 1
   else : 
    print("คุณเลือก arrow ทันที ")
    pareetoo -= 50 
    player -= 1
   print(pareetoo)
   if pareetoo == 0 : 
      print ("win")
   elif ( pareetoo < 0):
        print ("pareetoo ได้ฟื้นฟูเลือด")
        pareetoo = 20
if player == 0 :
  print( "you lose" )


 



     