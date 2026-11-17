
import csv
import json
from connect import connect


def get_group_id(cursor, group_name):
    if not group_name:
        return None

    cursor.execute(
        "SELECT id FROM groups WHERE name = %s",
        (group_name,)
    )

    result = cursor.fetchone()
    return result[0] if result else None


def save_contact(conn, record):
    name = str(record.get("name", "")).strip()
    phone = str(record.get("phone", "")).strip()
    email = record.get("email") or None
    birthday = record.get("birthday") or None
    group_name = record.get("group") or record.get("group_name")

    extra_phones = record.get("phones", [])

    if isinstance(extra_phones, str):
        extra_phones = [extra_phones]

    if not phone and extra_phones:
        first = extra_phones[0]
        phone = first.get("phone", "") if isinstance(first, dict) else str(first)

    if not name or not phone:
        raise ValueError("Name and phone are required.")

    cur = conn.cursor()

    group_id = get_group_id(cur, group_name)

    cur.execute("""
        INSERT INTO phonebook (name, phone, email, birthday, group_id)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name)
        DO UPDATE SET
            phone = EXCLUDED.phone,
            email = EXCLUDED.email,
            birthday = EXCLUDED.birthday,
            group_id = COALESCE(EXCLUDED.group_id, phonebook.group_id)
        RETURNING id
    """, (name, phone, email, birthday, group_id))

    contact_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO phones (contact_id, phone, type)
        VALUES (%s, %s, 'mobile')
        ON CONFLICT (contact_id, phone) DO NOTHING
    """, (contact_id, phone))

    for item in extra_phones:
        if isinstance(item, dict):
            extra_phone = str(item.get("phone", "")).strip()
            phone_type = item.get("type", "mobile")
        else:
            extra_phone = str(item).strip()
            phone_type = "mobile"

        if extra_phone:
            cur.execute("""
                INSERT INTO phones (contact_id, phone, type)
                VALUES (%s, %s, %s)
                ON CONFLICT (contact_id, phone) DO NOTHING
            """, (contact_id, extra_phone, phone_type))

    cur.close()
    return contact_id


def show_contacts(group_id=None, sort_by="id", direction="ASC",
                  limit=None, offset=0):

    sort_columns = {
        "id": "p.id",
        "name": "p.name",
        "birthday": "p.birthday",
        "created_at": "p.created_at"
    }

    sort_column = sort_columns.get(sort_by, "p.id")
    direction = "DESC" if direction.upper() == "DESC" else "ASC"

    conn = connect()

    if conn is None:
        return

    try:
        cur = conn.cursor()

        query = """
            SELECT
                p.id,
                p.name,
                p.email,
                p.birthday,
                g.name,
                COALESCE(STRING_AGG(DISTINCT ph.phone, ', '), p.phone)
            FROM phonebook p
            LEFT JOIN groups g ON p.group_id = g.id
            LEFT JOIN phones ph ON p.id = ph.contact_id
        """

        params = []

        if group_id is not None:
            query += " WHERE p.group_id = %s"
            params.append(group_id)

        query += f"""
            GROUP BY p.id, p.name, p.email, p.birthday,
                     p.phone, p.created_at, g.name
            ORDER BY {sort_column} {direction}
        """

        if limit is not None:
            query += " LIMIT %s OFFSET %s"
            params.extend([limit, offset])

        cur.execute(query, params)
        contacts = cur.fetchall()

        print("\n--- PHONEBOOK CONTACTS ---")

        if not contacts:
            print("No contacts found.")

        for contact in contacts:
            print(f"ID: {contact[0]}")
            print(f"Name: {contact[1]}")
            print(f"Email: {contact[2] or 'No email'}")
            print(f"Birthday: {contact[3] or 'Unknown'}")
            print(f"Group: {contact[4] or 'No group'}")
            print(f"Phones: {contact[5] or 'No phones'}")
            print("-" * 30)

        cur.close()

    except Exception as error:
        print("Error:", error)

    finally:
        conn.close()


def search_contact():
    search_text = input("Enter name, email or phone: ").strip()

    conn = connect()

    if conn is None:
        return

    try:
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM search_contacts(%s)",
            (search_text,)
        )

        results = cur.fetchall()

        print("\n--- SEARCH RESULTS ---")

        if not results:
            print("Contact not found.")

        for contact in results:
            print(contact)

        cur.close()

    except Exception as error:
        print("Error:", error)

    finally:
        conn.close()


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip() or None
    birthday = input("Enter birthday (YYYY-MM-DD): ").strip() or None

    conn = connect()

    if conn is None:
        return

    try:
        contact_id = save_contact(conn, {
            "name": name,
            "phone": phone,
            "email": email,
            "birthday": birthday
        })

        conn.commit()
        print(f"Contact saved successfully! ID: {contact_id}")

    except Exception as error:
        conn.rollback()
        print("Error:", error)

    finally:
        conn.close()


def add_extra_phone():
    try:
        contact_id = int(input("Enter contact ID: "))
        phone = input("Enter additional phone: ").strip()
        phone_type = input("Enter type (mobile/work/home): ").strip() or "mobile"

        conn = connect()

        if conn is None:
            return

        try:
            cur = conn.cursor()

            cur.execute(
                "CALL add_phone(%s, %s, %s)",
                (contact_id, phone, phone_type)
            )

            conn.commit()
            print("Phone added successfully!")

            cur.close()

        except Exception as error:
            conn.rollback()
            print("Error:", error)

        finally:
            conn.close()

    except ValueError:
        print("Contact ID must be a number.")


def move_contact():
    try:
        contact_id = int(input("Enter contact ID: "))

        conn = connect()

        if conn is None:
            return

        try:
            cur = conn.cursor()

            cur.execute("SELECT id, name FROM groups ORDER BY id")
            groups_list = cur.fetchall()

            print("\n--- GROUPS ---")

            for group in groups_list:
                print(f"{group[0]}. {group[1]}")

            group_id = int(input("Choose group ID: "))

            cur.execute(
                "CALL move_to_group(%s, %s)",
                (contact_id, group_id)
            )

            conn.commit()
            print("Contact moved successfully!")

            cur.close()

        except Exception as error:
            conn.rollback()
            print("Error:", error)

        finally:
            conn.close()

    except ValueError:
        print("Please enter valid numbers.")


def filter_by_group():
    conn = connect()

    if conn is None:
        return

    try:
        cur = conn.cursor()

        cur.execute("SELECT id, name FROM groups ORDER BY id")
        groups_list = cur.fetchall()

        print("\n--- AVAILABLE GROUPS ---")

        for group in groups_list:
            print(f"{group[0]}. {group[1]}")

        group_id = int(input("Enter group ID: "))

        cur.close()
        conn.close()

        show_contacts(group_id=group_id)

    except ValueError:
        print("Please enter a valid group ID.")
        conn.close()

    except Exception as error:
        print("Error:", error)
        conn.close()


def sort_contacts():
    print("\n--- SORT CONTACTS ---")
    print("1. By ID")
    print("2. By name")
    print("3. By birthday")
    print("4. By creation date")

    choice = input("Choose sorting option: ")

    sort_options = {
        "1": "id",
        "2": "name",
        "3": "birthday",
        "4": "created_at"
    }

    sort_by = sort_options.get(choice)

    if sort_by is None:
        print("Invalid choice.")
        return

    direction = input("Ascending or descending (ASC/DESC): ").strip().upper()

    if direction not in ("ASC", "DESC"):
        print("Invalid direction.")
        return

    show_contacts(sort_by=sort_by, direction=direction)


def show_page():
    try:
        page_size = int(input("Enter contacts per page: "))
        page_number = int(input("Enter page number: "))

        if page_size < 1 or page_number < 1:
            print("Numbers must be positive.")
            return

        conn = connect()

        if conn is None:
            return

        try:
            cur = conn.cursor()

            cur.execute("SELECT COUNT(*) FROM phonebook")
            total_contacts = cur.fetchone()[0]

            total_pages = (total_contacts + page_size - 1) // page_size

            if page_number > total_pages or total_pages == 0:
                print("Page does not exist.")
                return

            offset = (page_number - 1) * page_size

            print(f"\nPage {page_number} of {total_pages}")

            cur.close()

        finally:
            conn.close()

        show_contacts(limit=page_size, offset=offset)

    except ValueError:
        print("Please enter valid numbers.")

    except Exception as error:
        print("Error:", error)


def import_csv():
    file_path = input("Enter CSV file path: ").strip()

    conn = connect()

    if conn is None:
        return

    imported = 0

    try:
        with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    extra_phones = []

                    if row.get("additional_phones"):
                        extra_phones = [
                            phone.strip()
                            for phone in row["additional_phones"].split(";")
                            if phone.strip()
                        ]

                    save_contact(conn, {
                        "name": row.get("name"),
                        "phone": row.get("phone"),
                        "email": row.get("email"),
                        "birthday": row.get("birthday"),
                        "group": row.get("group"),
                        "phones": extra_phones
                    })

                    conn.commit()
                    imported += 1

                except Exception as error:
                    conn.rollback()
                    print(f"Skipped row: {error}")

        print(f"CSV import completed. Processed: {imported}")

    except Exception as error:
        print("CSV import error:", error)

    finally:
        conn.close()


def import_json():
    file_path = input("Enter JSON file path: ").strip()

    conn = connect()

    if conn is None:
        return

    imported = 0

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, dict):
            data = data.get("contacts", [])

        if not isinstance(data, list):
            raise ValueError("JSON must contain a list of contacts.")

        for record in data:
            try:
                save_contact(conn, record)
                conn.commit()
                imported += 1

            except Exception as error:
                conn.rollback()
                print(f"Skipped contact: {error}")

        print(f"JSON import completed. Processed: {imported}")

    except Exception as error:
        print("JSON import error:", error)

    finally:
        conn.close()


def export_json():
    file_path = input("Enter export filename (default contacts_export.json): ").strip()

    if not file_path:
        file_path = "contacts_export.json"

    conn = connect()

    if conn is None:
        return

    try:
        cur = conn.cursor()

        cur.execute("""
            SELECT p.id, p.name, p.phone, p.email,
                   p.birthday, g.name
            FROM phonebook p
            LEFT JOIN groups g ON p.group_id = g.id
            ORDER BY p.id
        """)

        contacts = cur.fetchall()
        result = []

        for contact in contacts:
            cur.execute("""
                SELECT phone, type
                FROM phones
                WHERE contact_id = %s
                ORDER BY id
            """, (contact[0],))

            phones = [
                {"phone": row[0], "type": row[1]}
                for row in cur.fetchall()
            ]

            result.append({
                "id": contact[0],
                "name": contact[1],
                "phone": contact[2],
                "email": contact[3],
                "birthday": str(contact[4]) if contact[4] else None,
                "group": contact[5],
                "phones": phones
            })

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)

        print(f"Export completed: {file_path}")

        cur.close()

    except Exception as error:
        print("Export error:", error)

    finally:
        conn.close()


def export_csv():
    file_path = input("Enter export filename (default contacts_export.csv): ").strip()

    if not file_path:
        file_path = "contacts_export.csv"

    conn = connect()

    if conn is None:
        return

    try:
        cur = conn.cursor()

        cur.execute("""
            SELECT p.id, p.name, p.phone, p.email,
                   p.birthday, g.name
            FROM phonebook p
            LEFT JOIN groups g ON p.group_id = g.id
            ORDER BY p.id
        """)

        contacts = cur.fetchall()

        with open(file_path, "w", encoding="utf-8-sig", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "id", "name", "phone", "email",
                "birthday", "group", "additional_phones"
            ])

            for contact in contacts:
                cur.execute("""
                    SELECT phone
                    FROM phones
                    WHERE contact_id = %s AND phone <> %s
                    ORDER BY id
                """, (contact[0], contact[2]))

                extra_phones = ";".join(
                    row[0] for row in cur.fetchall()
                )

                writer.writerow([
                    contact[0],
                    contact[1],
                    contact[2],
                    contact[3],
                    contact[4],
                    contact[5],
                    extra_phones
                ])

        print(f"CSV export completed: {file_path}")

        cur.close()

    except Exception as error:
        print("CSV export error:", error)

    finally:
        conn.close()


def main():
    while True:
        print("\n========== PHONEBOOK ==========")
        print("1. Show all contacts")
        print("2. Search contact")
        print("3. Add or update contact")
        print("4. Add additional phone")
        print("5. Move contact to group")
        print("6. Filter contacts by group")
        print("7. Sort contacts")
        print("8. Show contacts by pages")
        print("9. Import contacts from CSV")
        print("10. Import contacts from JSON")
        print("11. Export contacts to JSON")
        print("12. Export contacts to CSV")
        print("0. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_contacts()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            add_contact()
        elif choice == "4":
            add_extra_phone()
        elif choice == "5":
            move_contact()
        elif choice == "6":
            filter_by_group()
        elif choice == "7":
            sort_contacts()
        elif choice == "8":
            show_page()
        elif choice == "9":
            import_csv()
        elif choice == "10":
            import_json()
        elif choice == "11":
            export_json()
        elif choice == "12":
            export_csv()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
