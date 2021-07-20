import os
l = '''import configparser,subprocess,os,urllib.request,glob,sys,time
print("""One-Next 1.4 loading....""")
time.sleep(5)
store = configparser.ConfigParser()
store.read(f'store.ini')
repo = configparser.ConfigParser()
repo.read(f'repo.ini')
def vprint(s):
    [print(p) for p in s]
def install(app,pac):
    try:
        d = store["Defalt"][app]
        urllib.request.urlretrieve(d,f"{app}.{pac}")
        print("Complite")
    except KeyError as e:
        print(f"{app}は存在しません")
def cmd(c):
    if c == "app-info":
        print("""
        システムアプリケーション
        Open Media Application
        Pro8
        拡張機能
        Next-plus++
        """)
    elif c == "Cario":
        print("""Cario 8.0
アプリケーションの起動 = app
アプリケーションストアの起動 = store
        """)
        c = input(">>")
        if c == "app":
            print("インストール済みアプリケーション")
            file_list = glob.glob("./*.cario", recursive=True)
            file_list = [os.path.basename(r) for r in file_list]
            for x in file_list:
              print(x.replace('.cario', ''))
            s = input("起動するアプリケーションを入力>>")
            os.system(f"python {s}.cario")
        elif c == "store":
            print("更新しています")
            for key in repo['Defalt']:
                r = repo["Defalt"][key]
                urllib.request.urlretrieve(r, f"store.ini")
                store.read(f'store.ini')
            print("""
アプリ一覧""")
            for key in store['Defalt']:
                print(key)
            install(input("インストールするアプリ名>>"),"cario")
        
    elif c == "nam":
        print("""Nap Application Manager 10
アプリケーションの起動 = app
アプリケーションストアの起動 = store
        """)
        c = input(">>")
        if c == "app":
            print("インストール済みアプリケーション")
            file_list = glob.glob("./*.nap", recursive=True)
            file_list = [os.path.basename(r) for r in file_list]
            for x in file_list:
              print(x.replace('.nap', ''))
            s = input("起動するアプリケーションを入力>>")
            os.system(f"python {s}.nap")
        elif c == "store":
            print("更新しています")
            for key in repo['Defalt']:
                r = repo["Defalt"][key]
                urllib.request.urlretrieve(r, f"store.ini")
                store.read(f'store.ini')
            print("""
アプリ一覧""")
            for key in store['nap']:
                print(key)
            app = input("Select app>>")
            try:
                d = store["nap"][app]
                urllib.request.urlretrieve(d, f"appinfo.ini")
                irepo = configparser.ConfigParser()
                irepo.read(f'appinfo.ini')
                name = irepo["defalt"]["name"]
                ver = irepo["defalt"]["ver"]
                come = irepo["defalt"]["come"]
                url = irepo["defalt"]["url"]
                print(f"""Name: {name}
Ver.{ver}
comment:{come}""")
                urllib.request.urlretrieve(url, f"{name}.nap")
                print("Complite")
            except KeyError as e:
                print(f"{app}は存在しません")
    elif c == "nf":
        print("""Name: Defalt App
Publisher: NextOS-Developer
Support Ver: 21717(World)
Famous content: NEXTOS-DEVGLOUP-NEXT10-INSTALL-SOPPORT-FAMOUS
Issue ID: l2z-xcv-775-qx""")
    elif c == "system":
            print("""Next OS 10
Edition	 Next 10 home
update	 21717
OS build 10.7
Kernel   One-Next 21717.1.4 Nosmor
Famous: True""")


def cario(a):
    print("""NEXT8 Module Contloler
Loading......OK
""")
    print("Loading Repo")
    print("更新しています")
    for key in repo['Defalt']:
        r = repo["Defalt"][key]
        urllib.request.urlretrieve(r, f"store.ini")
        store.read(f'store.ini')
    install(a) 
if __name__ == "__main__":
    while True:
        c = "boot"
        print(">>login")
        if c == "boot":
            print("""
Welcome to NextOS 10
Web page:
dcom://www.next.com/OpenMedia/NextOS/10/
dcom://www.openmedia.com/nextos/Nosmor/
dcom://next.openmedia.com/10/
dcom://next.seccond.com/10/
Support 2021
amania Inc. 2015~2021
Next-SE 2021
openmedia 2021
OS: Next10 Nosmor NosmorEdition
Login protocol:Next-Login.nap
Video-Driver: NGD-3090
CPU-Driver: NPD-4600

            """)
            while True:
                c = input(">>")
                cmd(c)
        elif c == "exit":
            break
        else:
            print("Not command")'''
cn = """[Defalt]
defalt = https://github.com/amania-Gostd/Gostd/raw/main/store.ini
Ndynamic = https://github.com/amania-Gostd/NDynamic/raw/main/store.ini"""
print("Loading install.nap")
print("NextOS 10 インストーラー")
c = input("インストールしますか? y/n>")
if c == "y":
    print("インストール中")
    n = open("Next.py","w",encoding="UTF-8")
    repo = open("repo.ini","w",encoding="UTF-8")
    n.write(l)
    repo.write(cn)
    n.close()
    repo.close()
    print("読み込み中")
    os.system("Next.py")
