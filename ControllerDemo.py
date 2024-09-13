import time
import cv2
import mediapipe

class Controller:
    TITLE_BREAK = 'It is time to take a break!'
    MESSAGE_BREAK = "Take a 20 second break looking at something 20 feet away!"
    TITLE_TOO_CLOSE = 'You are too close!'
    MESSAGE_TOO_CLOSE = 'Please maintain a distance of 52 cm and adjust your viewing distance'
    TWENTY_MINUTES = 35

    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def run(self):
        start_time = time.time()
        start_time_too_close = 0

        while self.model.is_cap_opened():
            face = self.model.get_face(self.model.get_img())
            if face is not None:
                distance = self.model.update_distance()
                if distance is not None:
                    distance = int (distance)
                    self.view.show_distance(distance) # Check this part
                    cv2.waitKey(1)

                    current_time = time.time()
                    if current_time - start_time >= self.view.get_input_break_label_view():
                        self.model.send_notification(self.TITLE_BREAK, self.MESSAGE_BREAK)
                        start_time = time.time()
                    
                    if distance < self.view.get_input_distance_label_view():
                        self.view.make_window_red()
                        if (start_time_too_close == 0):
                            start_time_too_close = time.time()
                    else:
                        self.view.make_window_green()
                        start_time_too_close = time.time()

                    if (time.time() - start_time_too_close) > int (self.view.get_input_break_label_view()): # Check if 10 seconds have passed
                        distance = self.model.update_distance()
                        self.model.send_notification(self.TITLE_TOO_CLOSE, self.MESSAGE_TOO_CLOSE)
                        start_time_too_close = time.time() # Update the start time
            else:
                self.view.make_window_red()
                distance = None
                self.view.show_distance(None)