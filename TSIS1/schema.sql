ALTER TABLE phonebook
ADD COLUMN IF NOT EXISTS email VARCHAR(150),
ADD COLUMN IF NOT EXISTS birthday DATE,
ADD COLUMN IF NOT EXISTS created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO groups (name)
VALUES
    ('Family'),
    ('Friends'),
    ('University'),
    ('Work')
ON CONFLICT (name) DO NOTHING;

ALTER TABLE phonebook
ADD COLUMN IF NOT EXISTS group_id INTEGER;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.table_constraints
        WHERE constraint_name = 'fk_phonebook_group'
          AND table_name = 'phonebook'
    ) THEN
        ALTER TABLE phonebook
        ADD CONSTRAINT fk_phonebook_group
        FOREIGN KEY (group_id)
        REFERENCES groups(id)
        ON DELETE SET NULL;
    END IF;
END $$;

CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER NOT NULL,
    phone VARCHAR(20) NOT NULL,
    type VARCHAR(30) DEFAULT 'mobile',
    CONSTRAINT fk_phones_contact
        FOREIGN KEY (contact_id)
        REFERENCES phonebook(id)
        ON DELETE CASCADE,
    CONSTRAINT unique_contact_phone
        UNIQUE (contact_id, phone)
);

INSERT INTO phones (contact_id, phone, type)
SELECT p.id, p.phone, 'mobile'
FROM phonebook p
WHERE NOT EXISTS (
    SELECT 1
    FROM phones ph
    WHERE ph.contact_id = p.id
      AND ph.phone = p.phone
);