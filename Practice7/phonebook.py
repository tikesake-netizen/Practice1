
import csv
from connect import connect


def show_contacts():
    conn = connect()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook ORDER BY id")
        contacts = cur.fetchall()

        print("\n===== PHONE BOOK =====")
        for contact in contacts:
            print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]}")

        cur.close()

    except Exception as error:
        print("Error:", error)

    finally:
        conn.close()


def import_from_csv():
    conn = connect()
    if conn is None:
        return

    try:
        cur = conn.cursor()

        with open("contacts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                cur.execute(
                    """
                    INSERT INTO phonebook (name, phone)
                    VALUES (%s, %s)
                    ON CONFLICT (name) DO NOTHING
                    """,
                    (row["name"], row["phone"])
                )

        conn.commit()
        print("Contacts imported successfully!")
        cur.close()

    except Exception as error:
        conn.rollback()
        print("Import error:", error)

    finally:
        conn.close()


def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not phone:
        print("Name and phone cannot be empty!")
        return

    conn = connect()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
            (name, phone)
        )

        conn.commit()
        print("Contact added successfully!")
        cur.close()

    except Exception as error:
        conn.rollback()
        print("Error:", error)

    finally:
        conn.close()


def update_contact():
    name = input("Enter current contact name: ").strip()

    print("\n1. Update name")
    print("2. Update phone")

    choice = input("Choose what to update: ")

    if choice == "1":
        column = "name"
        new_value = input("Enter new name: ").strip()

    elif choice == "2":
        column = "phone"
        new_value = input("Enter new phone: ").strip()

    else:
        print("Invalid choice!")
        return

    if not new_value:
        print("New value cannot be empty!")
        return

    conn = connect()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        query = f"UPDATE phonebook SET {column} = %s WHERE name = %s"
        cur.execute(query, (new_value, name))

        if cur.rowcount > 0:
            conn.commit()
            print("Contact updated successfully!")
        else:
            conn.rollback()
            print("Contact not found!")

        cur.close()

    except Exception as error:
        conn.rollback()
        print("Update error:", error)

    finally:
        conn.close()


def search_contact():
    print("\n1. Search by name")
    print("2. Search by phone prefix")

    choice = input("Choose search type: ")

    if choice == "1":
        value = input("Enter name or part of name: ").strip()

        query = """
            SELECT * FROM phonebook
            WHERE name ILIKE %s
            ORDER BY name
        """
        parameter = (f"%{value}%",)

    elif choice == "2":
        value = input("Enter phone prefix: ").strip()

        query = """
            SELECT * FROM phonebook
            WHERE phone LIKE %s
            ORDER BY name
        """
        parameter = (f"{value}%",)

    else:
        print("Invalid choice!")
        return

    if not value:
        print("Search value cannot be empty!")
        return

    conn = connect()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute(query, parameter)
        contacts = cur.fetchall()

        if contacts:
            print("\n===== SEARCH RESULTS =====")

            for contact in contacts:
                print(
                    f"ID: {contact[0]} | "
                    f"Name: {contact[1]} | "
                    f"Phone: {contact[2]}"
                )
        else:
            print("No contacts found!")

        cur.close()

    except Exception as error:
        print("Search error:", error)

    finally:
        conn.close()


def delete_contact():
    print("\n1. Delete by name")
    print("2. Delete by phone number")

    choice = input("Choose delete type: ")

    if choice == "1":
        value = input("Enter contact name: ").strip()
        column = "name"

    elif choice == "2":
        value = input("Enter phone number: ").strip()
        column = "phone"

    else:
        print("Invalid choice!")
        return

    if not value:
        print("Value cannot be empty!")
        return

    confirm = input(
        f"Are you sure you want to delete contact by {column} '{value}'? (yes/no): "
    )

    if confirm.lower() != "yes":
        print("Deletion cancelled.")
        return

    conn = connect()
    if conn is None:
        return

    try:
        cur = conn.cursor()

        query = f"DELETE FROM phonebook WHERE {column} = %s"
        cur.execute(query, (value,))

        if cur.rowcount > 0:
            conn.commit()
            print(f"Successfully deleted {cur.rowcount} contact(s)!")
        else:
            conn.rollback()
            print("Contact not found!")

        cur.close()

    except Exception as error:
        conn.rollback()
        print("Delete error:", error)

    finally:
        conn.close()


def main():
    while True:
        print("\n===== PHONE BOOK MENU =====")
        print("1. Show contacts")
        print("2. Import contacts from CSV")
        print("3. Add new contact")
        print("4. Update contact")
        print("5. Search contact")
        print("6. Delete contact")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_contacts()

        elif choice == "2":
            import_from_csv()

        elif choice == "3":
            add_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            search_contact()

        elif choice == "6":
            delete_contact()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()


        