import os,sys,time

M = "\033[0;91m"
H = "\033[0;92m"
K = "\033[0;93m"
P = "\033[0m"

class Main:
	def __init__(self):
		self.infoo()
		
	def logoo(self):
		if "win" in sys.platform:os.system("cls")
		else:os.system("clear")
		print(f"""{M}●{K}●{H}●{P}                                      
\t®______   ______ _     _ _______ _______
\t |_____] |_____/ |     |    |    |______
\t |_____] |    \_ |_____|    |    |______
\t ____ ____ ____ ____ ___  ____ ____ _  _ 
\t |___ |__| |    |___ |__] |  | |  | |_/  
\t |    |  | |___ |___ |__] |__| |__| | \_ 
\t   ʜᴛᴛᴘs://ʜᴀᴍᴢᴀʜᴋɪʀᴀɴᴀ0.ɢᴏᴅᴀᴅᴅʏsɪᴛᴇs.ᴄᴏᴍ
\t                  ᴴᴬᴷᴵᴿᴬ""")
		
	def infoo(self):
		self.logoo()
		time.sleep(2)
		exit("\nScript Di Tutup\n\n")
		
Main()