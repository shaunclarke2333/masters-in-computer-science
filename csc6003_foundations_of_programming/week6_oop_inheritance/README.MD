# Zoo Object-Oriented Programming Project

This project focuses on creating a simple class hierarchy to represent animals in a zoo. You will define a base `Animal` class and child classes such as `Bear`, `Elephant`, and `Penguin`, each inheriting common functionality while adding their own unique behavior.

## Requirements

### Base Class: `Animal`

Each animal should include the following **attributes** and **methods**, which are accessible through a menu system.

#### Attributes
- `name`: The name of the animal  
- `species`: The species of the animal  

#### Methods
- `make_sound()`:  
  Returns a generic animal sound. Each subclass will override this method with a species-specific sound.

- `info()`:  
  Returns a formatted string containing the animal’s name, species, and sound.

---

## Subclasses

You must include subclasses for `Bear`, `Elephant`, and `Penguin`. Each subclass inherits from the `Animal` class and overrides or extends methods and attributes.

### `Bear`
- **Additional Attribute:**  
  `fur_color` (string), such as "Brown", "White", or "Black & White".
- **Overridden Methods:**  
  - `make_sound()` should return a bear-specific roar.  
  - `info()` should include the fur color in the returned string.

### `Elephant`
- **Additional Attribute:**  
  `weight` (float), representing weight in kilograms.
- **Overridden Methods:**  
  - `make_sound()` should return an elephant "trumpet" sound.  
  - `info()` should include the elephant’s weight.

### `Penguin`
- **Additional Attribute:**  
  `height` (float), representing height in feet.
- **Overridden Methods:**  
  - `make_sound()` should return a penguin "squawk" sound.  
  - `info()` should include the penguin’s height.

---

## Main Program Requirements

Your `main` program should include a simple menu that allows the user to:

1. **Add animals** to the zoo (stored in a list).  
2. **Print all animals** currently in the zoo.  
3. **Print all animals of a specific type** (Bears, Elephants, or Penguins).

This structure demonstrates inheritance, method overriding, and basic class interaction through a user-driven menu system.
