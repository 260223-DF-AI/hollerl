# contact_book.py - Contact Book Application
# Starter code for e003-exercise-data-structures

"""
Contact Book Application
------------------------
A simple contact management system using Python data structures.

Data Structure:
- Each contact is a dictionary with: name, phone, email, category, created_at
- All contacts are stored in a list

Complete the TODO sections below to finish the application.
"""

from datetime import datetime

# =============================================================================
# Initialize Contact Book
# =============================================================================
contacts = []


# =============================================================================
# TODO: Task 1 - Create the Contact Book
# =============================================================================

def add_contact(contacts, name, phone, email, category):
    """
    Add a new contact to the contact book.
    
    Args:
        contacts: The list of all contacts
        name: Contact's full name
        phone: Contact's phone number
        email: Contact's email address
        category: One of: friend, family, work, other
    
    Returns:
        The created contact dictionary
    """
    # TODO: Create a contact dictionary with all fields
    # TODO: Add created_at timestamp using datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # TODO: Append to contacts list
    # TODO: Return the new contact
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "category": category,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    return contacts[-1]


# =============================================================================
# TODO: Task 2 - Display Contacts
# =============================================================================

def display_all_contacts(contacts):
    """
    Display all contacts in a formatted table.
    
    Output format:
    =============================================
                CONTACT BOOK (X contacts)
    =============================================
    #  | Name            | Phone         | Category
    ---|-----------------|---------------|----------
    1  | Alice Johnson   | 555-123-4567  | friend
    ...
    """
    # TODO: Print header with contact count
    # TODO: Print table headers
    # TODO: Loop through contacts and print each row
    # TODO: Print footer
    print("=" * 44)
    print(f"            CONTACT BOOK ({len(contacts)} contacts)")
    print("=" * 44)
    print(f"#  | Name            | Phone         | Category")
    print("-" * 44)
    number = 0
    for x in contacts:
        number += 1
        print(f"{number:<3}| {x['name']:<15} | {x['phone']:<13} | {x['category']}")


def display_contact_details(contact):
    """
    Display detailed information for a single contact.
    
    Output format:
    --- Contact Details ---
    Name:     [name]
    Phone:    [phone]
    Email:    [email]
    Category: [category]
    Added:    [created_at]
    ------------------------
    """
    # TODO: Print formatted contact details
    print("--- Contact Details ---")
    print(f"Name:     {contact['name']}")
    print(f"Phone:    {contact['phone']}")
    print(f"Email:    {contact['email']}")
    print(f"Category: {contact['category']}")
    print(f"Added:    {contact['created_at']}")
    print("------------------------")


# =============================================================================
# TODO: Task 3 - Search Functionality
# =============================================================================

def search_by_name(contacts, query):
    """
    Find contacts whose name contains the query string.
    Case-insensitive search.
    
    Returns:
        List of matching contacts
    """
    # TODO: Filter contacts where query is in name (case-insensitive)
    # Hint: Use list comprehension and .lower()
    return [contact for contact in contacts if query.lower() in contact['name'].lower()]


def filter_by_category(contacts, category):
    """
    Return all contacts in a specific category.
    
    Returns:
        List of contacts matching the category
    """
    # TODO: Filter contacts by category
    return [contact for contact in contacts if category == contact['category']]


def find_by_phone(contacts, phone):
    """
    Find a contact by exact phone number.
    
    Returns:
        The contact dictionary if found, None otherwise
    """
    # TODO: Search for contact with matching phone
    found_contact = [contact for contact in contacts if phone == contact['phone']]
    if len(found_contact) > 0:
        return found_contact[0]
    return None


# =============================================================================
# TODO: Task 4 - Update and Delete
# =============================================================================

def update_contact(contacts, phone, field, new_value):
    """
    Update a specific field of a contact.
    
    Args:
        contacts: The list of all contacts
        phone: Phone number to identify the contact
        field: The field to update (name, phone, email, or category)
        new_value: The new value for the field
    
    Returns:
        True if updated, False if contact not found
    """
    # TODO: Find contact by phone
    # TODO: Update the specified field
    # TODO: Return success/failure
    changing_contact = find_by_phone(contacts, phone)
    if changing_contact is not None:
        changing_contact.update({field: new_value})
        return True
    return False


def delete_contact(contacts, phone):
    """
    Delete a contact by phone number.
    
    Returns:
        True if deleted, False if not found
    """
    # TODO: Find and remove contact with matching phone
    removing_contact = find_by_phone(contacts, phone)
    if removing_contact is not None:
        contacts.remove(removing_contact)
        return True
    return False


# =============================================================================
# TODO: Task 5 - Statistics
# =============================================================================

def display_statistics(contacts):
    """
    Display statistics about the contact book.
    
    Output:
    --- Contact Book Statistics ---
    Total Contacts: X
    By Category:
      - Friends: X
      - Family: X
      - Work: X
      - Other: X
    Most Recent: [name] (added [date])
    -------------------------------
    """
    # TODO: Count total contacts
    # TODO: Count contacts by category
    # TODO: Find most recently added contact
    print("--- Contact Book Statistics ---")
    print(f"Total Contacts: {len(contacts)}")
    print("By Category:")
    print(f"  - Friends: {len(filter_by_category(contacts, 'friend'))}")
    print(f"  - Family: {len(filter_by_category(contacts, 'family'))}")
    print(f"  - Work: {len(filter_by_category(contacts, 'work'))}")
    print(f"  - Other: {len(filter_by_category(contacts, 'other'))}")
    print(f"Most Recent: {contacts[-1]['name']} (added {contacts[-1]['created_at']})")
    print("-------------------------------")


# =============================================================================
# STRETCH GOAL: Interactive Menu
# =============================================================================

def display_menu():
    """Display the main menu."""
    print("\n========== CONTACT BOOK ==========")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. View statistics")
    print("0. Exit")
    print("==================================")


def main():
    """Main function with interactive menu."""
    # TODO: Implement menu loop
    # Use while True and break on exit choice
    while True:
        display_menu()
        choice = input()
        match choice:
            case "1":
                display_all_contacts(contacts)
            case "2":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                category = input("Enter category (friend, family, work, other): ")
                add_contact(contacts, name, phone, email, category)
            case "3":
                search_choice = input("Search by (1) Name, (2) Category, (3) Phone: ")
                if search_choice == "1":
                    query = input("Enter name to search: ")
                    results = search_by_name(contacts, query)
                elif search_choice == "2":
                    category = input("Enter category to search: ")
                    results = filter_by_category(contacts, category)
                else:
                    phone = input("Enter phone to search: ")
                    results = [find_by_phone(contacts, phone)]
                for contact in results:
                    display_contact_details(contact)
            case "4":
                phone = input("Enter phone of contact to update: ")
                field = input("Enter field to update (name, phone, email, category): ")
                new_value = input(f"Enter new value for {field}: ")
                update_contact(contacts, phone, field, new_value)
            case "5":
                phone = input("Enter phone of contact to delete: ")
                delete_contact(contacts, phone)
            case "6":
                display_statistics(contacts)
            case "0":
                break

# =============================================================================
# Test Code - Add sample data and test functions
# =============================================================================
"""
if __name__ == "__main__":
    print("Contact Book Application")
    print("-" * 40)
    
    # TODO: Add at least 5 sample contacts
    # add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    print("-" * 40)
    print("TASK 1 & 2: Adding Sample Contacts and Displaying")
    print("-" * 40)
    add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    add_contact(contacts, "Bob Smith", "555-987-6543", "bob@work.com", "work")
    add_contact(contacts, "Carol White", "555-456-7890", "carol@family.net", "family")
    add_contact(contacts, "David Brown", "555-321-4321", "david@other.com", "other")
    add_contact(contacts, "Eve Davis", "555-654-3210", "eve@other.com", "other")

    
    # TODO: Test your functions
    # display_all_contacts(contacts)
    # results = search_by_name(contacts, "alice")
    # etc.
    display_all_contacts(contacts)
    display_contact_details(contacts[2])
    
    print("-" * 40)
    print("TASK 3: Testing Search Functions")
    print("-" * 40)
    print(search_by_name(contacts, "it"))
    print(filter_by_category(contacts, "other"))
    print(find_by_phone(contacts, "555-321-4321"))
    
    print("-" * 40)
    print("TASK 4: Testing Update and Delete")
    print("-" * 40)
    print(update_contact(contacts, "555-987-6543", "category", "friend"))
    print(delete_contact(contacts, "555-321-4321"))
    display_all_contacts(contacts)
    
    print("-" * 40)
    print("TASK 5: Displaying Statistics")
    print("-" * 40)
    display_statistics(contacts)
"""    
    # STRETCH: Uncomment to run interactive menu
main()
