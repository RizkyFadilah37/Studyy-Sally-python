# Create Abstract class in python
# abc = Abstract Base Class
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class PushButton(Button):
    def click(self):
        print("Push Button Clicked")

class RadioButton(Button):
    def click(self):
        print("Radio Button Clicked")

# button = Button() # TypeError: Can't instantiate abstract class Button with abstract methods click
push_button = PushButton()
radio_button = RadioButton()
push_button.click()
radio_button.click()