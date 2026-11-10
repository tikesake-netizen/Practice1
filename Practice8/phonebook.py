
from connect import connect


def show_contacts():
    connection = connect()

    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM phonebook ORDER BY id")
        contacts = cursor.fetchall()

        print("\n--- PHONEBOOK CONTACTS ---")

        if not contacts:
            print("PhoneBook is empty.")
        else:
            for contact in contacts:
                print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]}")

        cursor.close()

    except Exception as error:
        print("Error:", error)

    finally:
        connection.close()


def search_contact():
    search_text = input("Enter name or phone: ")

    connection = connect()

    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM search_phonebook(%s)",
            (search_text,)
        )

        contacts = cursor.fetchall()

        print("\n--- SEARCH RESULTS ---")

        if not contacts:
            print("Contact not found.")
        else:
            for contact in contacts:
                print(contact)

        cursor.close()

    except Exception as error:
        print("Error:", error)

    finally:
        connection.close()


def add_or_update_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    connection = connect()

    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute(
            "CALL add_or_update_user(%s, %s)",
            (name, phone)
        )

        connection.commit()
        print("Contact added or updated successfully!")

        cursor.close()

    except Exception as error:
        connection.rollback()
        print("Error:", error)

    finally:
        connection.close()


def add_multiple_contacts():
    names = input("Enter names separated by commas: ").split(",")
    phones = input("Enter phones separated by commas: ").split(",")

    names = [name.strip() for name in names]
    phones = [phone.strip() for phone in phones]

    connection = connect()

    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute(
            "CALL add_users_batch(%s, %s)",
            (names, phones)
        )

        connection.commit()
        print("Batch operation completed!")

        cursor.close()

    except Exception as error:
        connection.rollback()
        print("Error:", error)

    finally:
        connection.close()


def show_page():
    try:
        page_number = int(input("Enter page number: "))
        page_size = int(input("Enter page size: "))

        connection = connect()

        if connection is None:
            return

        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM get_phonebook_page(%s, %s)",
                (page_number, page_size)
            )

            contacts = cursor.fetchall()

            print("\n--- PHONEBOOK PAGE ---")

            if not contacts:
                print("No contacts on this page.")
            else:
                for contact in contacts:
                    print(contact)

            cursor.close()

        finally:
            connection.close()

    except ValueError:
        print("Please enter valid numbers.")

    except Exception as error:
        print("Error:", error)


def delete_contact():
    search_text = input("Enter name or phone to delete: ")

    connection = connect()

    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute(
            "CALL delete_phonebook_contact(%s)",
            (search_text,)
        )

        connection.commit()
        cursor.close()

    except Exception as error:
        connection.rollback()
        print("Error:", error)

    finally:
        connection.close()


def main():
    while True:
        print("\n========== PHONEBOOK ==========")
        print("1. Show all contacts")
        print("2. Search contact")
        print("3. Add or update contact")
        print("4. Add multiple contacts")
        print("5. Show contacts by pages")
        print("6. Delete contact")
        print("0. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_contacts()

        elif choice == "2":
            search_contact()

        elif choice == "3":
            add_or_update_contact()

        elif choice == "4":
            add_multiple_contacts()

        elif choice == "5":
            show_page()

        elif choice == "6":
            delete_contact()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()