
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_id INTEGER,
    p_phone VARCHAR,
    p_type VARCHAR DEFAULT 'mobile'
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM phonebook WHERE id = p_contact_id
    ) THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    IF p_phone !~ '^\+?[0-9]{10,15}$' THEN
        RAISE EXCEPTION 'Invalid phone number';
    END IF;

    INSERT INTO phones (contact_id, phone, type)
    VALUES (p_contact_id, p_phone, p_type)
    ON CONFLICT (contact_id, phone) DO NOTHING;
END;
$$;


CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_id INTEGER,
    p_group_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM phonebook WHERE id = p_contact_id
    ) THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM groups WHERE id = p_group_id
    ) THEN
        RAISE EXCEPTION 'Group not found';
    END IF;

    UPDATE phonebook
    SET group_id = p_group_id
    WHERE id = p_contact_id;
END;
$$;


CREATE OR REPLACE FUNCTION search_contacts(
    p_search VARCHAR DEFAULT ''
)
RETURNS TABLE (
    contact_id INTEGER,
    contact_name VARCHAR,
    contact_email VARCHAR,
    contact_birthday DATE,
    group_name VARCHAR,
    phone_numbers TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.id,
        p.name,
        p.email,
        p.birthday,
        g.name,
        COALESCE(
            STRING_AGG(ph.phone, ', '),
            p.phone
        )
    FROM phonebook p
    LEFT JOIN groups g ON p.group_id = g.id
    LEFT JOIN phones ph ON p.id = ph.contact_id
    WHERE p.name ILIKE '%' || p_search || '%'
       OR p.email ILIKE '%' || p_search || '%'
       OR p.phone ILIKE '%' || p_search || '%'
       OR ph.phone ILIKE '%' || p_search || '%'
    GROUP BY p.id, p.name, p.email, p.birthday, g.name
    ORDER BY p.id;
END;
$$;
