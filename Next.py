import configparser,subprocess,os,urllib.request,glob,sys
print("NEXT7 Mock")
print("Next Console")
store = configparser.ConfigParser()
store.read(f'store.ini')
repo = configparser.ConfigParser()
repo.read(f'repo.ini')
def vprint(s):
    [print(p) for p in s]
def install(app):
    try:
        d = store["Defalt"][app]
        urllib.request.urlretrieve(d,f"{app}.cario")
        print("Complite")
    except KeyError as e:
        print(f"{app}は存在しません")
def cmd(c):
    if c == "app-info":
        print("""Lang: Ja-Jp
        システムアプリケーション
        Sys 6.0
        Command-main 4
        日本語グローバルパッケージ
        Indas パッケージローダー
        下位互換性保持アプリケーション
        wastPhoneエミュレーター
        その他のアプリケーション
        Cario Client
        Next Module
        """)
    elif c == "Cario":
        print("""Cario 7.0
        Indas パッケージローダーと接続中....OK
        NPhoneエミュレーターと接続中....OK
        下位互換性保持アプリケーションと接続中....OK
        Shellを実行中....(キャッシュをクリア)OK
        Cario-Serverに接続中....OK
        Shellを実行中....OK
        Cario Client Moduleに接続中....OK
com.Cario.jp com.ZenOS.sus com.gigaos.sus com.astomos.sus com.indasos.sus com.dosbeta.sus com.next.susの著名が使用されています
Cario V7
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
            print("""com.astomos.sus com.gigaos.sus com.zenos.sus com.next.susの著名が使用されています
アプリ一覧""")
            for key in store['Defalt']:
                print(key)
            install(input("インストールするアプリ名>>"))

    elif c == "sus-com":
        print("""com.wast-system.Cario-client
com.Cario.jp
sus.localiz.jp
com.wastos.sus
com.ZenOS.sus
com.gigaos.sus
com.astomos.sus
com.redbox.sus
com.indasos.sus
com.dosbeta.sus
com.next.sus""")

def cario(a):
    print("""Cario Client Module
Loading......OK
""")
    print("Loading Repo")
    print("更新しています")
    for key in repo['Defalt']:
        r = repo["Defalt"][key]
        urllib.request.urlretrieve(r, f"store.ini")
        store.read(f'store.ini')
    install(a) 

while True:
    print("Execute exit when loading as a module")
    c = input(">>")
    if c == "system":
        print("""
    Next 7
    OS: Next
    Development codename: Mock
    Ver: 7
    Kernel: Indas-Next""")

    elif c == "boot":
        print("connected")
        while True:
            c = input(">>")
            cmd(c)
    elif c == "exit":
        break
    else:
        print("Not command")