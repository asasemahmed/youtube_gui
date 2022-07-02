# the youtube downloader app
# created by asem aballah



import time
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from youtube_func import download_vedio as dw
import webbrowser as web
from pytube import YouTube




# the screen home page

bg = "#CBF3F0"
root = tk.Tk()
root.title("ASEM (youtube downloder)")
root.geometry('800x700')
root.configure(bg=bg)
root.resizable(width=False, height=False)


website_image = tk.PhotoImage(file="ww.png")

label_name = tk.Label(root, text="ASEM ABDALLAH", font=("ravie", 30), fg="#FF9F1C", bg=bg)
label_name.pack()
label_name.place(x=200, y=200)

label_title = tk.Label(root, text="Youtube App", font=("magneto", 25), fg="#2EC4B6", bg=bg)
label_title.pack()
label_title.place(x=120, y=150)


def goto_app():
    frame = tk.Frame(root, bg="#d00000")
    frame.pack(side="top", expand=True, fill="both")
    run_app()

open_web = lambda : web.open("https://sites.google.com/view/asem-ahmed/home")
open_youtube = lambda : web.open("https://www.youtube.com/")

app_button = tk.Button(root, text="GO TO APP", bg="#2EC4B6", fg="#CBF3F0", command=goto_app, width=10, height=2,
        font=("stencil", 15))
app_button.pack()
app_button.place(x=330, y=300)

website_button = tk.Button(root, image=website_image,  bg="white", command=open_web)
website_button.pack()
website_button.place(x=380, y=155)




img_youtube_logo = tk.PhotoImage(file="youtube_logo.png")
img_download_icon = tk.PhotoImage(file="download_icon.png")
img_path_icon = tk.PhotoImage(file="path_icon.png")
you_tubec_icon = tk.PhotoImage(file="youtube_icon.png")


# function for run you tube app
def run_app():

    label_logo_youtube = tk.Label(root, image=img_youtube_logo, width=88, height=40)
    label_logo_youtube.pack()
    label_logo_youtube.place(x=370, y=0)

    label_url = tk.Label(root, text="URL", font=("Elephant", 20), bg='#d00000', fg="white")
    label_url.pack()
    label_url.place(x=120, y=110)

    url = tk.StringVar()
    url.set("")


    entry_url = tk.Entry(root, width=30, textvariable=url, font=(30))
    entry_url.pack()
    entry_url.place(x=310, y=115)

    label_quality = tk.Label(root, text="QUALITY", font=('Elephant', 20), bg="#d00000", fg="white")
    label_quality.pack()
    label_quality.place(x=120, y=307)

    qu = tk.IntVar()
    radio_button1 = tk.Radiobutton(root, text="360", value=360, variable=qu, font=(7), bg="#d00000")
    radio_button1.pack()
    radio_button1.place(x=310, y=307)
    radio_button2 = tk.Radiobutton(root, text="480", value=480, variable=qu, font=(7), bg="#d00000")
    radio_button2.pack()
    radio_button2.place(x=380, y=307)
    radio_button3 = tk.Radiobutton(root, text="720", value=720, variable=qu, font=(7), bg="#d00000")
    radio_button3.pack()
    radio_button3.place(x=450, y=307)
    radio_button4 = tk.Radiobutton(root, text="Highe Q", value=2, variable=qu, font=(7), bg="#d00000")
    radio_button4.pack()
    radio_button4.place(x=520, y=307)
    radio_button5 = tk.Radiobutton(root, text="Low Q", value=1, variable=qu, font=(7), bg="#d00000")
    radio_button5.pack()
    radio_button5.place(x=630, y=307)

    label_file = tk.Label(root, text="File", font=('Elephant', 20), bg="#d00000", fg="white")
    label_file.pack()
    label_file.place(x=125, y=200)

    
    def ask_file() -> str:
        file_location = ""
        path_file.set("")
        file_location = filedialog.askdirectory()
        path_file_entry.insert(0, file_location)
        return file_location

    path_file = tk.StringVar()
    path_file_entry = tk.Entry(root, width=30, font=(2), textvariable=path_file)
    path_file_entry.pack()
    path_file_entry.place(x=310, y=210)

    button_file_img = tk.Button(root, image=img_path_icon, font=(20), command=ask_file, bg="#d00000")
    button_file_img.pack()
    button_file_img.place(x=276, y=207)


    def download_vedio():
        if url.get() == "":
            messagebox.showerror("EROR URL", "URL is wrong please Enter \n valide URL")
        else:
            dw(url=url.get(), file=path_file.get(), resolution=qu.get())

    downlaad_icon_button = tk.Button(root, image=img_download_icon, font=(20), command=download_vedio, bg="#d00000")
    downlaad_icon_button.pack()
    downlaad_icon_button.place(x=390, y=400)

    youtube_button = tk.Button(root, image=you_tubec_icon, command=open_youtube)
    youtube_button.pack()
    youtube_button.place(x=275, y=110)

tk.mainloop()
