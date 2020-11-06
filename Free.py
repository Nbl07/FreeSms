#kang recode minggir asw_-
#bikin nya mudah asw jangan Recode punya orang_-
import requests,time,os

class Payu:
	def __init__(self):
		self.u='https://nuubi.herokuapp.com/api/smsgratis'
		self.banner()

	def banner(self):
		os.system('clear')
		print('''
___________________
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
  ╔════════════╗
  ╚════════════╝
   ║██████████╚╗
   ║██╔══╗█╔═╗█║                   Sms Geratis
   ║██║╬╔╝█╚╗║█║          <=============X=============>
   ║██╚═╝█║█╚╝█║               Pembuat : ./Nbl•⁰⁷
   ╚╗█████████═╝               Team : Malaikat Tak Bersayap
    ╚╗║╠╩╩╩╩╩╝                 pesan : lain kali modal dikit anjim:v
     ║║┈┈┈█▐███████▒.｡oO
     ║██╠╦╦╦╗
     ╚╗██████    ©copyright_2020-2021
      ╚════╝
                 Nb : Yang Recode Gue Doain K*NT*L Nya Putus:v
                 
<=============X=============>''')
		no=input('[?] Nomor Tujuan (85****): ')
		psn=input('[perhatian] minimal 15 huruf cuy [?] isi pesan: ')
		self.main(no,psn)

	def main(self,no,msg):
		sub=requests.post("https://nuubi.herokuapp.com/api/smsgratis",
			data={'number': no, 'pesan': msg}).json()
		if sub['status'] == 'ok':
			print(f"[#] {sub['msg']}")
		else:
			print(f"[#] {sub['msg']}")

try:
	Payu()
	while True:
		plh=input("\n[?] kirim lagi bos (y/n) ")
		if plh.lower() == 'y':
			Payu()
		elif plh.lower() == 'n':
			exit('udah puas stah:v')
except KeyboardInterrupt:
	print('\nErr: KeyboardInterrupt')
except Exception as E:
	print('Err: %s'%(E))
