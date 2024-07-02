
from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):
    """
    Абстрактный класс Издателя , класс для каналов 
    """
    @abstractmethod
    def attach(self, observer: 'Observer') -> None:
        """
        Добавить наблюдателя к списку наблюдателей.
        """
        pass

    @abstractmethod
    def detach(self, observer: 'Observer') -> None:
        """
        Удалить наблюдателя  из списка наблюдателей.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Уведомить всех наблюдателей о новом видео.
        """
        pass

class YouTubeChannel(Subject):
    """
    Класс канала на YouTube.
    """
    def __init__(self, name: str):
        self._name = name
        self._observers: List['Observer'] = []

    def attach(self, observer: 'Observer') -> None:
        self._observers.append(observer)

    def detach(self, observer: 'Observer') -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print(f"Новый ролик на канале {self._name}!")
        for observer in self._observers:
            observer.update(self)

    def new_video(self) -> None:
        """
    новое видео.
        """
        print(f"Канал {self._name} выпустил новое видео.")
        self.notify()

class Observer(ABC):
    """
   класс Наблюдателя (Observer)
    """
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Метод для уведомления Наблюдателя.
        """
        pass

class User(Observer):
    # наблюдатель

    def __init__(self, name: str):
        self._name = name

    def update(self, subject: Subject) -> None:
        print(f"{self._name} получил уведомление от канала {subject._name} о новом видео.")


if __name__ == "__main__":
    channel1 = YouTubeChannel("Python Tutorials")
    channel2 = YouTubeChannel("Gaming Channel")

    user1 = User("John")
    user2 = User("Alice")


    channel1.attach(user1)
    channel1.attach(user2)
    channel2.attach(user1)


    channel1.new_video()
    channel2.new_video()

    channel1.detach(user2)

    channel1.new_video()

