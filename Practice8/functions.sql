CREATE OR REPLACE FUNCTION search_phonebook(search_text VARCHAR)
RETURNS TABLE (
    id INTEGER,
    name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    WHERE p.name ILIKE '%' || search_text || '%'
       OR p.phone ILIKE '%' || search_text || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_phonebook_page(
    page_number INTEGER,
    page_size INTEGER
)
RETURNS TABLE (
    id INTEGER,
    name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    IF page_number < 1 OR page_size < 1 THEN
        RAISE EXCEPTION 'Page number and page size must be positive';
    END IF;

    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT page_size
    OFFSET (page_number - 1) * page_size;
END;
$$ LANGUAGE plpgsql;