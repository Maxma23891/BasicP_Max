pareetoo = 200 
selection = int (input("โปรดเลือก 1 สู้ หรือ 2 ออก")) 
player = 0
if selection == 1 :
   player = int(input ( "จะโจมตีเท่าไหร่"))
else:
    print ("Die" )
   
while  player > 0 : 
   wea = int (input ("เลือกsaberกด 1" ))
   if wea == 1:
       pareetoo -= 40
       player -= 1
   elif wea == 0 :
       sw = int (input ("เลือกsword กด 1" ))
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
        pareetoo = 0+ 20

 



     