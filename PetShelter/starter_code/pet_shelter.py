# pet_shelter.py - Pet Shelter Management System
# Starter code for e005-exercise-oop

"""
Pet Shelter Management System
-----------------------------
A system to manage animals in a pet shelter using OOP principles.

Class Hierarchy:
        Animal (Base Class)
       /       \
    Dog         Cat
   /   \          \
Puppy  ServiceDog  Kitten

Complete the TODO sections to finish the implementation.
"""


# =============================================================================
# Task 1: Base Animal Class
# =============================================================================

from tkinter import colorchooser


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


# =============================================================================
# Task 2: Dog and Cat Classes
# =============================================================================

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
        # TODO: Call parent constructor with species="Cat"
        # TODO: Set self.color
        # TODO: Set self.is_indoor
        super().__init__(name, age, "Cat")
        self.color = color
        self.is_indoor = is_indoor
    
    def speak(self):
        """Cats meow."""
        # TODO: Return "{name} says Meow!"
        return f"{self.name} says Meow!"
    
    def scratch(self):
        """Cats scratch."""
        return f"{self.name} scratches the furniture!"
    
    def describe(self):
        """Override to include color and indoor status."""
        # TODO: Get base description from parent
        # TODO: Add color and indoor/outdoor status
        base = super().describe()
        indoor_outdoor = "indoor" if self.is_indoor else "outdoor"
        return f"{base} - {self.color}, {indoor_outdoor}"


# =============================================================================
# Task 3: Specialized Classes
# =============================================================================

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
            name: Dog's name
            age: Age in years
            breed: Dog breed
            service_type: Type of service (e.g., "guide", "therapy", "search")
        """
        # TODO: Call parent constructor with is_trained=True
        # TODO: Set self.service_type
        super().__init__(name, age, breed, is_trained=True)
        self.service_type = service_type
    
    def perform_service(self):
        """Perform the dog's service."""
        # TODO: Return "{name} performs {service_type} duties."
        return f"{self.name} performs {self.service_type} duties."
    
    def describe(self):
        """Include service type in description."""
        # TODO: Get base description and add service type
        base = super().describe()
        return f"{base} - {self.service_type}"


class Kitten(Cat):
    """A kitten (cat under 1 year old)."""
    
    def __init__(self, name, age_months, color):
        """
        Initialize a kitten.
        
        Args:
            name: Kitten's name
            age_months: Age in months
            color: Kitten's color/pattern
        """
        # TODO: Convert months to years
        # TODO: Call parent constructor
        # TODO: Store age_months
        age_years = age_months / 12
        super().__init__(name, age_years, color)
        self.age_months = age_months
    
    def speak(self):
        """Kittens mew."""
        # TODO: Return "{name} says Mew! Mew!"
        return f"{self.name} says Mew! Mew!"
    
    def describe(self):
        """Show age in months for kittens."""
        # TODO: Similar to Puppy.describe()
        status = "adopted" if self._adopted else "available"
        return f"{self.name} is a {self.age_months}-month-old {self.color} kitten ({status})"
# =============================================================================
# Task 4: The Shelter Class
# =============================================================================

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
        # TODO: Loop through animals and return one with matching name
        # TODO: Return None if not found
        for animal in self.animals:
            if animal.name == name:
                return animal
        return None

    def list_available(self):
        """List all animals available for adoption."""
        # TODO: Return list of animals where is_adopted() is False
        return [animal for animal in self.animals if not animal.is_adopted()]

    def list_by_species(self, species):
        """List all animals of a specific species."""
        # TODO: Filter self.animals by species
        return [animal for animal in self.animals if species == animal.species]

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


# =============================================================================
# Task 5: Demonstration
# =============================================================================

def main():
    """Demonstrate the pet shelter system."""
    
    # Create shelter
    shelter = Shelter("Happy Paws Rescue")
    
    # Add various animals (using completed classes)
    shelter.add_animal(Dog("Buddy", 3, "Golden Retriever", True))
    # TODO: Add a Cat
    # TODO: Add a Puppy
    # TODO: Add a ServiceDog
    # TODO: Add a Kitten
    shelter.add_animal(Cat("Whiskers", 4, "White", False))
    shelter.add_animal(Puppy("Clifford", 11, "Labrador"))
    shelter.add_animal(ServiceDog("Mr.Peanutbutter", 5, "Doberman", "therapy"))
    shelter.add_animal(Kitten("Muffin", 9, "Gray"))

    
    # Display all animals
    shelter.display_all()

    # Demonstrate polymorphism
    shelter.make_all_speak()
    
    # Adopt an animal
    print("\n--- Adoption ---")
    print(shelter.adopt_animal("Buddy"))
    
    # Try to adopt again
    print(shelter.adopt_animal("Buddy"))
    
    # Show statistics
    stats = shelter.get_statistics()
    print(f"\n--- Shelter Statistics ---")
    print(f"  Total: {stats['total']}")
    print(f"  Available: {stats['available']}")
    print(f"  Adopted: {stats['adopted']}")
    print(f"  By Species: {stats['by_species']}")


if __name__ == "__main__":
    main()
