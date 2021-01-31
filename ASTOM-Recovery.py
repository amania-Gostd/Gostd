import time
import configparser
import codecs
import urllib.request
import shutil
import os
time.sleep(5)
def ini(v):
    i = f'''[Defalt]
application = True
Unsignedapplication = false
nostoreapp = false
appcmd = None
Ver = {v}'''
    return i
def install(app):
    try:
        open("test.py","w")
        d = config["Defalt"][app]
        urllib.request.urlretrieve(d, "DOS.py")
        a = ini(app)
        s = open("config.ini","w")
        s.write(a)
        s.close()
    except KeyError as e:
        print(f"{app}は存在しません")
print("ASTOM-Recovery Build G7TEL")
print("""===================Recovery Menu===================

i = ASTOMインストーラー
s = OPAStoreの設定ファイルを更新
dos = ASTOM-OSを起動します
a = 初期化
""")
c = input(">>>")
if c == "i":
    print("実行するとDOS-Build15TERがインストールされます")
    d = input("実行するには、yを入力してください")
    if d == "y":
        print("インストールしています")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/amania-Gostd/Gostd/main/update.ini", "update.ini")
        config = configparser.ConfigParser()
        config.readfp(codecs.open("update.ini", "r", "utf8"))
        install("10.5.8")
    else:
        pass
elif c == "s":
    print("アップデート中.......")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/amania-Gostd/Gostd/main/store.ini", "store.ini")
    print("完了")
    pass
elif c == "dos":
    import os
    os.system("DOS.py")
elif c == "a":
    print("初期化しています")
    config = configparser.ConfigParser()
    config.readfp(codecs.open("config.ini", "r", "utf8"))
    v = config["Defalt"]["Ver"]
    urllib.request.urlretrieve(f"https://raw.githubusercontent.com/amania-Gostd/Gostd/main/{v}.AUIF","DOS.py")
    target_dir = 'app'
    shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    a = ini(v)
    s = open("config.ini","w")
    s.write(a)
    s.close()
    print("Finish")
    
