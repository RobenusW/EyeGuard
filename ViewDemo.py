import customtkinter
from Settings import Settings
 
class View:
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    count_thread = 0
    previous_label = None

    def __init__(self, root, settings):
        self.window = root
        self.window.title("Distance Viewer")
        self.window.attributes('-fullscreen', True)
        self.settings = settings  # Store the settings object
        self.settings_button = customtkinter.CTkButton(self.window, text="Settings", command=self.open_settings)
        self.settings_button.pack()

    def open_settings(self):
        self.settings.open_settings_window()

    def create_camera_access_label(self):
        label = customtkinter.CTkLabel(master=self.window, text="Enable Camera Access!")
    
    def show_distance(self,distance):
        if distance is not None:
            label = customtkinter.CTkLabel(master=self.window, text="Distance: " + str(distance) + " cm", font=("Helevetica", 100), bg_color=self.make_label_color(distance))
            label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
            self.window.update()
            if self.previous_label is not None:
                self.previous_label.destroy()
            self.previous_label = label
        else:
            label = customtkinter.CTkLabel(master=self.window, text="No face detected", font=("Helevetica", 100), bg_color="red")
            label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
            self.window.update()
            if self.previous_label is not None:
                self.previous_label.destroy()
            self.previous_label = label


    def make_window_green(self):
        self.window.config(bg="green")
        self.window.update()

    def make_window_red(self):
        self.window.config(bg="red")
        self.window.update()

    def get_input_break_label_view(self):
        return self.settings.get_input_break_label()
    
    def get_input_distance_label_view(self):
        return self.settings.get_input_distance_label()
    
    def make_label_color(self, distance):
        if distance < int (self.settings.get_input_distance_label()):
            return "red"
        else:
            return "green"