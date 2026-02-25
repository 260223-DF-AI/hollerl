# e003: Exercise - Data Structures

## Overview

| Attribute | Value |
|-----------|-------|
| **Mode** | Implementation (Code Lab) |
| **Duration** | 3-4 hours |
| **Prerequisites** | c020-c032 (Data types), d004 (Data types demo) |
| **Deliverable** | A Python contact book application using dictionaries and lists |

---

## Learning Objectives

By completing this exercise, you will:

- Work with lists, dictionaries, and tuples
- Perform CRUD operations on data structures
- Use dictionary methods for data manipulation
- Format and display structured data
- Apply datetime for timestamps

---

## The Scenario

You're building a **Contact Book** application that stores and manages personal contacts. Each contact will have multiple fields, and you'll be able to add, view, search, and delete contacts.

---

## Setup

### Prerequisites

- Python 3.x installed
- Completion of Tuesday's exercises

### Getting Started

1. Navigate to the `starter_code/` folder
2. Open `contact_book.py` in your editor
3. Follow the tasks below to complete the application

---

## Data Structure

Each contact should be a dictionary with the following structure:

```python
contact = {
    "name": "Alice Johnson",
    "phone": "555-123-4567",
    "email": "alice@example.com",
    "category": "friend",  # friend, family, work, other
    "created_at": "2024-01-15 10:30:00"
}
```

All contacts are stored in a list:

```python
contacts = [contact1, contact2, contact3, ...]
```

---

## Core Tasks

### Task 1: Create the Contact Book (30 min)

1. **Initialize an empty contacts list:**

   ```python
   contacts = []
   ```

2. **Create a function to add a contact:**

   ```python
   def add_contact(contacts, name, phone, email, category):
       """Add a new contact to the contact book."""
       # Create a contact dictionary
       # Add created_at timestamp using datetime
       # Append to contacts list
       pass
   ```

3. **Test by adding 3 sample contacts:**

   ```python
   add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
   add_contact(contacts, "Bob Smith", "555-987-6543", "bob@work.com", "work")
   add_contact(contacts, "Carol White", "555-456-7890", "carol@family.net", "family")
   ```

---

### Task 2: Display Contacts (45 min)

1. **Create a function to display all contacts:**

   ```python
   def display_all_contacts(contacts):
       """Display all contacts in a formatted table."""
       # Print header
       # Loop through contacts and print each one
       # Show count at the end
       pass
   ```

   Expected output format:

   ```
   =============================================
               CONTACT BOOK (3 contacts)
   =============================================
   #  | Name            | Phone         | Category
   ---|-----------------|---------------|----------
   1  | Alice Johnson   | 555-123-4567  | friend
   2  | Bob Smith       | 555-987-6543  | work
   3  | Carol White     | 555-456-7890  | family
   =============================================
   ```

2. **Create a function to display a single contact's details:**

   ```python
   def display_contact_details(contact):
       """Display detailed information for a single contact."""
       pass
   ```

   Expected output:

   ```
   --- Contact Details ---
   Name:     Alice Johnson
   Phone:    555-123-4567
   Email:    alice@example.com
   Category: friend
   Added:    2024-01-15 10:30:00
   ------------------------
   ```

---

### Task 3: Search Functionality (45 min)

1. **Search by name (partial match):**

   ```python
   def search_by_name(contacts, query):
       """Find contacts whose name contains the query string."""
       # Return a list of matching contacts
       # Use .lower() for case-insensitive search
       pass
   ```

2. **Filter by category:**

   ```python
   def filter_by_category(contacts, category):
       """Return all contacts in a specific category."""
       pass
   ```

3. **Find by exact phone number:**

   ```python
   def find_by_phone(contacts, phone):
       """Find a contact by exact phone number. Return None if not found."""
       pass
   ```

---

### Task 4: Update and Delete (45 min)

1. **Update a contact:**

   ```python
   def update_contact(contacts, phone, field, new_value):
       """
       Update a specific field of a contact.
       Find contact by phone number, update the specified field.
       Return True if updated, False if contact not found.
       """
       pass
   ```

2. **Delete a contact:**

   ```python
   def delete_contact(contacts, phone):
       """
       Delete a contact by phone number.
       Return True if deleted, False if not found.
       """
       pass
   ```

---

### Task 5: Statistics (30 min)

Create a function to display contact book statistics:

```python
def display_statistics(contacts):
    """Display statistics about the contact book."""
    pass
```

Output:

```
--- Contact Book Statistics ---
Total Contacts: 10
By Category:
  - Friends: 4
  - Family: 3
  - Work: 2
  - Other: 1
Most Recent: Alice Johnson (added 2024-01-15)
-------------------------------
```

---

### Stretch Goal: Interactive Menu (Optional, 45 min)

Create an interactive menu system:

```
========== CONTACT BOOK ==========
1. View all contacts
2. Add new contact
3. Search contacts
4. Update contact
5. Delete contact
6. View statistics
0. Exit
==================================
Enter choice:
```

Use a while loop to keep the program running until the user chooses to exit.

---

## Definition of Done

- [ ] Contacts stored as list of dictionaries
- [ ] Can add contacts with all required fields
- [ ] Can display all contacts in formatted table
- [ ] Can search by name (case-insensitive)
- [ ] Can filter by category
- [ ] Can update and delete contacts
- [ ] Statistics function works correctly
- [ ] (Stretch) Interactive menu implemented

---

## Submission

1. Complete the `contact_book.py` script
2. Include at least 5 sample contacts
3. Demonstrate each function with test calls
4. Take screenshots of the output
5. Submit code and screenshots

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| KeyError | Check that dictionary keys match exactly |
| Contact not found | Verify phone format matches stored format |
| Empty results | Check case sensitivity in searches |
