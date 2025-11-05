# Module 7: Python Design Patterns

## Overview
This module surveys the 23 classic "Gang of Four" design patterns and demonstrates how to apply each in Python. Learners will explore practical implementations that highlight Python's idiomatic features while reinforcing object-oriented principles.

## Week 1: Creational Patterns
Focus: Object creation mechanisms that increase flexibility and reuse.

### Abstract Factory
Creates families of related objects without specifying concrete classes.
```python
class Button:
    def render(self):
        raise NotImplementedError

class WinButton(Button):
    def render(self):
        return "Windows button"

class MacButton(Button):
    def render(self):
        return "macOS button"

class GUIFactory:
    def create_button(self) -> Button:
        raise NotImplementedError

class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

factory: GUIFactory = MacFactory()
print(factory.create_button().render())  # macOS button
```

### Builder
Separates construction of a complex object from its representation.
```python
class House:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.add("walls")
        return self

    def build_roof(self):
        self.house.add("roof")
        return self

    def build_garden(self):
        self.house.add("garden")
        return self

    def result(self):
        return self.house

villa = HouseBuilder().build_walls().build_roof().build_garden().result()
print(villa.parts)  # ['walls', 'roof', 'garden']
```

### Factory Method
Defines an interface for creating an object but lets subclasses decide which class to instantiate.
```python
class Transport:
    def deliver(self):
        raise NotImplementedError

class Truck(Transport):
    def deliver(self):
        return "Deliver by land"

class Ship(Transport):
    def deliver(self):
        return "Deliver by sea"

class Logistics:
    def create_transport(self) -> Transport:
        raise NotImplementedError

class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()

manager = RoadLogistics()
print(manager.create_transport().deliver())  # Deliver by land
```

### Prototype
Copies existing objects without making code dependent on their classes.
```python
import copy

class Document:
    def __init__(self, title, sections):
        self.title = title
        self.sections = sections

    def clone(self):
        return copy.deepcopy(self)

original = Document("Report", ["Intro", "Results"])
copy_doc = original.clone()
copy_doc.sections.append("Conclusion")
print(original.sections)  # ['Intro', 'Results']
```

### Singleton
Ensures a class has only one instance and provides a global access point.
```python
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Settings(metaclass=Singleton):
    pass

print(Settings() is Settings())  # True
```

## Week 2: Structural Patterns
Focus: Composition of classes and objects to form larger structures.

### Adapter
Allows objects with incompatible interfaces to work together.
```python
class EuropeanPlug:
    def voltage(self):
        return 230

class USAdapter:
    def __init__(self, plug: EuropeanPlug):
        self.plug = plug

    def voltage(self):
        return 110

device = USAdapter(EuropeanPlug())
print(device.voltage())  # 110
```

### Bridge
Separates an abstraction from its implementation so both can vary independently.
```python
class Renderer:
    def render_circle(self, radius):
        raise NotImplementedError

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        return f"Vector circle radius {radius}"

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        return f"Raster circle radius {radius}"

class Circle:
    def __init__(self, renderer: Renderer, radius: int):
        self.renderer = renderer
        self.radius = radius

    def draw(self):
        return self.renderer.render_circle(self.radius)

print(Circle(VectorRenderer(), 5).draw())  # Vector circle radius 5
```

### Composite
Composes objects into tree structures and manipulates them uniformly.
```python
class FileSystemEntry:
    def display(self, depth=0):
        raise NotImplementedError

class File(FileSystemEntry):
    def __init__(self, name):
        self.name = name

    def display(self, depth=0):
        print("  " * depth + self.name)

class Folder(FileSystemEntry):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, entry: FileSystemEntry):
        self.children.append(entry)

    def display(self, depth=0):
        print("  " * depth + self.name)
        for child in self.children:
            child.display(depth + 1)

root = Folder("root")
root.add(File("file.txt"))
root.display()
```

### Decorator
Adds responsibilities to objects dynamically.
```python
from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

@bold
def greet(name):
    return f"Hello {name}"

print(greet("Ada"))  # <b>Hello Ada</b>
```

### Facade
Provides a simplified interface to a complex subsystem.
```python
class CPU:
    def freeze(self):
        return "CPU freeze"

class Memory:
    def load(self):
        return "Memory load"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()

    def start(self):
        return [self.cpu.freeze(), self.memory.load()]

print(ComputerFacade().start())
```

### Flyweight
Minimizes memory use by sharing as much data as possible among similar objects.
```python
class TreeType:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class TreeFactory:
    _types = {}

    @classmethod
    def get_tree_type(cls, name, color):
        key = (name, color)
        if key not in cls._types:
            cls._types[key] = TreeType(name, color)
        return cls._types[key]

forest = [TreeFactory.get_tree_type("oak", "green") for _ in range(3)]
print(len(set(map(id, forest))))  # 1
```

### Proxy
Provides a surrogate or placeholder for another object to control access.
```python
class Image:
    def display(self):
        raise NotImplementedError

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._load_from_disk()

    def _load_from_disk(self):
        print(f"Loading {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")

class LazyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if not self._real_image:
            self._real_image = RealImage(self.filename)
        self._real_image.display()

LazyImage("photo.png").display()
```

## Week 3: Behavioral Patterns
Focus: Algorithms and assignment of responsibilities between objects.

### Chain of Responsibility
Passes requests along a chain of handlers.
```python
class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        handled = self._process(request)
        if not handled and self.successor:
            return self.successor.handle(request)
        return handled

class AuthHandler(Handler):
    def _process(self, request):
        return request.get("auth")

class DataHandler(Handler):
    def _process(self, request):
        return request.get("data")

chain = AuthHandler(DataHandler())
print(chain.handle({"auth": True, "data": "payload"}))  # True
```

### Command
Encapsulates a request as an object.
```python
class Light:
    def __init__(self):
        self.on = False

    def switch(self):
        self.on = not self.on
        return self.on

class SwitchCommand:
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        return self.light.switch()

print(SwitchCommand(Light()).execute())  # True
```

### Interpreter
Defines a representation for grammar and an interpreter that uses it.
```python
class Number:
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

expression = Add(Number(4), Number(5))
print(expression.interpret())  # 9
```

### Iterator
Provides a way to access elements sequentially without exposing underlying representation.
```python
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n >= 0:
            yield n
            n -= 1

print(list(Countdown(3)))  # [3, 2, 1, 0]
```

### Mediator
Defines an object that encapsulates how objects interact.
```python
class ChatRoom:
    def show_message(self, user, message):
        print(f"[{user}]: {message}")

class User:
    def __init__(self, name, room: ChatRoom):
        self.name = name
        self.room = room

    def send(self, message):
        self.room.show_message(self.name, message)

room = ChatRoom()
User("Alice", room).send("Hello")
```

### Memento
Captures and externalizes an object's internal state.
```python
class EditorMemento:
    def __init__(self, content):
        self.content = content

class Editor:
    def __init__(self):
        self.content = ""

    def type(self, text):
        self.content += text

    def save(self):
        return EditorMemento(self.content)

    def restore(self, memento: EditorMemento):
        self.content = memento.content

editor = Editor()
editor.type("Hello")
snapshot = editor.save()
editor.type(" world")
editor.restore(snapshot)
print(editor.content)  # Hello
```

### Observer
Defines a one-to-many dependency between objects.
```python
class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify(self, data):
        for observer in self._observers:
            observer(data)

subject = Subject()
subject.subscribe(lambda data: print(f"Got {data}"))
subject.notify("event")
```

### State
Allows an object to alter its behavior when its internal state changes.
```python
class TrafficLight:
    def __init__(self):
        self.state = "red"

    def change(self):
        transitions = {"red": "green", "green": "yellow", "yellow": "red"}
        self.state = transitions[self.state]
        return self.state

light = TrafficLight()
print(light.change())  # green
```

### Strategy
Defines a family of algorithms, encapsulates each, and makes them interchangeable.
```python
import math

def euclidean(a, b):
    return math.dist(a, b)

def manhattan(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))

class DistanceCalculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy(a, b)

calc = DistanceCalculator(manhattan)
print(calc.calculate((0, 0), (3, 4)))  # 7
```

### Template Method
Defines skeleton of an algorithm, deferring steps to subclasses.
```python
class DataPipeline:
    def run(self):
        data = self.extract()
        data = self.transform(data)
        self.load(data)

    def extract(self):
        raise NotImplementedError

    def transform(self, data):
        return data

    def load(self, data):
        raise NotImplementedError

class CSVToDB(DataPipeline):
    def extract(self):
        return ["row1", "row2"]

    def load(self, data):
        print(f"Loading {data}")

CSVToDB().run()
```

### Visitor
Represents an operation to be performed on elements of an object structure.
```python
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def accept(self, visitor):
        return visitor.visit_file(self)

class Folder:
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def accept(self, visitor):
        return visitor.visit_folder(self)

class SizeVisitor:
    def visit_file(self, file):
        return file.size

    def visit_folder(self, folder):
        return sum(child.accept(self) for child in folder.children)

structure = Folder("root", [File("a.txt", 2), File("b.txt", 3)])
print(SizeVisitor().visit_folder(structure))  # 5
```

## Week 4: Integration Project
- Select a domain (e.g., IoT, fintech, education) and implement a subsystem using at least one pattern from each category.
- Document trade-offs in choosing specific patterns and provide tests or scripts that exercise them.
- Present a walkthrough highlighting how Python features shape each implementation.

## Capstone Assessment
- Written exam covering recognition of pattern scenarios.
- Peer review of the integration project focusing on maintainability and readability.
- Final presentation demonstrating working code and explaining pattern choices.
