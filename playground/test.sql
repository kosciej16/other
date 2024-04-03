CREATE OR REPLACE FUNCTION sf_internal.compare_directories(
    src_cur refcursor,
    dst_cur refcursor)
RETURNS refcursor AS $$
DECLARE
    result_cur refcursor;
    src_row RECORD;
    dst_row RECORD;
    status TEXT;
BEGIN
    -- Be carefull, that table is used and removed later in code
    DROP TABLE IF EXISTS _compare_entries;
    CREATE TABLE _compare_entries(
        status TEXT NOT NULL,
        parent TEXT,
        src_fn TEXT,
        dst_fn TEXT,
        src_size BIGINT,
        dst_size BIGINT,
        username TEXT,
        mtime TIMESTAMP
    );

    FETCH src_cur INTO src_row;
    FETCH dst_cur INTO dst_row;
    WHILE NOT src_row IS NULL OR NOT dst_row IS NULL LOOP
        IF src_row IS NULL OR src_row.fn > dst_row.fn OR src_row.fn = dst_row.fn AND src_row.parent_path > dst_row.parent_path THEN
            INSERT INTO _compare_entries VALUES ('new', dst_row.parent_path, null, dst_row.fn, null, dst_row.size, dst_row.username, dst_row.mt);
            FETCH dst_cur INTO dst_row;
        ELSIF dst_row IS NULL OR src_row.fn < dst_row.fn OR src_row.fn = dst_row.fn AND src_row.parent_path < dst_row.parent_path THEN
            INSERT INTO _compare_entries VALUES ('removed', src_row.parent_path, src_row.fn, null, src_row.size, null, src_row.username, src_row.mt);
            FETCH src_cur INTO src_row;
        ELSE
            IF src_row.size = dst_row.size THEN
                status = 'no_change';
            ELSE
                status = 'changed';
            END IF;
            INSERT INTO _compare_entries VALUES (status, src_row.parent_path, src_row.fn, dst_row.fn, src_row.size, dst_row.size, src_row.username, src_row.mt);
            FETCH dst_cur INTO dst_row;
            FETCH src_cur INTO src_row;
        END IF;
    END LOOP;
    OPEN result_cur FOR SELECT * FROM _compare_entries;
    RETURN result_cur;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER VOLATILE PARALLEL UNSAFE;
