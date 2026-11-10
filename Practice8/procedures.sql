CREATE OR REPLACE PROCEDURE add_or_update_user(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phonebook (name, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (name)
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$;


CREATE OR REPLACE PROCEDURE add_users_batch(
    p_names VARCHAR[],
    p_phones VARCHAR[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
BEGIN
    IF cardinality(p_names) <> cardinality(p_phones) THEN
        RAISE EXCEPTION 'Names and phones must have the same length';
    END IF;

    FOR i IN 1..COALESCE(array_length(p_names, 1), 0)
    LOOP
        IF p_names[i] IS NULL OR TRIM(p_names[i]) = '' THEN
            RAISE NOTICE 'Invalid name at position %', i;
        ELSIF p_phones[i] IS NULL OR p_phones[i] !~ '^\+?[0-9]{10,15}$' THEN
            RAISE NOTICE 'Invalid phone for %: %', p_names[i], p_phones[i];
        ELSE
            INSERT INTO phonebook (name, phone)
            VALUES (p_names[i], p_phones[i])
            ON CONFLICT (name)
            DO UPDATE SET phone = EXCLUDED.phone;

            RAISE NOTICE 'Contact processed: %', p_names[i];
        END IF;
    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_phonebook_contact(
    p_search VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_search OR phone = p_search;

    IF NOT FOUND THEN
        RAISE NOTICE 'Contact not found: %', p_search;
    ELSE
        RAISE NOTICE 'Contact deleted successfully';
    END IF;
END;
$$;