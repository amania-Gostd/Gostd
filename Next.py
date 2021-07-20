print("Next Login Manager")
print("初期化(s) ログイン(y) 新規ユーザー(n)")
import configparser,subprocess,os,urllib.request,glob,sys,time
us = configparser.ConfigParser()
us.read(f'user.ini')
l = '''import configparser,subprocess,os,urllib.request,glob,sys,time
print("""One-Next 2 loading....""")
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
        print("""Cario 9.0
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
        print("""Nap Application Manager 11
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
Support Ver: 21720(Dev)
Famous content: NEXTOS-DEV-EDITION
Issue ID: xcv-667-qx7""")
    elif c == "system":
            print("""Next OS 11
Edition	 Next 11 Developer
update	 21720
OS build 10.7
Kernel   One-Next 21720.2 basics
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
    print("ONE-Next 2 Beta")
    while True:
        c = "Login"
        if c == "Login":
            print("""
Welcome to NextOS 11
Web page:
dcom://www.next.com/OpenMedia/NextOS/11/
dcom://www.openmedia.com/nextos/onenext/2
dcom://next.openmedia.com/11/
dcom://next.seccond.com/11/
Support 2021
amania Inc. 2015~2021
Next-SE 2021
openmedia 2021
OS: Next 11 Dev
Login protocol: XNLM
Video-Driver: NVD
CPU-Driver: NCD

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
def vprint(s):
    [print(p) for p in s]
while True:
    c = input(">")
    if c == "s":
        print("Deleteing User 実行するとユーザーの中にあるすべてのファイルが消去されます")
        os.system("rmdir /s USER")
        u = input("ユーザー名の入力>")
        print("作成中")
        os.system(f"mkdir USER\{u}")
        print("Installing NextOS")
        n = open(f"USER/{u}/Next.py", "w", encoding='UTF-8')
        n.write(l)
        n.close()
        print("Setting repo")
        dd = open(f"USER/{u}/repo.ini", "w", encoding='UTF-8')
        dd.write(cn)
        dd.close()
        print("Complited")
        cnf = open("user.ini", "w", encoding='UTF-8')
        cnf.write(f"""[Defalt]
{u} = USER\{u}""")
        cnf.close()
    elif  c == "y":
        us = configparser.ConfigParser()
        us.read(f'user.ini')
        for us in us['Defalt']:
            print(us)
        u = input("USER-SELECT>>")
        os.system(f"cd USER\{u} && python Next.py")
    elif c == "n":
        u = input("ユーザー名の入力>")
        print("作成中")
        os.system(f"mkdir USER\{u}")
        print("Installing NextOS")
        n = open(f"USER/{u}/Next.py", "w", encoding='UTF-8')
        n.write(l)
        n.close()
        print("Setting repo")
        dd = open(f"USER/{u}/repo.ini", "w", encoding='UTF-8')
        dd.write(cn)
        dd.close()
        us.read(f'user.ini')
        print("Complited")
        cnf = open("user.ini", "w", encoding='UTF-8')
        cnf.write(f"""[Defalt]
{u} = USER\{u}""")
        cnf.close()
    
