# Builder Pattern

**Type**: Creational Pattern

**Motivation**: The Builder Pattern is used in the `builder_pattern.py` to construct a complex object step by step. It separates the construction of an object from its representation, allowing the same construction process to create different representations.

## Use Cases

- When you want to construct complex objects step by step.
- When you want to reuse the same construction process to create different representations of a product.
- When you want to isolate complex construction code from the business logic of the product.

## Limitations

- The overall complexity of the code increases since the pattern requires creating multiple new classes.
- The builder pattern might be overkill for simple objects, as it could complicate the code unnecessarily.

