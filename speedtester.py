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
window = Tk ()
window.title ('a speed tester by g!')
window.geometry("500x300")
window.configure(background=marrom1)
window.resizable(width=FALSE, height=FALSE)
icon=PhotoImage(r"C:\Users\Administrator\Documents\pyt\speedtester\netbruh.ico")

img = Image.open(r"C:\Users\Administrator\Documents\pyt\speedtester\netbruh.ico")
img = img.resize((72,72))
img = ImageTk.PhotoImage(img)

#wifi logo
l_logo_img = Label(window, height=500, image=img, compound=LEFT, padx=10, anchor='nw', bg=marrom1, fg= marrom1)
l_logo_img.place(x=210, y=5)

#text under logo
l_logo_name = Label(window,text='a Net Tester!',font=('NTWagner 16'), padx=10, anchor='ne', bg=marrom1, fg=marromF)
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
    button_test['text'] = 'TEST'
    button_test.place(x=220, y=260)

    
#cfg example>
l_download = Label(window, text=('xx'), padx=10, anchor='ne',font=('NTWagner 20'), bg=marrom1, fg= marromF)
l_download.place(x=370, y=150)
l_mbps = Label(window, text=('Mbp/s Down.'), padx=10, anchor='ne',font=('NTWagner 14'), bg=marrom1, fg= marromF)
l_mbps.place(x=345, y=200)

#cfg example<
l_upload = Label(window, text=('xx'), padx=10, anchor='ne',font=('NTWagner 20'), bg=marrom1, fg= marromF)
l_upload.place(x=55, y=150)
l_mpbs = Label(window, text=('Mbp/s Uplo.'), padx=10, anchor='ne',font=('NTWagner 14'), bg=marrom1, fg= marromF)
l_mpbs.place(x=30, y=200)

#img up
imgup = Image.open(r"C:\Users\Administrator\Documents\pyt\speedtester\up.png")
imgup = imgup.resize((50,50))
imgup = ImageTk.PhotoImage(imgup)
#up logo
l_logo_imgup = Label(window, height=500, image=imgup, compound=LEFT, padx=10, anchor='ne', bg=marrom1, fg=marrom1)
l_logo_imgup.place(x=185, y=150)

#img down
imgdown = Image.open(r"C:\Users\Administrator\Documents\pyt\speedtester\down.png")
imgdown = imgdown.resize((50,50))
imgdown = ImageTk.PhotoImage(imgdown)
#down logo
l_logo_imgdown = Label(window, height=500, image=imgdown, compound=LEFT, padx=10, anchor='ne', bg=marrom1, fg=marrom1)
l_logo_imgdown.place(x=260, y=150)

#placing test button
button_test = Button(window, command=main, height=10, text=('START'), font=('NTWagner 10'), relief=RAISED, overrelief=RAISED, compound=CENTER, padx=0, anchor='nw', bg=marrom1, fg=marromF)
button_test.place(x=230, y=260)

window.mainloop()
