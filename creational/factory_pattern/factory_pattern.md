# Factory Pattern

**Type**: Creational Pattern

**Motivation**: The Factory Pattern is used in the `factory_pattern.py` to create different types of Burger objects without exposing the creation logic to the client and providing a common interface for creating objects. This makes the code more flexible, scalable, and maintainable.

## Use Cases
- When the system needs to be independent of how its products are created and represented.
- When a class can't anticipate the type of objects it needs to create.
- When a class wants its subclasses to specify the objects it creates.

## Limitations
- The code can become more complicated since you need to introduce a lot of new subclasses which implement the factory method.
- Clients might have to subclass the Factory class just to create a particular type of object.