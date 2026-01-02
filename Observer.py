"""
L'objectif du pattern observer est d'arriver à "découpler" les interactions
entre des elements/composants logiciels. "Découpler" veut dire rendre les
interactions plus flexibles et moins fortes entre des élements logiciels,
de sorte d'améliorer la maintenabilité et l'évolutivité de ces élements.
Le pattern observer definit un "observable" qui va notifier des
"observers"/"listeners", de l'arrivée d'un évènement particulier.
Les observers concrêts réalisent une même interface
(via polymorphisme) déclarée dans une classe abstraite.
L'observable est responsable de permettre aux observers de s'abonner à ses
notifications. L'observable n'est pas au courant de ce que font les observers
suite aux notifications.

docstring
"""

from abc import ABC, abstractmethod
from enum import StrEnum


class EventListeners(ABC):
    @abstractmethod
    def update(self, filename: str) -> None:
        pass


class EmailAlertsListener(EventListeners):
    def __init__(self, email: str, message: str) -> None:
        self.__email: str = email
        self.__message: str = message

    def update(self, filename: str) -> None:
        action: str = (
            f"Sending email to dest: {self.__email}, "
            f"object: {self.__message}, name: {filename}"
        )
        print(action)


class LoggingListener(EventListeners):
    def __init__(self, log: str, message: str) -> None:
        self.__log = log
        self.__message = message

    def update(self, filename: str) -> None:
        action: str = (
            f"Writing log to dest: {self.__log}, "
            f"object: {self.__message}, name: {filename}"
        )
        print(action)


class EventType(StrEnum):
    OPEN = "OPEN"
    SAVE = "SAVE"


class EventManager:
    def __init__(self) -> None:
        self.__listeners: dict[EventType, list[EventListeners]] = {
            EventType.OPEN: [],
            EventType.SAVE: [],
        }

    def subscribe(self, event_type: EventType, listener: str) -> None:
        self.__listeners[event_type].append(listener)

    def unsubscribe(self, event_type: EventType, listener: str) -> None:
        self.__listeners[event_type].remove(listener)

    def notify(self, event_type: EventType, filename_data: str) -> None:
        for listeners in self.__listeners[event_type]:
            listeners.update(filename_data)


class Editor:
    def __init__(self) -> None:
        self.events = EventManager()

    def openFile(self, filename: str) -> None:
        self.events.notify(EventType.OPEN, filename)

    def saveFile(self, filename: str) -> None:
        self.events.notify(EventType.SAVE, filename)


if __name__ == "__main__":
    editor = Editor()
    logger_listener = LoggingListener("logger", "new file opened")
    email_listener = EmailAlertsListener("exemple@domain.com", "new file saved")

    editor.events.subscribe(EventType.OPEN, logger_listener)
    editor.events.subscribe(EventType.SAVE, email_listener)

    filename = "my_code.py"
    editor.openFile(filename)
    editor.saveFile(filename)
