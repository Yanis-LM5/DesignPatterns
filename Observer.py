from abc import ABC, abstractmethod

class EventListeners(ABC):

    @abstractmethod
    def update(self, filename: str) -> str :
        pass

class EmailAlertsListener(EventListeners):

    def __init__(self, email: str, message: str) -> None:
       self.__email: str = email
       self.__message: str = message


    def update(self, filename: str) -> str:
        return self.__message + " " + filename


class LoggingListener(EventListeners):

    def __init__(self, log: str, message: str):
        self.__log = log
        self.__message = message

    def update(self, filename: str) -> str:
        return self.__log + " " + filename


class EventManager:
    __listeners=[]
    def __init__(self):
        pass

    def subscribe(self, listener: str) -> None:
        self.__listeners.append(listener)

    def unsubscribe(self, listener: str) -> None:
        self.__listeners.remove(listener)

    def notify(self, data: str) -> None:
        for i in range (len(self.__listeners)):
            print(self.__listeners[i] +": "+ data)


class Editor:
    def __init__(self):
        self.events = EventManager()

    def openFile(self, path: str) -> None:
        self.events.notifiy("file {path} open")

    def saveFile(self, path: str) -> None:
        self.events.notifiy("file {path} saved")



if __name__ == "__main__":
    editor = Editor()
    logger = LoggingListener("mail", "azer@ert.com")

    editor.events.subscribe("yan")
    editor.events.subscribe("aze")
    editor.events.subscribe("ert")
    editor.events.subscribe("rty")
    editor.events.notify("new product available")
    editor.events.unsubscribe("rty")
    editor.events.notify("new product available")

# error: 'DesignPatterns/' does not have a commit checked out
# fatal: adding files failed
