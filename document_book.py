import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
import json

# コールバック関数をネストして定義
def back3():
    p3.destroy()
   
    title()

def back2():
    r.destroy()
   
    title()

def back1():
    p4.destroy()
   
    title()
def printdata(w):
    def x():
        f=open('data.json',encoding="utf-8",mode='r')
        a=json.load(f)
        print("企業名>"+a[w]["企業名"])
        print("評価>"+a[w]["評価"])
        print("URL>"+a[w]["URL"])
        print("感想>"+a[w]["感想"])
        print("メモ>"+a[w]["メモ"])
        print("")
    return x
def page4(w):#企業の詳細
    def x():
        f=open('data.json',encoding="utf-8",mode='r')
        a=json.load(f)
        x=r.geometry()#参照
        r.destroy()
        global p4
        p4 = tk.Tk()
        p4.geometry(x)
        p4.title("詳細")
        

        

        lab1 = tk.Message(p4,text="企業名>"+a[w]["企業名"], font=("",15),width=700)
        lab1.place(x=20, y=50)

        lab2 = tk.Message(p4,text="評価>"+a[w]["評価"], font=("",15),width=700)
        lab2.place(x=20, y=100)
        
        lab4 = tk.Message(p4,text="URL>"+a[w]["URL"], font=("",15),width=700)
        lab4.place(x=20, y=150)


        lab3 = tk.Message(p4,text="感想>"+a[w]["感想"], font=("",15),width=700)
        lab3.place(x=20, y=220)
        
        lab3 = tk.Message(p4,text="メモ>"+a[w]["メモ"], font=("",15),width=700)
        lab3.place(x=20, y=290)

        bot1 = tk.Button(p4, text="戻る", font=("",10), width=10,command=back1)
        bot1.place(x=100, y=450)
        
        bot2 = tk.Button(p4, text="出力", font=("",10), width=10,command=printdata(w))
        bot2.place(x=300, y=450)


    return x

def bot1_1():#jsonに追加するボタン
    import json
    f=open('data.json', encoding="utf-8",mode='r')
    
    a=json.load(f)
    i=int(len(a))
    #name=input()
    a[i+1]={"企業名":txt1.get(),"評価":txt2.get(),"URL":txt5.get(),"感想":txt3.get(),"メモ":txt4.get()}
    path = "data.json"

    with open(path, encoding="utf-8", mode="w") as f:
         json.dump(a, f, ensure_ascii=False, indent=2)
    f.close()

def page3():#追加
    x=root.geometry()
    root.destroy()
    global p3
    p3 = tk.Tk()
    p3.geometry(x)
    p3.title("追加")
        
    lab1 = tk.Label(p3,text="企業名", font=("",20))
    lab1.place(x=20, y=50)
    lab2 = tk.Label(p3,text="評価", font=("",20))
    lab2.place(x=20, y=100)
    
    lab2 = tk.Label(p3,text="URL", font=("",20))
    lab2.place(x=20, y=150)


    lab2 = tk.Label(p3,text="感想", font=("",20))
    lab2.place(x=20, y=220)
    lab3 = tk.Label(p3,text="メモ", font=("",20))
    lab3.place(x=20, y=290)
    
    #タイトル画像
    t = tk.PhotoImage(file="title.PNG")
    canvas = tk.Canvas(width=800, height=100)
    canvas.place(x=100, y=450)
    canvas.create_image(0, 0, image=t, anchor=tk.NW)
    
    #テキストボックス
    global txt1,txt2,txt3,txt4,txt5
    txt1 = tk.Entry(p3,font=("",20), width=20)
    txt1.place(x=100, y=50)
    txt2 = tk.Entry(p3,font=("",20), width=15)
    txt2.place(x=100, y=100)
    txt3 = tk.Entry(p3,font=("",20), width=50)
    txt3.place(x=100, y=150)
    txt4 = tk.Entry(p3,font=("",20), width=50)
    txt4.place(x=100, y=220)
    txt5 = tk.Entry(p3,font=("",20), width=50)
    txt5.place(x=100, y=290)

   #ボタン
    bot1 = tk.Button(p3, text="追加", font=("",15), width=10,height=3,command=bot1_1)
    bot1.place(x=100, y=350)

    bot2 = tk.Button(p3, text="終了", font=("",15), width=10,height=3,command=exit)
    bot2.place(x=250, y=350)

    bot3 = tk.Button(p3, text="戻る", font=("",15), width=10,height=3,command=back3)
    bot3.place(x=400, y=350)
    


    p3.mainloop()


def page2():#参照
    x=root.geometry()
    root.destroy()
    global r
    r = tk.Tk()
    r.geometry(x)
    r.title("企業一覧")


    canvas = tk.Canvas(r, width=800, height=600)
    frame = tk.Frame(canvas)

    f=open('data.json',encoding="utf-8",mode='r')
    a=json.load(f)
    for w in a:
       b = tk.Button(frame,text="企業名:"+a[w]["企業名"]+" , 評価:"+a[w]["評価"],font=15,width=45,command=page4(w))
       b.pack(pady=10)

    # スクロールバーの配置
    hbar = tk.Scrollbar(r, orient=tk.HORIZONTAL)
    hbar.config(command=canvas.xview)
    hbar.pack(side=tk.BOTTOM, fill=tk.X)
    vbar = tk.Scrollbar(r, orient=tk.VERTICAL)
    vbar.config(command=canvas.yview)
    vbar.pack(side=tk.RIGHT,fill=tk.Y)

    canvas.create_window(0, 0, window=frame)
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.update_idletasks()

    canvas.config(
      scrollregion=canvas.bbox("all"),
      xscrollcommand=hbar.set,
      yscrollcommand=vbar.set)
 # スクロールバー位置のリセット
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)

    f=open('data.json',encoding="utf-8",mode='r')
    a=json.load(f)
    bot3 = tk.Button(r, text="戻る", font=("",18), width=3,command=back2)
    bot3.place(x=550, y=450)
    
    
   
    

    
    
    r.mainloop()

def title():
 global root
 root= tk.Tk()
 root.geometry("800x600")
 #タイトル画像
 t = tk.PhotoImage(file="title.PNG")
 canvas = tk.Canvas(width=800, height=100)
 canvas.place(x=70, y=200)
 canvas.create_image(0, 0, image=t, anchor=tk.NW)
    
 button1 = tk.Button(text = '参照',font=20,command=page2).place(x = 50, y  = 450,width=200,height=50)
 button2 = tk.Button(text = '追加',font=20,command=page3).place(x = 300, y = 450,width=200,height=50)
 button3 = tk.Button(text = '終了',font=20,command=exit).place(x = 550, y = 450,width=200,height=50)
    #tl.mainloop()



 root.mainloop()

title()
