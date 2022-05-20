from tkinter import * 
from PIL import ImageTk, Image

def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            import pong_pong
            pong_pong.main()
        elif args == 2:
            import pong_game
            pong_game.main()
        """elif args == 3:
            from Options import Petunjuk
            Petunjuk.main()"""
       

    def option():
        lab_img1 = Button(
            main_window,
            text="Select",
            bg='#e6fff5',
            border=0,
            justify='center',
            font=("Arial", 12)
        )

        sel_btn1 = Button(
            text="Arena 1",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#cef3da",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Arena 2",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#dacef3",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Petunjuk Permainan",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#f3dace",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
       

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()
    background_image = ImageTk.PhotoImage(Image.open("backgorund-awal.png"))
    img1 = ImageTk.PhotoImage(Image.open("fancy-court.png"))
    main_window.geometry("700x500")
    main_window.resizable(0, 0)
    main_window.title("B'Pong")
    #main_window.configure(background=img1)
    
    """frame = Frame(main_window, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)"""
    
    

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(0, 0))

    lab_img = Label(
        main_window,
        image = background_image,
        text="B'Pong",
        bg='#e6fff5',
        font=("Courier", 28)
    )
    lab_img.pack(pady=(0, 0))

    main_window.mainloop()


start_main_page()