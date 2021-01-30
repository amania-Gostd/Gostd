print("auif UPloder Ver.10")
print("AUIFファイルを使用してアップデートをします")
import configparser
import codecs
import urllib.request
def install(app):
    try:
        open("test.py","w")
        d = config["Defalt"][app]
        urllib.request.urlretrieve(d, "DOS.py")
    except KeyError as e:
        print(f"{app}は存在しません")
print("使用可能なAUIFを検索しています")
urllib.request.urlretrieve("https://github.com/amzon-0021/store/raw/main/update.ini", "update.ini")
config = configparser.ConfigParser()
###config.read('update.ini')
config.readfp(codecs.open("update.ini", "r", "utf8"))
print("ダウンロードするバージョンを選択してください(Ver.10.2以上のみ使用できます)")
for key in config['Defalt']:
    print(key)
c = input(">>")
install(c)


