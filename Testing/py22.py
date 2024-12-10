import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window,text= 'awokwk')
label2 = tkinter.Label(main_window,text= 'ahihihi')

btn = tkinter.Button(main_window,text='Click')

# method positioning
label1.pack()
label2.pack()
btn.pack()

# method menampilkan GUI
main_window.mainloop()