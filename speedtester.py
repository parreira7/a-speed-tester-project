from tkinter import *
from PIL import Image, ImageTk

#colors
c1 = ('#353535')
c2 = ('#711919')
cL = ('#000000')
cS = ('#2196f3')
cB = ('#ffffff')
marrom1 = ('#873e23')
marromF = ('#e28743')
barra = ('#1e81b0')

#start tkinter and cfg size
wdw = Tk ()
wdw.title ('a speed tester by g!')
wdw.geometry("500x300")
wdw.configure(background=marrom1)
wdw.resizable(width=FALSE, height=FALSE)
icon=PhotoImage('ico.ico')
wdw.iconbitmap(True,icon)

#imagens
img = Image.open('ico.ico')
img = img.resize((72,72))
img = ImageTk.PhotoImage(img)
l_logo_img = Label(wdw, height=500, image=img, compound=LEFT, padx=10, anchor='nw', bg=marrom1, fg= marrom1)
l_logo_img.place(x=210, y=5)
l_logo_name = Label(wdw,text='a Net Tester!',font=('NTWagner 16'), padx=10, anchor='ne', bg=marrom1, fg=marromF)
l_logo_name.place(x=180, y=85)

#function
import speedtest
speed = speedtest.Speedtest()
def main():
    l_download ['text'] = 'Processing'   
    download = f"{'{:.2f}'.format(speed.download()/1024/1024)}"
    l_download ['text'] = download

    l_upload ['text'] = 'Processing'
    upload = f"{'{:.2f}'.format(speed.upload()/1024/1024)}"
    l_upload ['text'] = upload
#test button
    button_test.place(x=230, y=215)

#cfg example>
l_download = Label(wdw, text=('xx'), padx=10, anchor='ne',font=('NTWagner 20'), bg=marrom1, fg= marromF)
l_download.place(x=375, y=150)
l_mbps = Label(wdw, text=('Mbp/s Down.'), padx=10, anchor='ne',font=('NTWagner 14'), bg=marrom1, fg= marromF)
l_mbps.place(x=335, y=200)

#cfg example<
l_upload = Label(wdw, text=('xx'), padx=10, anchor='ne',font=('NTWagner 20'), bg=marrom1, fg= marromF)
l_upload.place(x=75, y=150)
l_mpbs = Label(wdw, text=('Mbp/s Uplo.'), padx=10, anchor='ne',font=('NTWagner 14'), bg=marrom1, fg= marromF)
l_mpbs.place(x=40, y=200)

#img up
imgup = Image.open('up.png')
imgup = imgup.resize((50,50))
imgup = ImageTk.PhotoImage(imgup)
start = Image.open('click.png')
start = start.resize((35,35))
start = ImageTk.PhotoImage(start)
#up logo
l_logo_imgup = Label(wdw, height=500, image=imgup, compound=LEFT, padx=10, anchor='ne', bg=marrom1, fg=marrom1)
l_logo_imgup.place(x=185, y=150)
#img down
imgdown = Image.open('down.png')
imgdown = imgdown.resize((50,50))
imgdown = ImageTk.PhotoImage(imgdown)
#down logo
l_logo_imgdown = Label(wdw, height=500, image=imgdown, compound=LEFT, padx=10, anchor='ne', bg=marrom1, fg=marrom1)
l_logo_imgdown.place(x=260, y=150)
#placing test button
button_test = Button(wdw, image=start, command=main, bg=marrom1, fg=marrom1, relief=FLAT, overrelief=FLAT)
button_test.place(x=230, y=215)

wdw.mainloop()
