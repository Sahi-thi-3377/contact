def add_contact(contacts, name, phone):
    contacts[name] = phone
    return contacts

if __name__ == "__main__":
    my_contacts = {}
    updated_contacts = add_contact(my_contacts, "Ravi", "9876543210")
    print(updated_contacts)