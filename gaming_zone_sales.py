from tkinter import *
from tkinter import messagebox
import random
import time
import datetime
import tempfile,os


root=Tk()
root.geometry("1350x700+0+0")
root.title("sales tracking")
root.configure(background="white")

Top=Frame(root,width=1350,height=20,bd=14,relief="raise")
Top.pack(side=TOP)

f1=Frame(root,width=900,height=500,bd=8,relief="raise")
f1.pack(side=LEFT)

f2=Frame(root,width=440,height=500,bd=8,relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1,width=900,height=350,bd=8,relief="raise")
f1a.pack(side=TOP)

f2a=Frame(f1,width=900,height=150,bd=6,relief="raise")
f2a.pack(side=BOTTOM)

ft2=Frame(f2,width=440,height=350,bd=12,relief="raise")
ft2.pack(side=TOP)
fb2=Frame(f2,width=440,height=150,bd=16,relief="raise")
fb2.pack(side=BOTTOM)

f1aa=Frame(f1a,width=900,height=350,bd=8,relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a,width=900,height=350,bd=8,relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a,width=450,height=150,bd=8,relief="raise")
f2aa.pack(side=LEFT)

f2ab=Frame(f2a,width=450,height=150,bd=8,relief="raise")
f2ab.pack(side=RIGHT)

Top.configure(background='black')
f1.configure(background='white')
f2.configure(background='white')

lblInfo=Label(Top,font=('arial',40,'bold'),text="Sales Management System \t", bd=10)
lblInfo.grid(row=0,column=0)

#===========================functions=====================================
def qExit():
    qExit=messagebox.askyesno("Quit System","Do you want to quit?")
    if qExit >0:
        root.destroy()
        return


def iPrint():
    q=txtReceipt.get("1.0","end-1c")
    filename=tempfile.mktemp(".txt")
    open(filename,"w").write(q)
    os.startfile(filename,"print")



def Receipt():
    txtReceipt.delete("1.0",END)
    y=random.randint(10908,500876)
    randomRef=str(y)
    Receipt_ref.set("POS"+randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_ref.get()+"\t\t"+Dateoforder.get()+"\n\n")
    txtReceipt.insert(END,"Items\t\t\t\t\t"+"Cost of Rides"+"\n")
    if var1.get() ==1 :
        p1=int(E_basketball.get())
        price1= p1*100
        txtReceipt.insert(END,'King Basketball\t\t\t\t\t'+str(price1)+" BDT\n")
    if var2.get() ==1 :
        p2=int(E_tt_car.get())
        price2= p2*100
        txtReceipt.insert(END,'MANX TT Car\t\t\t\t\t'+str(price2)+" BDT\n")
    if var3.get() ==1 :
        p3=int(E_tt_moto.get())
        price3= p3*100
        txtReceipt.insert(END,'MANX TT Moto \t\t\t\t\t'+str(price3)+" BDT\n")
    if var4.get() ==1 :
        p4=int(E_train.get())
        price4= p4*100
        txtReceipt.insert(END,'Happy Train \t\t\t\t\t'+str(price4)+" BDT\n")
    if var5.get() ==1 :
        p5=int(E_kids_moto.get())
        price5= p5*100
        txtReceipt.insert(END,'Kids Moto \t\t\t\t\t'+str(price5)+" BDT\n")
    if var6.get() ==1 :
        p6=int(E_kids_ufo.get())
        price6= p6*100
        txtReceipt.insert(END,'Kids  Ufoo \t\t\t\t\t'+str(price6)+" BDT\n")
    if var7.get() ==1 :
        p7=int(E_foot_ninja.get())
        price7= p7*100
        txtReceipt.insert(END,'Foot Ninja \t\t\t\t\t'+str(price7)+" BDT\n")
    if var8.get() ==1 :
        p8=int(E_king_hammer.get())
        price8= p8*100
        txtReceipt.insert(END,'king Hammer \t\t\t\t\t'+str(price8)+" BDT\n")
    if var9.get() ==1 :
        p9=int(E_flying_dragon.get())
        price9= p9*100
        txtReceipt.insert(END,'Flying Dragon \t\t\t\t\t'+str(price9)+" BDT\n")
    if var10.get() ==1 :
        p10=int(E_royal_carriage.get())
        price10= p10*100
        txtReceipt.insert(END,'Royal Carriage \t\t\t\t\t'+str(price10)+" BDT\n")
    if var11.get() ==1 :
        p11=int(E_hunting_hero.get())
        price11= p11*100
        txtReceipt.insert(END,'Hunting Hero \t\t\t\t\t'+str(price11)+" BDT\n")
    if var12.get() ==1 :
        p12=int(E_ocean_cariusel.get())
        price12= p12*100
        txtReceipt.insert(END,'Ocean Carousel \t\t\t\t\t'+str(price12)+" BDT\n")
    if var13.get() ==1 :
        p13=int(E_furious_car.get())
        price13= p13*100
        txtReceipt.insert(END,'Furious Car \t\t\t\t\t'+str(price13)+" BDT\n")
    if var14.get() ==1 :
        p14=int(E_air_hockey.get())
        price14= p14*100
        txtReceipt.insert(END,'Air Hockey \t\t\t\t\t'+str(price14)+" BDT\n")
    if var15.get() ==1 :
        p15=int(E_drifting_car.get())
        price15= p15*200
        txtReceipt.insert(END,'Drifting Car \t\t\t\t\t'+str(price15)+" BDT\n")
    if var16.get() ==1 :
        p16=int(E_kids_world.get())
        price16= p16*200
        txtReceipt.insert(END,'Kids World \t\t\t\t\t'+str(price16)+" BDT\n")
    if var17.get() ==1 :
        p17=int(E_robo_bot.get())
        price17= p17*200
        txtReceipt.insert(END,'Robo Bot \t\t\t\t\t'+str(price17)+" BDT\n")
    if var18.get() ==1 :
        p18=int(E_vr_games.get())
        price18= p18*200
        txtReceipt.insert(END,'VR Games \t\t\t\t\t'+str(price18)+" BDT\n")
    if var19.get() ==1 :
        p19=int(E_balance_cart.get())
        price19= p19*200
        txtReceipt.insert(END,'Balance Cart \t\t\t\t\t'+str(price19)+" BDT\n")
    if var20.get() ==1 :
        p20=int(E_relax_chair.get())
        price20= p20*200
        txtReceipt.insert(END,'Relax Chair \t\t\t\t\t'+str(price20)+" BDT\n")
    txtReceipt.insert(END,"-----------------------------------------------------------\n")
    r1=TotalPrice.get().replace("(","")
    r1=r1.replace(")","")
    r1=r1.split(",")
    result1=r1[1]
    result1=result1[2:-1]
    txtReceipt.insert(END,'Price in total\t\t\t\t\t'+result1+" BDT\n")
    if Discount.get() != "0":
        txtReceipt.insert(END,"Discounted Percentage: \t\t\t\t\t"+Discount.get()+"\n")
        r2=NetPrice.get().replace("(","")
        r2=r2.replace(")","")
        r2=r2.split(",")
        result2=r2[1]
        result2=result2[2:-1]
        txtReceipt.insert(END,"Current Net price:\t\t\t\t\t"+result2+" BDT\n")






def Total_calculation():
    item1= int (E_basketball.get())
    item2= int (E_tt_car.get())
    item3= int (E_tt_moto.get())
    item4= int (E_train.get())
    item5= int (E_kids_moto.get())
    item6= int (E_kids_ufo.get())
    item7= int (E_foot_ninja.get())
    item8= int (E_king_hammer.get())
    item9= int (E_flying_dragon.get())
    item10= int (E_royal_carriage.get())
    item11= int (E_hunting_hero.get())
    item12= int (E_ocean_cariusel.get())
    item13= int (E_furious_car.get())
    item14= int (E_air_hockey.get())
    item15= int (E_drifting_car.get())
    item16= int (E_kids_world.get())
    item17= int (E_robo_bot.get())
    item18= int (E_vr_games.get())
    item19= int (E_balance_cart.get())
    item20= int (E_relax_chair.get())

    total_costings=(item1*100)+(item2*100)+(item3*100)+(item4*100)+(item5*100)+(item6*100)+(item7*100)+(item8*100)\
        +(item9*100)+(item10*100)+(item11*100)+(item12*100)+(item13*100)+(item14*100)+(item15*200)+(item16*200)\
            +(item17*200)+(item18*200)+(item19*200)+(item20*200)
    xx1=float(Discount.get())
    discounted_value= float((total_costings*xx1)/100)
    total_net_price= float (total_costings-discounted_value)
    valueoftotalprice= "BDT", str('%.2f'%(total_costings))
    valueofnetprice= "BDT", str('%.2f'%(total_net_price))
    TotalPrice.set(valueoftotalprice)
    NetPrice.set(valueofnetprice)


#======================checkbutton===========================
def checkbutton_value():
    if(var1.get()==1):
        txt_basketball.configure(state=NORMAL)
    elif var1.get()==0 :
        txt_basketball.configure(state=DISABLED)
        E_basketball.set("0")
    if(var2.get()==1):
        txt_tt_car.configure(state=NORMAL)
    elif var2.get()==0 :
        txt_tt_car.configure(state=DISABLED)
        E_tt_car.set("0")
    if(var3.get()==1):
        txt_tt_moto.configure(state=NORMAL)
    elif var3.get()==0 :
        txt_tt_moto.configure(state=DISABLED)
        E_tt_moto.set("0")
    if(var4.get()==1):
         txt_train.configure(state=NORMAL)
    elif var4.get()==0 :
        txt_train.configure(state=DISABLED)
        E_train.set("0")
    if(var5.get()==1):
        txt_kids_moto.configure(state=NORMAL)
    elif var5.get()==0 :
        txt_kids_moto.configure(state=DISABLED)
        E_kids_moto.set("0")
    if(var6.get()==1):
        txt_kids_ufo.configure(state=NORMAL)
    elif var6.get()==0 :
        txt_kids_ufo.configure(state=DISABLED)
        E_kids_ufo.set("0")
    if(var7.get()==1):
        txt_foot_ninja.configure(state=NORMAL)
    elif var7.get()==0 :
        txt_foot_ninja.configure(state=DISABLED)
        E_foot_ninja.set("0")
    if(var8.get()==1):
        txt_king_hammer.configure(state=NORMAL)
    elif var8.get()==0 :
        txt_king_hammer.configure(state=DISABLED)
        E_king_hammer.set("0")
    if(var9.get()==1):
        txt_flying_dragon.configure(state=NORMAL)
    elif var9.get()==0 :
        txt_flying_dragon.configure(state=DISABLED)
        E_flying_dragon.set("0")
    if(var10.get()==1):
        txt_royal_carriage.configure(state=NORMAL)
    elif var10.get()==0 :
        txt_royal_carriage.configure(state=DISABLED)
        E_royal_carriage.set("0")
    if(var11.get()==1):
        txt_hunting_hero.configure(state=NORMAL)
    elif var11.get()==0 :
        txt_hunting_hero.configure(state=DISABLED)
        E_hunting_hero.set("0")
    if(var12.get()==1):
        txt_ocean_cariusel.configure(state=NORMAL)
    elif var12.get()==0 :
        txt_ocean_cariusel.configure(state=DISABLED)
        E_ocean_cariusel.set("0")
    if(var13.get()==1):
        txt_furious_car.configure(state=NORMAL)
    elif var13.get()==0 :
        txt_furious_car.configure(state=DISABLED)
        E_furious_car.set("0")
    if(var14.get()==1):
        txt_air_hockey.configure(state=NORMAL)
    elif var14.get()==0 :
        txt_air_hockey.configure(state=DISABLED)
        E_air_hockey.set("0")
    if(var15.get()==1):
        txt_drifting_car.configure(state=NORMAL)
    elif var15.get()==0 :
        txt_drifting_car.configure(state=DISABLED)
        E_drifting_car.set("0")
    if(var16.get()==1):
        txt_kids_world.configure(state=NORMAL)
    elif var16.get()==0 :
        txt_kids_world.configure(state=DISABLED)
        E_kids_world.set("0")
    if(var17.get()==1):
        txt_robo_bot.configure(state=NORMAL)
    elif var17.get()==0 :
        txt_robo_bot.configure(state=DISABLED)
        E_robo_bot.set("0")
    if(var18.get()==1):
        txt_vr_games.configure(state=NORMAL)
    elif var18.get()==0 :
        txt_vr_games.configure(state=DISABLED)
        E_vr_games.set("0")
    if(var19.get()==1):
        txt_balance_cart.configure(state=NORMAL)
    elif var19.get()==0 :
        txt_balance_cart.configure(state=DISABLED)
        E_balance_cart.set("0")
    if(var20.get()==1):
        txt_relax_chair.configure(state=NORMAL)
    elif var20.get()==0 :
        txt_relax_chair.configure(state=DISABLED)
        E_relax_chair.set("0")
#=============================================================

def Reset():
    txtReceipt.delete("1.0",END)
    TotalPrice.set("")
    Discount.set("0")
    NetPrice.set("")
    E_basketball.set("0")
    E_tt_car.set("0")
    E_tt_moto.set("0")
    E_train.set("0")
    E_kids_moto.set("0")
    E_kids_ufo.set("0")
    E_foot_ninja.set("0")
    E_king_hammer.set("0")
    E_flying_dragon.set("0")
    E_royal_carriage.set("0")
    E_hunting_hero.set("0")
    E_ocean_cariusel.set("0")
    E_furious_car.set("0")
    E_air_hockey.set("0")
    E_drifting_car.set("0")
    E_kids_world.set("0")
    E_robo_bot.set("0")
    E_vr_games.set("0")
    E_balance_cart.set("0")
    E_relax_chair.set("0")
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    txt_basketball.configure(state=DISABLED)
    txt_tt_car.configure(state=DISABLED)
    txt_tt_moto.configure(state=DISABLED)
    txt_train.configure(state=DISABLED)
    txt_kids_moto.configure(state=DISABLED)
    txt_kids_ufo.configure(state=DISABLED)
    txt_foot_ninja.configure(state=DISABLED)
    txt_king_hammer.configure(state=DISABLED)
    txt_flying_dragon.configure(state=DISABLED)
    txt_royal_carriage.configure(state=DISABLED)
    txt_hunting_hero.configure(state=DISABLED)
    txt_ocean_cariusel.configure(state=DISABLED)
    txt_furious_car.configure(state=DISABLED)
    txt_air_hockey.configure(state=DISABLED)
    txt_drifting_car.configure(state=DISABLED)
    txt_kids_world.configure(state=DISABLED)
    txt_robo_bot.configure(state=DISABLED)
    txt_vr_games.configure(state=DISABLED)
    txt_balance_cart.configure(state=DISABLED)
    txt_relax_chair.configure(state=DISABLED)


    

#===========================variables=====================================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()


Dateoforder=StringVar()
Receipt_ref=StringVar()
TotalPrice=StringVar()
Discount=StringVar()
NetPrice=StringVar()

E_basketball=StringVar()
E_tt_car=StringVar()
E_tt_moto=StringVar()
E_train=StringVar()
E_kids_moto=StringVar()
E_kids_ufo=StringVar()
E_foot_ninja=StringVar()
E_king_hammer=StringVar()
E_flying_dragon=StringVar()
E_royal_carriage=StringVar()
E_hunting_hero=StringVar()
E_ocean_cariusel=StringVar()
E_furious_car=StringVar()
E_air_hockey=StringVar()
E_drifting_car=StringVar()
E_kids_world=StringVar()
E_robo_bot=StringVar()
E_vr_games=StringVar()
E_balance_cart=StringVar()
E_relax_chair=StringVar()

Discount.set("0")
E_basketball.set("0")
E_tt_car.set("0")
E_tt_moto.set("0")
E_train.set("0")
E_kids_moto.set("0")
E_kids_ufo.set("0")
E_foot_ninja.set("0")
E_king_hammer.set("0")
E_flying_dragon.set("0")
E_royal_carriage.set("0")
E_hunting_hero.set("0")
E_ocean_cariusel.set("0")
E_furious_car.set("0")
E_air_hockey.set("0")
E_drifting_car.set("0")
E_kids_world.set("0")
E_robo_bot.set("0")
E_vr_games.set("0")
E_balance_cart.set("0")
E_relax_chair.set("0")



Dateoforder.set(time.strftime("%d/%m/%Y %H:%M:%S"))

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")
var17.set("0")
var18.set("0")
var19.set("0")
var20.set("0")

#=================================column1========================================================
basketball=Checkbutton(f1aa,text="King Basketball \t",variable=var1,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=0,column=0)
tt_car=Checkbutton(f1aa,text="MANX TT Car \t",variable=var2,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=1,column=0)
tt_moto=Checkbutton(f1aa,text="MANX TT Moto \t",variable=var3,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=2,column=0)
train=Checkbutton(f1aa,text="Happy Train \t",variable=var4,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=3,column=0)
kids_moto=Checkbutton(f1aa,text="Kids Moto \t",variable=var5,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=4,column=0)
kids_ufo=Checkbutton(f1aa,text="Kids  Ufoo \t",variable=var6,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=5,column=0)
foot_ninja=Checkbutton(f1aa,text="Foot Ninja \t",variable=var7,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=6,column=0)
king_hammer=Checkbutton(f1aa,text="King Hammer \t",variable=var8,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=7,column=0)
flying_dragon=Checkbutton(f1aa,text="Flying Dragon \t",variable=var9,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=8,column=0)
royal_carriage=Checkbutton(f1aa,text="Royal Carriage \t",variable=var10,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=9,column=0)
#=================================column2========================================================
hunting_hero=Checkbutton(f1ab,text="Hunting Hero \t",variable=var11,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=0,column=0)
ocean_cariusel=Checkbutton(f1ab,text="Ocean Carousel \t",variable=var12,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=1,column=0)
furious_car=Checkbutton(f1ab,text="Furious Car \t",variable=var13,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=2,column=0)
air_hockey=Checkbutton(f1ab,text="Air Hockey \t",variable=var14,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=3,column=0)
drifting_car=Checkbutton(f1ab,text="Drifting Car \t",variable=var15,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=4,column=0)
kids_world=Checkbutton(f1ab,text="Kids World \t",variable=var16,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=5,column=0)
robo_bot=Checkbutton(f1ab,text="Robotic Bot \t",variable=var17,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=6,column=0)
vr_games=Checkbutton(f1ab,text="VR Games \t",variable=var18,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=7,column=0)
balance_cart=Checkbutton(f1ab,text="Balance Cart \t",variable=var19,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=8,column=0)
relax_chair=Checkbutton(f1ab,text="Relax Chair \t",variable=var20,onvalue=1,offvalue=0, font=('arial',18,'bold'),command=checkbutton_value).grid(row=9,column=0)

#=================================enter widget for column1========================================================
txt_basketball=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,textvariable=E_basketball ,justify='left', state=DISABLED)
txt_basketball.grid(row=0,column=1)
txt_tt_car=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,textvariable=E_tt_car , justify='left', state=DISABLED)
txt_tt_car.grid(row=1,column=1)
txt_tt_moto=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,textvariable=E_tt_moto , justify='left', state=DISABLED)
txt_tt_moto.grid(row=2,column=1)
txt_train=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6, textvariable=E_train ,justify='left', state=DISABLED)
txt_train.grid(row=3,column=1)
txt_kids_moto=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,textvariable=E_kids_moto , justify='left', state=DISABLED)
txt_kids_moto.grid(row=4,column=1)
txt_kids_ufo=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,textvariable=E_kids_ufo , justify='left', state=DISABLED)
txt_kids_ufo.grid(row=5,column=1)
txt_foot_ninja=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6, textvariable=E_foot_ninja ,justify='left', state=DISABLED)
txt_foot_ninja.grid(row=6,column=1)
txt_king_hammer=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6, textvariable=E_king_hammer ,justify='left', state=DISABLED)
txt_king_hammer.grid(row=7,column=1)
txt_flying_dragon=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6, textvariable=E_flying_dragon ,justify='left', state=DISABLED)
txt_flying_dragon.grid(row=8,column=1)
txt_royal_carriage=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6, textvariable=E_royal_carriage ,justify='left', state=DISABLED)
txt_royal_carriage.grid(row=9,column=1)

#=================================enter widget for column2========================================================
txt_hunting_hero=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,textvariable=E_hunting_hero , justify='left', state=DISABLED)
txt_hunting_hero.grid(row=0,column=1)
txt_ocean_cariusel=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,textvariable=E_ocean_cariusel , justify='left', state=DISABLED)
txt_ocean_cariusel.grid(row=1,column=1)
txt_furious_car=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,textvariable=E_furious_car , justify='left', state=DISABLED)
txt_furious_car.grid(row=2,column=1)
txt_air_hockey=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,textvariable=E_air_hockey , justify='left', state=DISABLED)
txt_air_hockey.grid(row=3,column=1)
txt_drifting_car=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6, textvariable=E_drifting_car ,justify='left', state=DISABLED)
txt_drifting_car.grid(row=4,column=1)
txt_kids_world=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6, textvariable=E_kids_world ,justify='left', state=DISABLED)
txt_kids_world.grid(row=5,column=1)
txt_robo_bot=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6, textvariable=E_robo_bot ,justify='left', state=DISABLED)
txt_robo_bot.grid(row=6,column=1)
txt_vr_games=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6, textvariable=E_vr_games ,justify='left', state=DISABLED)
txt_vr_games.grid(row=7,column=1)
txt_balance_cart=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,textvariable=E_balance_cart , justify='left', state=DISABLED)
txt_balance_cart.grid(row=8,column=1)
txt_relax_chair=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6, textvariable=E_relax_chair ,justify='left', state=DISABLED)
txt_relax_chair.grid(row=9,column=1)

#====================================Information==============================================
lblReceipt=Label(ft2,font=('arial',10,'bold'),text="Receipt",bd=2,anchor='w')
lblReceipt.grid(row=0,column=0,sticky=W)
txtReceipt=Text(ft2,width=65,height=28,bg='white',bd=8,font=('arial',10,'bold'))
txtReceipt.grid(row=1,column=0)

#====================================Button========================================
btnTotal= Button(fb2,padx=15,pady=1,bd=4,fg="black",font=('arial',12,"bold"),width=4,text="Total",command=Total_calculation).grid(row=0,column=0)
btnReceipt= Button(fb2,padx=15,pady=1,bd=4,fg="black",font=('arial',12,"bold"),width=4,text="Receipt",command=Receipt).grid(row=0,column=1)
btnReset= Button(fb2,padx=15,pady=1,bd=4,fg="black",font=('arial',12,"bold"),width=4,text="Reset",command=Reset).grid(row=0,column=2)
btnPrint= Button(fb2,padx=15,pady=1,bd=4,fg="black",font=('arial',12,"bold"),width=4,text="Print", command=iPrint).grid(row=0,column=3)
btnExit= Button(fb2,padx=15,pady=1,bd=4,fg="black",font=('arial',12,"bold"),width=4,text="Exit",command=qExit).grid(row=0,column=4)

#====================================Costing info========================================
lblTotalPrice= Label(f2aa,font=('arial',16,'bold'),text='Total Price',bd=8).grid(row=0,column=0,sticky=W)
txtlblTotalPrice= Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left',textvariable=TotalPrice).grid(row=0,column=1,sticky=W)

lblDiscount= Label(f2aa,font=('arial',16,'bold'),text='Discount (%)',bd=8).grid(row=1,column=0,sticky=W)
txtlblDiscount= Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left',textvariable=Discount).grid(row=1,column=1,sticky=W)

lblNetCurrentPice= Label(f2ab,font=('arial',16,'bold'),text='Net Current Price',bd=8).grid(row=0,column=0,sticky=W)
txtlblNetCurrentPice= Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left',textvariable=NetPrice).grid(row=0,column=1,sticky=W)


root.mainloop()