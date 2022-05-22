import tkinter as tk

from others.handler import Handler


class GUI(Handler):
    def __init__(self, handler):
        super().__init__(handler)
        self.man_button = None
        self.toggle_button = None
        self.toga_button = None
        self.vs_button = None
        self.vs_input = None
        self.vs_input_var = None
        self.hdg_button = None
        self.hdg_input = None
        self.hdg_input_var = None
        self.app_button = None
        self.nav_button = None
        self.alt_button = None
        self.alt_input = None
        self.alt_input_var = None
        self.spd_input_var = None
        self.gui = None
        self.spd_button = None
        self.spd_input = None

        self.button_on_color = "green"
        self.button_off_color = "red"

    def start(self):
        self.gui = tk.Tk()
        # gui.overrideredirect(True)
        self.gui.config(padx=6, pady=6)
        self.gui.title("Nimble GUI")

        # spd
        self.spd_input_var = tk.StringVar()
        self.spd_input_var.set("0")
        self.spd_input = tk.Entry(self.gui, textvariable=self.spd_input_var)
        self.spd_input.grid(row=0, column=0, columnspan=1)

        def spd():
            self.toggle_mode("SPD")

        self.spd_button = tk.Button(self.gui, text="SPD", command=spd)
        self.spd_button.grid(row=1, column=0, columnspan=1)

        # alt
        self.alt_input_var = tk.StringVar()
        self.alt_input_var.set("0")
        self.alt_input = tk.Entry(self.gui, textvariable=self.alt_input_var)
        self.alt_input.grid(row=0, column=1, columnspan=1)

        def alt():
            self.toggle_mode("ALT")

        self.alt_button = tk.Button(self.gui, text="ALT", command=alt)
        self.alt_button.grid(row=1, column=1, columnspan=1)

        # nav
        def nav():
            self.toggle_mode("NAV")

        self.nav_button = tk.Button(self.gui, text="NAV", command=nav)
        self.nav_button.grid(row=0, column=2, columnspan=1)

        # app
        def app():
            self.toggle_mode("APP")

        self.app_button = tk.Button(self.gui, text="APP", command=app)
        self.app_button.grid(row=1, column=2, columnspan=1)

        # hdg
        self.hdg_input_var = tk.StringVar()
        self.hdg_input_var.set("0")
        self.hdg_input = tk.Entry(self.gui, textvariable=self.hdg_input_var)
        self.hdg_input.grid(row=0, column=3, columnspan=1)

        def hdg():
            self.toggle_mode("HDG")

        self.hdg_button = tk.Button(self.gui, text="HDG", command=hdg)
        self.hdg_button.grid(row=1, column=3, columnspan=1)

        # vs
        self.vs_input_var = tk.StringVar()
        self.vs_input_var.set("0")
        self.vs_input = tk.Entry(self.gui, textvariable=self.vs_input_var)
        self.vs_input.grid(row=0, column=4, columnspan=1)

        def vs():
            self.toggle_mode("VS")

        self.vs_button = tk.Button(self.gui, text="VS", command=vs)
        self.vs_button.grid(row=1, column=4, columnspan=1)

        # toga
        def toga():
            self.toggle_mode("TOGA")

        self.toga_button = tk.Button(self.gui, text="TOGA", command=toga)
        self.toga_button.grid(row=2, column=0, columnspan=2, rowspan=2)

        # toggle
        def config_toggle_btn():
            controller_on = self.is_controller_on()
            if controller_on:
                self.toggle_button.config(foreground="green", text="ON")
            else:
                self.toggle_button.config(foreground="red", text="OFF")

        def toggle():
            controller_on = self.is_controller_on()
            if controller_on:
                self.switch_off_controller()
            else:
                self.switch_on_controller()

        self.toggle_button = tk.Button(self.gui, text="toggle", command=toggle)
        config_toggle_btn()
        self.toggle_button.grid(row=2, column=2, columnspan=1)

        # man
        def man():
            self.toggle_mode("MAN")

        self.man_button = tk.Button(self.gui, text="MAN", command=man)
        self.man_button.grid(row=2, column=3, columnspan=2, rowspan=2)

        for entry in (self.spd_input, self.alt_input, self.hdg_input, self.vs_input):
            entry.config(justify=tk.CENTER, width=7)

        self.gui.bind('<Return>', self.return_event)

        self.gui.mainloop()

    def receive_state_update(self, name, state):
        if name == "ALT":
            if state:
                self.alt_button.config(foreground=self.button_on_color)
            else:
                self.alt_button.config(foreground=self.button_off_color)
        elif name == "VS":
            if state:
                self.vs_button.config(foreground=self.button_on_color)
            else:
                self.vs_button.config(foreground=self.button_off_color)
        elif name == "HDG":
            if state:
                self.hdg_button.config(foreground=self.button_on_color)
            else:
                self.hdg_button.config(foreground=self.button_off_color)
        elif name == "SPD":
            if state:
                self.spd_button.config(foreground=self.button_on_color)
            else:
                self.spd_button.config(foreground=self.button_off_color)
        elif name == "MAN":
            if state:
                self.man_button.config(foreground=self.button_on_color)
            else:
                self.man_button.config(foreground=self.button_off_color)
        elif name == "NAV":
            if state:
                self.nav_button.config(foreground=self.button_on_color)
            else:
                self.nav_button.config(foreground=self.button_off_color)
        elif name == "APP":
            if state:
                self.app_button.config(foreground=self.button_on_color)
            else:
                self.app_button.config(foreground=self.button_off_color)
        elif name == "TOGA":
            if state:
                self.toga_button.config(foreground=self.button_on_color)
            else:
                self.toga_button.config(foreground=self.button_off_color)
        elif name == "running":
            if state:
                self.toggle_button.config(foreground=self.button_on_color, text="ON")
            else:
                self.toggle_button.config(foreground=self.button_off_color, text="OFF")

    def return_event(self, e):
        self.set_mode("VS", float(self.vs_input.get()))
        self.set_mode("ALT", float((self.alt_input.get())))
        self.set_mode("SPD", float((self.spd_input.get())))
        self.set_mode("HDG", float((self.hdg_input.get())))
