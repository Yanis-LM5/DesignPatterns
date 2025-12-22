from abc import ABC, abstractmethod
import os
import platform

#-------------------------------------------------Creational Patterns


class Button(ABC):

    @abstractmethod
    def render(self) -> None:
       pass

    @abstractmethod
    def onClick(self) -> None:
        pass

class WindowsButton(Button):
    def render(self) -> None:
        print("WindowsButtonRender")

    def onClick(self) -> None:
        print("WindowsButtonOnClick")


class HtmlButton(Button):

    def render(self) -> None:
        print("HtmlButtonRender")

    def onClick(self) -> None:
        print("HtmlButtonOnClick")


class Dialog(ABC):

    @abstractmethod
    def createButton(self) -> Button:
        pass

    def render(self) -> None:
        okButton = self.createButton()
        okButton.onClick()
        okButton.render()


class WindowsDialog(Dialog):

    def createButton(self) -> WindowsButton:
        return WindowsButton()


class WebDialog(Dialog):

    def createButton(self) -> HtmlButton:
        return HtmlButton()


class App:

    def __init__(self, config_os: str) -> None:
        self.dialog: Dialog | None = None
        self.config_os = config_os

    def initialize(self) -> None:
        if self.config_os == "Windows":
            self.dialog = WindowsDialog()
        else:
            self.dialog = WebDialog()

    def main(self) -> None:
        self.initialize()
        self.dialog.render()


if __name__ == "__main__":
    app1 = App("Web")
    app2 = App("Windows")

    app1.main()
    app2.main()
    # print(os.name)
    # print(platform.system())