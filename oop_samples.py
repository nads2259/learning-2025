"""Comprehensive object-oriented programming examples.

This module contains a collection of classes and helper functions that illustrate
object-oriented programming concepts in Python, ranging from the basics to
advanced techniques. Each concept is encapsulated in a dedicated example to keep
concerns isolated and make it easy to explore individual topics.
"""
from __future__ import annotations

from abc import ABC, ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Protocol, Type, TypeVar


# ---------------------------------------------------------------------------
# Basic class definition and instantiation
# ---------------------------------------------------------------------------
class BasicGreeter:
    """A minimal class showcasing attributes and instance methods."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a friendly greeting."""
        return f"Hello, {self.name}!"


# ---------------------------------------------------------------------------
# Class variables vs. instance variables
# ---------------------------------------------------------------------------
class LibraryMember:
    """Illustrate the difference between class-level and instance-level data."""

    total_members: int = 0  # Class variable shared by all instances

    def __init__(self, member_id: int, name: str) -> None:
        self.member_id = member_id  # Instance variable unique to the object
        self.name = name
        LibraryMember.total_members += 1

    def describe(self) -> str:
        return f"Member {self.member_id}: {self.name}"


# ---------------------------------------------------------------------------
# Encapsulation with properties
# ---------------------------------------------------------------------------
class BankAccount:
    """Demonstrate encapsulation by managing access to a private balance."""

    def __init__(self, owner: str, starting_balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = float(starting_balance)

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = float(value)

    def deposit(self, amount: float) -> None:
        self.balance = self.balance + amount


# ---------------------------------------------------------------------------
# Class methods and factory patterns
# ---------------------------------------------------------------------------
class Temperature:
    """Provide alternative constructors using class methods."""

    def __init__(self, celsius: float) -> None:
        self.celsius = float(celsius)

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> "Temperature":
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    def __repr__(self) -> str:
        return f"Temperature(celsius={self.celsius:.2f})"


# ---------------------------------------------------------------------------
# Static methods for utility behavior
# ---------------------------------------------------------------------------
class MathHelper:
    """House utility behavior unrelated to instance state."""

    @staticmethod
    def is_even(value: int) -> bool:
        return value % 2 == 0


# ---------------------------------------------------------------------------
# Single inheritance and method overriding
# ---------------------------------------------------------------------------
class Animal:
    def speak(self) -> str:
        return "..."


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


# ---------------------------------------------------------------------------
# Multiple inheritance and mixins
# ---------------------------------------------------------------------------
class WalkerMixin:
    def move(self) -> str:
        return "Walking on land"


class SwimmerMixin:
    def move(self) -> str:
        return "Swimming in water"


class AmphibiousRobot(WalkerMixin, SwimmerMixin):
    """Demonstrate method resolution order (MRO) with mixins."""

    def move(self) -> str:
        land_move = WalkerMixin.move(self)
        water_move = SwimmerMixin.move(self)
        return f"{land_move} and {water_move}"


# ---------------------------------------------------------------------------
# Composition over inheritance
# ---------------------------------------------------------------------------
class Engine:
    def start(self) -> str:
        return "Engine started"


class Car:
    """A car *has an* engine instead of inheriting from it."""

    def __init__(self, engine: Optional[Engine] = None) -> None:
        self.engine = engine or Engine()

    def start(self) -> str:
        return self.engine.start()


# ---------------------------------------------------------------------------
# Abstract base classes
# ---------------------------------------------------------------------------
class PaymentProcessor(ABC):
    """Define an interface for payment processors."""

    @abstractmethod
    def process(self, amount: float) -> str:
        raise NotImplementedError


class StripeProcessor(PaymentProcessor):
    def process(self, amount: float) -> str:
        return f"Processed ${amount:.2f} via Stripe"


# ---------------------------------------------------------------------------
# Duck typing via Protocols
# ---------------------------------------------------------------------------
class SupportsSpeak(Protocol):
    def speak(self) -> str:  # pragma: no cover - protocol definition only
        ...


def make_it_speak(entity: SupportsSpeak) -> str:
    """Illustrate duck typing with structural subtyping."""

    return entity.speak()


# ---------------------------------------------------------------------------
# Operator overloading
# ---------------------------------------------------------------------------
class Vector2D:
    """Support vector addition and comparison via operator overloading."""

    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------
@dataclass
class Point3D:
    """Use dataclasses to automatically generate boilerplate methods."""

    x: float
    y: float
    z: float = 0.0


# ---------------------------------------------------------------------------
# Descriptors
# ---------------------------------------------------------------------------
class CelsiusDescriptor:
    """Validate values assigned to the descriptor owner."""

    def __get__(self, instance: Any, owner: Type[Any]) -> Any:
        if instance is None:
            return self
        return instance.__dict__["_celsius"]

    def __set__(self, instance: Any, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature cannot go below absolute zero.")
        instance.__dict__["_celsius"] = value


class Thermometer:
    celsius = CelsiusDescriptor()

    def __init__(self, celsius: float = 0.0) -> None:
        self.celsius = celsius


# ---------------------------------------------------------------------------
# Metaclasses
# ---------------------------------------------------------------------------
class InterfaceMeta(ABCMeta):
    """Require implementing classes to define a 'schema' attribute."""

    def __new__(
        mcls,
        name: str,
        bases: tuple[type, ...],
        namespace: Dict[str, Any],
        **kwargs: Any,
    ) -> "InterfaceMeta":
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        if name != "BaseInterface" and "schema" not in namespace:
            raise TypeError("Concrete interfaces must define a 'schema' attribute.")
        return cls


class BaseInterface(metaclass=InterfaceMeta):
    pass


class UserPayload(BaseInterface):
    schema = {"id": int, "username": str}


# ---------------------------------------------------------------------------
# Custom exceptions
# ---------------------------------------------------------------------------
class ValidationError(Exception):
    """A custom exception for signaling validation problems."""


class User:
    """Show how custom exceptions integrate with class validation."""

    def __init__(self, username: str) -> None:
        if not username:
            raise ValidationError("Username must not be empty.")
        self.username = username


# ---------------------------------------------------------------------------
# Context managers with classes
# ---------------------------------------------------------------------------
class ManagedResource:
    """Implement the context manager protocol using special methods."""

    def __init__(self) -> None:
        self._open = False

    def __enter__(self) -> "ManagedResource":
        self._open = True
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self._open = False

    @property
    def is_open(self) -> bool:
        return self._open


# ---------------------------------------------------------------------------
# Fluent interfaces
# ---------------------------------------------------------------------------
class QueryBuilder:
    """Support method chaining to build queries."""

    def __init__(self) -> None:
        self._select: List[str] = []
        self._filters: List[str] = []

    def select(self, *fields: str) -> "QueryBuilder":
        self._select.extend(fields)
        return self

    def where(self, condition: str) -> "QueryBuilder":
        self._filters.append(condition)
        return self

    def build(self) -> str:
        select_part = ", ".join(self._select) or "*"
        where_part = f" WHERE {' AND '.join(self._filters)}" if self._filters else ""
        return f"SELECT {select_part} FROM table{where_part}"


# ---------------------------------------------------------------------------
# Polymorphism via strategy pattern
# ---------------------------------------------------------------------------
class DiscountStrategy(Protocol):
    def apply(self, total: float) -> float:  # pragma: no cover - protocol only
        ...


class NoDiscount:
    def apply(self, total: float) -> float:
        return total


class PercentageDiscount:
    def __init__(self, percent: float) -> None:
        self.percent = percent

    def apply(self, total: float) -> float:
        return total * (1 - self.percent / 100)


class Checkout:
    def __init__(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def total(self, items: Iterable[float]) -> float:
        subtotal = sum(items)
        return self.discount.apply(subtotal)


# ---------------------------------------------------------------------------
# Generic programming with TypeVar and factory methods
# ---------------------------------------------------------------------------
T = TypeVar("T", bound="Record")


class Record:
    """Base class providing a registry of subclasses."""

    registry: Dict[str, Type["Record"]] = {}

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        Record.registry[cls.__name__] = cls

    @classmethod
    def create(cls: Type[T], type_name: str, **kwargs: Any) -> T:
        try:
            subclass = cls.registry[type_name]
        except KeyError as exc:
            raise ValueError(f"Unknown record type: {type_name}") from exc
        return subclass(**kwargs)


class CustomerRecord(Record):
    def __init__(self, name: str, vip: bool = False) -> None:
        self.name = name
        self.vip = vip


class OrderRecord(Record):
    def __init__(self, order_id: int, total: float) -> None:
        self.order_id = order_id
        self.total = total


# ---------------------------------------------------------------------------
# Singleton pattern via overriding __new__
# ---------------------------------------------------------------------------
class SingletonLogger:
    _instance: Optional["SingletonLogger"] = None

    def __new__(cls) -> "SingletonLogger":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, "messages"):
            self.messages: List[str] = []

    def log(self, message: str) -> None:
        self.messages.append(message)


# ---------------------------------------------------------------------------
# Builder pattern using inner classes
# ---------------------------------------------------------------------------
class Computer:
    def __init__(self, cpu: str, ram: str, storage: str) -> None:
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def __repr__(self) -> str:
        return f"Computer(cpu={self.cpu!r}, ram={self.ram!r}, storage={self.storage!r})"

    class Builder:
        def __init__(self) -> None:
            self._cpu = ""
            self._ram = ""
            self._storage = ""

        def with_cpu(self, cpu: str) -> "Computer.Builder":
            self._cpu = cpu
            return self

        def with_ram(self, ram: str) -> "Computer.Builder":
            self._ram = ram
            return self

        def with_storage(self, storage: str) -> "Computer.Builder":
            self._storage = storage
            return self

        def build(self) -> "Computer":
            return Computer(self._cpu, self._ram, self._storage)


# ---------------------------------------------------------------------------
# Method resolution order exploration helper
# ---------------------------------------------------------------------------
def describe_mro(cls: Type[Any]) -> List[str]:
    """Return the method resolution order of the provided class."""

    return [c.__name__ for c in cls.mro()]


# ---------------------------------------------------------------------------
# Demonstration helper functions
# ---------------------------------------------------------------------------
def demo_basic_usage() -> Dict[str, Any]:
    """Collect example outputs showcasing each concept."""

    LibraryMember.total_members = 0
    LibraryMember(1, "Alice")
    account = BankAccount("Alice", 100.0)
    account.deposit(50.0)
    stripe_message = StripeProcessor().process(10.0)
    vector_sum = Vector2D(1, 2) + Vector2D(3, 4)
    query = QueryBuilder().select("id", "name").where("active = 1").build()
    checkout_total = Checkout(PercentageDiscount(10)).total([100, 50])
    order_record = Record.create("OrderRecord", order_id=123, total=49.99)
    logger_a = SingletonLogger()
    logger_b = SingletonLogger()
    logger_a.log("Test message")
    with ManagedResource() as resource:
        managed_open = resource.is_open
    managed_closed = not resource.is_open

    return {
        "basic_greeting": BasicGreeter("Alice").greet(),
        "total_members": LibraryMember.total_members,
        "current_balance": account.balance,
        "temperature_from_f": Temperature.from_fahrenheit(212).celsius,
        "is_even": MathHelper.is_even(4),
        "dog_speaks": Dog().speak(),
        "amphibious_move": AmphibiousRobot().move(),
        "car_start": Car().start(),
        "stripe_message": stripe_message,
        "make_it_speak": make_it_speak(Dog()),
        "vector_sum": repr(vector_sum),
        "point_dataclass": Point3D(1, 2, 3),
        "thermometer": Thermometer(25).celsius,
        "user_payload_schema": UserPayload.schema,
        "managed_resource_open": managed_open,
        "managed_resource_closed": managed_closed,
        "query": query,
        "checkout_total": checkout_total,
        "order_record_total": order_record.total,
        "singleton_same": logger_a is logger_b,
        "computer": repr(Computer.Builder().with_cpu("M3").with_ram("32GB").with_storage("1TB").build()),
        "mro_amphibious": describe_mro(AmphibiousRobot),
    }


__all__ = [
    "AmphibiousRobot",
    "Animal",
    "BankAccount",
    "BasicGreeter",
    "Car",
    "Checkout",
    "Computer",
    "CustomerRecord",
    "Dog",
    "Engine",
    "InterfaceMeta",
    "LibraryMember",
    "ManagedResource",
    "MathHelper",
    "make_it_speak",
    "NoDiscount",
    "OrderRecord",
    "PaymentProcessor",
    "PercentageDiscount",
    "Point3D",
    "QueryBuilder",
    "Record",
    "SingletonLogger",
    "StripeProcessor",
    "SupportsSpeak",
    "Temperature",
    "Thermometer",
    "User",
    "UserPayload",
    "ValidationError",
    "Vector2D",
    "WalkerMixin",
    "SwimmerMixin",
    "describe_mro",
    "demo_basic_usage",
]
