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
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "category": category,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    contacts.append(contact)
    pass


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
    print("=============================================")
    print("            CONTACT BOOK (X contacts)")
    print("=============================================")
    print(" #  | Name            | Phone         | Category")
    x = 0
    for contact in contacts:
        x += 1
        print("---|-----------------|---------------|----------")
        print(f"{x} | {contact["name"]}   | {contact["phone"]}  | {contact["category"]}")
    pass


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
    print(" --- Contact Details ---")
    print(f"Name: {contact["name"]}")
    print(f"Phone: {contact["phone"]}")
    print(f"Email: {contact["email"]}")
    print(f"Category: {contact["category"]}")
    print(f"Added: {contact["created_at"]}")
    print("------------------------")
    pass


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
    contacts_matching = []
    for contact in contacts:
        if (query.lower() == contact["name"].lower()):
            contacts_matching.append(contact)
    return contacts_matching
    pass
    

def filter_by_category(contacts, category):
    """
    Return all contacts in a specific category.
    
    Returns:
        List of contacts matching the category
    """
    # TODO: Filter contacts by category
    contacts_matching = []
    for contact in contacts:
        if (category.lower() == contact["category"].lower()):
            contacts_matching.append(contact)
    return contacts_matching
    pass


def find_by_phone(contacts, phone):
    """
    Find a contact by exact phone number.
    
    Returns:
        The contact dictionary if found, None otherwise
    """
    # TODO: Search for contact with matching phone
    for contact in contacts:
        if (phone.lower() == contact["phone"]):
            return contact
    return None
    pass


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
    contact = find_by_phone(contacts, phone)
    if contact is None:
        return False
    else:
        contact.update({field: new_value})
        return True
    pass


def delete_contact(contacts, phone):
    """
    Delete a contact by phone number.
    
    Returns:
        True if deleted, False if not found
    """
    # TODO: Find and remove contact with matching phone
    contact = find_by_phone(contacts, phone)
    if contact == None:
        return False
    else:
        contacts.remove(contact)
        return True
    pass


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
    print(" --- Contact Book Statistics ---")
    print(f"Total Contacts: {len(contacts)}")
    print("By Category: ")
    categories = []
    most_recent_contact = contacts[0]
    for contact in contacts:
        if (contact["category"] not in categories):
            print(f" - {contact["category"]}: {len(filter_by_category(contacts, contact["category"]))}")
            categories.append(contact["category"])
        if (most_recent_contact["created_at"] > contact["created_at"]):
            most_recent_contact = contact
    print(f"Most Recent: {most_recent_contact["name"]} {most_recent_contact["created_at"]} ")
    pass


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
    contacts = []
    while True:
        display_menu()
        number_input = int(input("Enter number: "))
        if (number_input == 1):
            display_all_contacts(contacts)
        elif (number_input == 2):
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            category = input("Enter category: ")
            add_contact(contacts, name, phone, email, category)
        elif (number_input == 3):
            name = input("Enter name: ") 
            print(search_by_name(contacts, name))
        elif (number_input == 5):
            name = input("Enter name: ") 
            print(delete_contact(contacts, search_by_name(contacts, name)["phone"]))
        elif (number_input == 4):
            name = input("Enter name: ") 
            field = input("Enter field to update: ") 
            new_value = input("Enter field to new_value: ") 
            print(update_contact(contacts, search_by_name(contacts, name)["phone"], field, new_value))
        elif (number_input == 6):
            display_statistics()
        elif (number_input == 0):
            break
        else:
            print("Invalid Input")
    pass


# =============================================================================
# Test Code - Add sample data and test functions
# =============================================================================

if __name__ == "__main__":
    print("Contact Book Application")
    print("=" * 40)
    
    add_contact(contacts, "Andrew Ziets", "609-712-6296", "andrewziets@gmail.com", "Myself")
    add_contact(contacts, "Joanna Ziets", "609-577-4438", "kjziets@gmail.com", "Parent")
    add_contact(contacts, "Matthew Sutherland", "382-193-2193", "mcsuthie@icloud.com", "Friend")
    add_contact(contacts, "James Jiang", "219-939-3949", "mobai@gmail.com", "Friend")
    add_contact(contacts, "Hayden Caldwell", "492-393-3902", "hwc11@case.edu", "Enemy")
    
    # TODO: Test your functions
    display_all_contacts(contacts)
    results = search_by_name(contacts, "andrew ziets")
    print(results)
    results2 = filter_by_category(contacts, "Friend")
    print(results2)
    results3 = find_by_phone(contacts, "492-393-3902")
    print(results3)
    print(update_contact(contacts, "219-939-3949", "email", "mobai@icloud.com"))
    print(find_by_phone(contacts, "219-939-3949"))
    print(delete_contact(contacts, "219-939-3949"))
    print(find_by_phone(contacts, "219-939-3949"))
    display_all_contacts(contacts)
    display_statistics(contacts)

    # STRETCH: Uncomment to run interactive menu
    main()