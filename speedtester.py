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
wdw.title ('')
wdw.geometry("500x500")
wdw.configure(background=c1)
wdw.resizable(width=FALSE, height=FALSE)

#stripe at mid-screen
frame_logo = Frame(wdw, width=500, height=250, bg=c1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_stripe = Frame(wdw, width=250, height=5, bg=cS)
frame_stripe.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)
frame_stripe = Frame(wdw, width=250, height=5, bg=cL)
frame_stripe.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

#img
img = Image.open('net.png')
img = img.resize((72,72))
img = ImageTk.PhotoImage(img)

#wifi logo
l_logo_img = Label(frame_logo, height=500, image=img, compound=LEFT, padx=10, anchor='nw', bg=c1, fg= c1)
l_logo_img.place(x=25, y=0)

#text under logo
l_logo_name = Label(frame_logo,text='a Net Tester!',font=('BebasNeue'), padx=10, anchor='ne', bg=c1, fg= cB)
l_logo_name.place(x=17.5, y=70)

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
    button_test['text'] = 'Test again'
    button_test.place(x=215, y=215)

    

#cfg example>
l_download = Label(frame_logo, text=('50'), padx=10, anchor='ne',font=('Arial 28'), bg=c1, fg= cB)
l_download.place(x=330, y=150)
l_mbps = Label(frame_logo, text=('Mbps/s Down.'), padx=10, anchor='ne',font=('BebasNeue'), bg=c1, fg= cB)
l_mbps.place(x=330, y=200)

#cfg example<
l_upload = Label(frame_logo, text=50, padx=10, anchor='ne',font=('Arial 28'), bg=c1, fg= cB)
l_upload.place(x=75, y=150)
l_mpbs = Label(frame_logo, text=('Mbps/s Uplo.'), padx=10, anchor='ne',font=('BebasNeue'), bg=c1, fg= cB)
l_mpbs.place(x=75, y=200)

#img up
imgup = Image.open('up.png')
imgup = imgup.resize((50,50))
imgup = ImageTk.PhotoImage(imgup)
#up logo
l_logo_imgup = Label(frame_logo, height=500, image=imgup, compound=LEFT, padx=10, anchor='ne', bg=c1, fg=c1)
l_logo_imgup.place(x=185, y=150)

#img down
imgdown = Image.open('down.png')
imgdown = imgdown.resize((50,50))
imgdown = ImageTk.PhotoImage(imgdown)
#down logo
l_logo_imgdown = Label(frame_logo, height=500, image=imgdown, compound=LEFT, padx=10, anchor='ne', bg=c1, fg=c1)
l_logo_imgdown.place(x=260, y=150)

#placing test button
button_test = Button(frame_logo,command=main, height=25, text=('Start Test'), font=('BebasNeue'), relief=RAISED, overrelief=RIDGE, compound=LEFT, padx=1, anchor='nw', bg=cS, fg=cL)
button_test.place(x=215, y=215)


wdw.mainloop()