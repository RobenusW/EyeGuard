from ModelDemo import Model
from ViewDemo import View
from Settings import Settings
from ControllerDemo import Controller
import customtkinter

if __name__ == "__main__":
        root = customtkinter.CTk()  # Create the main window
        model = Model() # Pass the main window and Settings to View
        settings = Settings(root)  # Pass the main window to Settings
        view = View(root, settings)
        controller = Controller(model, view)  # Pass Settings to Controller if needed
        controller.run()
