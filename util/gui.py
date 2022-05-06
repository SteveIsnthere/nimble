import tkinter as tk


class UI:
    def __init__(self, handler):
        self.handler = handler

        gui = tk.Tk()
        gui.config(padx=6, pady=6)
        gui.title("Nimble GUI")

        # spd
        spd_input_var = tk.StringVar()
        spd_input_var.set("0")
        spd_input = tk.Entry(gui, textvariable=spd_input_var)
        spd_input.grid(row=0, column=0, columnspan=1)

        def spd():
            speed = float(spd_input_var.get())
            print(speed)

        spd_button = tk.Button(gui, text="SPD", command=spd)
        spd_button.grid(row=1, column=0, columnspan=1)

        # alt
        alt_input_var = tk.StringVar()
        alt_input_var.set("0")
        alt_input = tk.Entry(gui, textvariable=alt_input_var)
        alt_input.grid(row=0, column=1, columnspan=1)

        def alt():
            altitude = float(alt_input_var.get())
            print(altitude)

        alt_button = tk.Button(gui, text="ALT", command=alt)
        alt_button.grid(row=1, column=1, columnspan=1)

        # nav
        def nav():
            print("nav")

        nav_button = tk.Button(gui, text="NAV", command=nav)
        nav_button.grid(row=0, column=2, columnspan=1)

        # app
        def app():
            print("nav")

        app_button = tk.Button(gui, text="APP", command=app)
        app_button.grid(row=1, column=2, columnspan=1)

        # hdg
        hdg_input_var = tk.StringVar()
        hdg_input_var.set("0")
        hdg_input = tk.Entry(gui, textvariable=hdg_input_var)
        hdg_input.grid(row=0, column=3, columnspan=1)

        def hdg():
            altitude = float(alt_input_var.get())
            print(altitude)

        hdg_button = tk.Button(gui, text="HDG", command=hdg)
        hdg_button.grid(row=1, column=3, columnspan=1)

        # vs
        vs_input_var = tk.StringVar()
        vs_input_var.set("0")
        vs_input = tk.Entry(gui, textvariable=vs_input_var)
        vs_input.grid(row=0, column=4, columnspan=1)

        def vs():
            altitude = float(alt_input_var.get())
            print(altitude)

        vs_button = tk.Button(gui, text="VS", command=vs)
        vs_button.grid(row=1, column=4, columnspan=1)

        # toga
        def toga():
            print("toga")

        toga_button = tk.Button(gui, text="TOGA", command=toga)
        toga_button.grid(row=2, column=0, columnspan=2, rowspan=2)

        # toggle
        def config_toggle_btn():
            controller_on = handler.controller_state()
            if controller_on:
                toggle_button.config(foreground="green", text="ON")
            else:
                toggle_button.config(foreground="red", text="OFF")

        def toggle():
            controller_on = handler.controller_state()
            if controller_on:
                handler.switch_off_controller()
            else:
                handler.switch_on_controller()
            config_toggle_btn()

        toggle_button = tk.Button(gui, text="toggle", command=toggle)
        config_toggle_btn()
        toggle_button.grid(row=2, column=2, columnspan=1)

        # man
        def man():
            print("toggle")

        man_button = tk.Button(gui, text="MAN", command=man)
        man_button.grid(row=2, column=3, columnspan=2, rowspan=2)

        for entry in (spd_input, alt_input, hdg_input, vs_input):
            entry.config(justify=tk.CENTER, width=7)

        gui.mainloop()
