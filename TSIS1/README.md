# TSIS 1 - PhoneBook

## Requirements
- Python 3
- PostgreSQL
- psycopg2-binary

## Installation

1. Install dependencies:

   pip install -r requirements.txt

2. Copy config.example.py to config.py.

3. Open config.py and enter your PostgreSQL password.

4. Create the database phonebook_db.

5. Run schema.sql in PostgreSQL.

6. Run procedures.sql in PostgreSQL.

7. Start the application:

   python phonebook.py

## Features

- Display contacts
- Search contacts by name, email or phone
- Add and update contacts
- Add multiple phone numbers
- Move contacts between groups
- Filter contacts by group
- Sort contacts
- Pagination
- CSV import and export
- JSON import and export
