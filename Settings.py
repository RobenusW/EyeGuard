import customtkinter
class Settings:
    MINUTE_TO_SECOND = 60
    RECOMMENDED_BREAK_INTERVAL = 20*60
    RECOMMENDED_DISTANCE = 52

    def __init__(self, root):
        self.root = root
        self.input_text_break_label = ""
        self.input_text_distance_label = ""
        self.settings_window = None

    def open_settings_window(self):
        if self.settings_window is not None and customtkinter.CTk.winfo_exists(self.settings_window):  # Check if the window already exists
            self.settings_window.focus()  # Bring the existing window to the front
            return
        
        self.settings_window = customtkinter.CTkToplevel(self.root)
        self.settings_window.title("Settings")

        # Add widgets to the new window
        self.break_label = customtkinter.CTkLabel(self.settings_window, text="Break Intervals:")
        self.break_label.pack()

        self.break_label_entry = customtkinter.CTkEntry(self.settings_window, placeholder_text="Minutes, Recommended 20 Minutes")
        self.break_label_entry.pack()

        self.distance_label = customtkinter.CTkLabel(self.settings_window, text="Distance to Screen:")
        self.distance_label.pack()

        self.distance_label_entry = customtkinter.CTkEntry(self.settings_window, placeholder_text="Centimeters, Recommended 52cm - 70cm")
        self.distance_label_entry.pack()

        self.save_button = customtkinter.CTkButton(self.settings_window, text="Save", command=self.save_input)
        self.save_button.pack(pady=10)

    def save_input(self):
        try:
            if self.break_label_entry.get() == "":
                self.input_text_break_label = self.RECOMMENDED_BREAK_INTERVAL
            else:
                self.input_text_break_label = int(self.break_label_entry.get()) * self.MINUTE_TO_SECOND
                if self.input_text_break_label < 0:
                    raise ValueError

            if self.distance_label_entry.get() == "":
                self.input_text_distance_label = self.RECOMMENDED_DISTANCE
            else:
                self.input_text_distance_label = int(self.distance_label_entry.get())
                if self.input_text_distance_label < 0:
                    raise ValueError
                    
        except ValueError:
            if hasattr(self, 'error_message'):
                self.error_message.destroy()
            self.error_message = customtkinter.CTkLabel(self.settings_window, text="Enter Valid Integer", text_color="red")
            self.error_message.pack()
        else:
            if hasattr(self, 'error_message'):
                self.error_message.destroy()
            self.settings_window.destroy()
            return self.input_text_break_label, self.input_text_distance_label

    def get_input_break_label(self):
        if self.input_text_break_label == "":
            return self.RECOMMENDED_BREAK_INTERVAL
        return self.input_text_break_label

    def get_input_distance_label(self):
        if self.input_text_distance_label == "":
            return self.RECOMMENDED_DISTANCE
        return self.input_text_distance_label