print("auif UPloder Ver.12")
print("AUIFファイルを使用してアップデートをします")
import configparser
import codecs
import urllib.request
def ini(v):
    i = f'''[Defalt]
application = True
Unsignedapplication = false
nostoreapp = false
appcmd = None
Ver = {v}
AUP = True'''
    return i
def install(app):
    try:
        if app == "new":
            d = open("new.aup","r",encoding="utf-8")
            d = d.read()
            s = open("DOS.py","w",encoding="utf-8")
            s.write(d)
            s.close()
            s = open("config.ini","w",encoding="utf-8")
            s.write(ini(aup["Defalt"]["New-Ver"]))
            s.close()
        else:
            d = config["Defalt"][app]
            urllib.request.urlretrieve(d, "Next.py")
            a = ini(app)
            s = open("config.ini","w",encoding="utf-8")
            s.write(a)
            s.close()
    except KeyError as e:
        print(f"{app}は存在しません")
print("使用可能なAUIFを検索しています")
urllib.request.urlretrieve("https://raw.githubusercontent.com/amania-Gostd/Gostd/main/update.ini", "ST/system/update.ini")
config = configparser.ConfigParser()
aup = configparser.ConfigParser()
###config.read('update.ini')
config.readfp(codecs.open("ST/system/update.ini", "r", "utf8"))
aup.readfp(codecs.open("ST/system/aup.ini", "r", "utf8"))
print("ダウンロードするバージョンを選択してください(Ver.10.2以上のみ使用できます)")
for key in config['Defalt']:
    print(key)
c = input(">>")
install(c)


