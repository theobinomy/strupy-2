
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class StrupyUi2(toga.App):
    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        # Create a main content box
        main_box = toga.Box()

        # Add the content on the main window
        self.main_window.content = main_box

        # Show the main window
        self.main_window.show()


def main():
    return StrupyUi2('strupy-ui2', 'asdf.stupy-ui2')
