
# Practice 8 — PhoneBook

## Description
This project is a PhoneBook application connected to PostgreSQL.
It allows users to manage contacts using Python and PL/pgSQL.

## Technologies
- Python 3.13
- PostgreSQL
- psycopg2
- python-dotenv

## Features
1. Show all contacts
2. Search contacts by name or phone
3. Add or update a contact
4. Add multiple contacts
5. Display contacts using pagination
6. Delete contacts

## Database
Database name: phonebook_db

Table: phonebook
- id — Primary Key
- name — Unique contact name
- phone — Contact phone number

## Installation

1. Clone the repository.
2. Open the Practice8 folder.
3. Create a virtual environment:

   python -m venv .venv

4. Activate the environment:

   .venv\Scripts\activate

5. Install dependencies:

   pip install -r requirements.txt

6. Create a .env file using .env.example.
7. Enter your PostgreSQL password in .env.

## Run

python phonebook.py

## SQL Files
- functions.sql — PostgreSQL functions
- procedures.sql — PostgreSQL procedures