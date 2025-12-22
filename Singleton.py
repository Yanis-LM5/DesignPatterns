from typing import Self

#-------------------------------------------------Creational Patterns

class Database:
    __instance: Self = None

    def __init__(self):
        self.__url = ""

    def set_url(self, url: str) -> None:
         self.__url = url

    @staticmethod
    def getInstance() -> Self:
        if (Database.__instance == None):
            Database.__instance = Database()
        return Database.__instance


    @property
    def url(self) -> str:
        return self.__url


if __name__ == "__main__":
    db1: Database = Database.getInstance()
    db1.set_url("db1_url")

    db2: Database = Database.getInstance()
    db2.set_url("db2_url")

    db3: Database = Database()

    print(db1, db2, db3)
    print(db1.url, db2.url)




#    Autre version avec get/set via @property
#   @property
#     def url(self) -> str:
#         return self.__url

#     @url.setter
#     def url(self, url: str) -> None:
#          self.__url = url


# if __name__ == "__main__":
#     db1: Database = Database.getInstance()
#     db1.url = "db1_url"

#     db2: Database = Database.getInstance()
#     db2.url = "db2_url"

#     print(db1, db2)
#     print(db1.url, db2.url)