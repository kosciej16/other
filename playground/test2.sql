CREATE OR REPLACE FUNCTION test()
/* returns SETOF record */
returns refcursor
AS $$
DECLARE
    cur cursor for SELECT * from sf.file_current limit 5;
    res refcursor;
    row record;
BEGIN
    CREATE TEMPORARY TABLE moja_tabelka (s1 sf.off_t, s2 sf.off_t);
    open cur;
    FETCH cur INTO row;
    WHILE not row IS NULL LOOP
        FETCH cur INTO row;
        insert into moja_tabelka values(row.size, row.size);
        /* return next (row.size::bigint, row.size::bigint); */
        /* return next (row.size, row.size); */

    END LOOP;

    OPEN res FOR SELECT * FROM moja_tabelka;
    RETURN res;
END;

$$ LANGUAGE plpgsql;
