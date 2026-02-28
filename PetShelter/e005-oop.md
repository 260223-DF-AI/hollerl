# e005: Exercise - Object-Oriented Programming

## Overview

| Attribute | Value |
|-----------|-------|
| **Mode** | Implementation (Code Lab) |
| **Duration** | 3-4 hours |
| **Prerequisites** | c039-c043 (OOP concepts), d006 (OOP demo) |
| **Deliverable** | A class hierarchy demonstrating inheritance and polymorphism |

---

## Learning Objectives

By completing this exercise, you will:

- Design and implement a class hierarchy
- Use constructors, attributes, and methods
- Apply inheritance and method overriding
- Demonstrate polymorphism in action
- Practice encapsulation principles

---

## The Scenario

You're building a **Pet Shelter Management System**. The shelter houses different types of animals, and you need to model their behaviors and characteristics using OOP principles.

---

## Class Hierarchy

```
        Animal (Base Class)
       /       \
    Dog         Cat
   /   \          \
Puppy  ServiceDog  Kitten
```

---

## Setup

### Prerequisites

- Python 3.x installed
- Understanding of OOP concepts from Friday's content

### Getting Started

1. Navigate to the `starter_code/` folder
2. Open `pet_shelter.py` in your editor
3. Follow the tasks below to build the system

---

## Core Tasks

### Task 1: Base Animal Class (30 min)

Create the `Animal` base class:

```python
class Animal:
    """Base class for all animals in the shelter."""
    
    def __init__(self, name, age, species):
        """
        Initialize an animal.
        
        Args:
            name: The animal's name
            age: Age in years
            species: Type of animal
        """
        self.name = name
        self.age = age
        self.species = species
        self._adopted = False  # Protected attribute
    
    def speak(self):
        """Make a sound. To be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement speak()")
    
    def describe(self):
        """Return a description of the animal."""
        status = "adopted" if self._adopted else "available"
        return f"{self.name} is a {self.age}-year-old {self.species} ({status})"
    
    def adopt(self):
        """Mark the animal as adopted."""
        if self._adopted:
            return f"{self.name} has already been adopted!"
        self._adopted = True
        return f"Congratulations! You adopted {self.name}!"
    
    def is_adopted(self):
        """Check if animal is adopted."""
        return self._adopted
    
    def __str__(self):
        """String representation."""
        return f"{self.species}: {self.name} (Age: {self.age})"
```

---

### Task 2: Dog and Cat Classes (45 min)

Create specialized classes that inherit from `Animal`:

```python
class Dog(Animal):
    """A dog in the shelter."""
    
    def __init__(self, name, age, breed, is_trained=False):
        """
        Initialize a dog.
        
        Args:
            name: Dog's name
            age: Age in years
            breed: Dog breed (e.g., "Golden Retriever")
            is_trained: Whether the dog is house-trained
        """
        super().__init__(name, age, "Dog")
        self.breed = breed
        self.is_trained = is_trained
    
    def speak(self):
        """Dogs bark."""
        return f"{self.name} says Woof! Woof!"
    
    def fetch(self):
        """Dogs can fetch."""
        return f"{self.name} fetches the ball!"
    
    def describe(self):
        """Override to include breed and training."""
        base = super().describe()
        trained = "trained" if self.is_trained else "not trained"
        return f"{base} - {self.breed}, {trained}"


class Cat(Animal):
    """A cat in the shelter."""
    
    def __init__(self, name, age, color, is_indoor=True):
        """
        Initialize a cat.
        
        Args:
            name: Cat's name
            age: Age in years
            color: Cat's color/pattern
            is_indoor: Whether the cat is indoor-only
        """
        # TODO: Call parent constructor
        # TODO: Set cat-specific attributes
        pass
    
    def speak(self):
        """Cats meow."""
        # TODO: Return cat sound
        pass
    
    def scratch(self):
        """Cats scratch."""
        return f"{self.name} scratches the furniture!"
    
    def describe(self):
        """Override to include color and indoor status."""
        # TODO: Extend parent description with cat-specific info
        pass
```

---

### Task 3: Specialized Classes (45 min)

Create more specific subclasses:

```python
class Puppy(Dog):
    """A puppy (dog under 1 year old)."""
    
    def __init__(self, name, age_months, breed):
        """
        Initialize a puppy.
        
        Args:
            name: Puppy's name
            age_months: Age in months (not years!)
            breed: Puppy breed
        """
        # Convert months to years for parent
        age_years = age_months / 12
        super().__init__(name, age_years, breed, is_trained=False)
        self.age_months = age_months
    
    def speak(self):
        """Puppies yip."""
        return f"{self.name} says Yip! Yip!"
    
    def describe(self):
        """Show age in months for puppies."""
        status = "adopted" if self._adopted else "available"
        return f"{self.name} is a {self.age_months}-month-old {self.breed} puppy ({status})"


class ServiceDog(Dog):
    """A trained service dog."""
    
    def __init__(self, name, age, breed, service_type):
        """
        Initialize a service dog.
        
        Args:
            service_type: Type of service (e.g., "guide", "therapy", "search")
        """
        # TODO: Call parent constructor with is_trained=True
        # TODO: Set service_type attribute
        pass
    
    def perform_service(self):
        """Perform the dog's service."""
        # TODO: Return description of service
        pass
    
    def describe(self):
        """Include service type in description."""
        # TODO: Extend parent description
        pass


class Kitten(Cat):
    """A kitten (cat under 1 year old)."""
    
    # TODO: Implement similar to Puppy
    pass
```

---

### Task 4: The Shelter Class (45 min)

Create a class to manage all animals:

```python
class Shelter:
    """Manages the pet shelter."""
    
    def __init__(self, name):
        """Initialize the shelter."""
        self.name = name
        self.animals = []
    
    def add_animal(self, animal):
        """Add an animal to the shelter."""
        self.animals.append(animal)
        return f"{animal.name} has been added to {self.name}"
    
    def find_by_name(self, name):
        """Find an animal by name."""
        # TODO: Search and return matching animal or None
        pass
    
    def list_available(self):
        """List all animals available for adoption."""
        # TODO: Return list of non-adopted animals
        pass
    
    def list_by_species(self, species):
        """List all animals of a specific species."""
        # TODO: Filter by species
        pass
    
    def adopt_animal(self, name):
        """Adopt an animal by name."""
        animal = self.find_by_name(name)
        if animal:
            return animal.adopt()
        return f"No animal named {name} found."
    
    def make_all_speak(self):
        """Demonstrate polymorphism - all animals speak."""
        print(f"\n--- {self.name} Choir ---")
        for animal in self.animals:
            print(f"  {animal.speak()}")
    
    def get_statistics(self):
        """Return shelter statistics."""
        total = len(self.animals)
        adopted = sum(1 for a in self.animals if a.is_adopted())
        available = total - adopted
        
        species_count = {}
        for animal in self.animals:
            species = animal.species
            species_count[species] = species_count.get(species, 0) + 1
        
        return {
            "total": total,
            "adopted": adopted,
            "available": available,
            "by_species": species_count
        }
    
    def display_all(self):
        """Display all animals."""
        print(f"\n{'='*50}")
        print(f"  {self.name} - Current Residents")
        print(f"{'='*50}")
        for i, animal in enumerate(self.animals, 1):
            print(f"{i}. {animal.describe()}")
        print(f"{'='*50}")
```

---

### Task 5: Demonstration (30 min)

Write a `main()` function that demonstrates all OOP concepts:

```python
def main():
    # Create shelter
    shelter = Shelter("Happy Paws Rescue")
    
    # Add various animals
    shelter.add_animal(Dog("Buddy", 3, "Golden Retriever", True))
    shelter.add_animal(Cat("Whiskers", 5, "Orange Tabby"))
    shelter.add_animal(Puppy("Max", 4, "Labrador"))
    shelter.add_animal(ServiceDog("Rex", 4, "German Shepherd", "guide"))
    shelter.add_animal(Kitten("Mittens", 3, "Calico"))
    
    # Display all animals
    shelter.display_all()
    
    # Demonstrate polymorphism
    shelter.make_all_speak()
    
    # Adopt an animal
    print(shelter.adopt_animal("Buddy"))
    
    # Show statistics
    stats = shelter.get_statistics()
    print(f"\nShelter Statistics:")
    print(f"  Total: {stats['total']}")
    print(f"  Available: {stats['available']}")
    print(f"  Adopted: {stats['adopted']}")
```

---

## Expected Output

```
==================================================
  Happy Paws Rescue - Current Residents
==================================================
1. Buddy is a 3-year-old Dog (available) - Golden Retriever, trained
2. Whiskers is a 5-year-old Cat (available) - Orange Tabby, indoor
3. Max is a 4-month-old Labrador puppy (available)
4. Rex is a 4-year-old Dog (available) - German Shepherd, trained, guide dog
5. Mittens is a 3-month-old Calico kitten (available)
==================================================

--- Happy Paws Rescue Choir ---
  Buddy says Woof! Woof!
  Whiskers says Meow!
  Max says Yip! Yip!
  Rex says Woof! Woof!
  Mittens says Mew! Mew!

Congratulations! You adopted Buddy!

Shelter Statistics:
  Total: 5
  Available: 4
  Adopted: 1
```

---

## Definition of Done

- [ ] `Animal` base class with core attributes and methods
- [ ] `Dog` and `Cat` classes inherit from `Animal`
- [ ] `Puppy`, `ServiceDog`, and `Kitten` properly extend their parents
- [ ] `Shelter` class manages collection of animals
- [ ] `speak()` method demonstrates polymorphism
- [ ] All classes have proper `__str__` methods
- [ ] `main()` demonstrates all features
- [ ] Code runs without errors

---

## Stretch Goals

1. Add more animal types (Bird, Rabbit, etc.)
2. Implement a `save_to_file()` method
3. Add vaccination tracking
4. Create an interactive menu for the shelter

---

## Submission

1. Complete `pet_shelter.py`
2. Run the demonstration
3. Screenshot showing polymorphism (all animals speaking)
4. Submit code and screenshots
