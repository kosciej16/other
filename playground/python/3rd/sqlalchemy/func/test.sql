CREATE OR REPLACE FUNCTION test()
RETURNS SETOF record AS $$
DECLARE 
  ret RECORD;
BEGIN
    return next (1, 3, 6);
    select 1, 3, 6 into ret;
    return next ret;
    select 2, 1, 2 into ret;
    return next ret;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER VOLATILE PARALLEL UNSAFE;

/* CREATE OR REPLACE FUNCTION sf_internal.compare_directories( */
/*     src_cur refcursor, */
/*     dst_cur refcursor) */
/* RETURNS record AS $$ */
/* DECLARE */
/*     files_cur refcursor; */
/*     stats_cur refcursor; */
/*     res record; */
/*     src_row RECORD; */
/*     dst_row RECORD; */
/*     status TEXT; */
/* BEGIN */
/*     CREATE TEMPORARY TABLE _compare_directories( */
/*         status TEXT NOT NULL, */
/*         parent TEXT, */
/*         src_fn TEXT, */
/*         dst_fn TEXT, */
/*         src_size INT, */
/*         dst_size INT, */
/*         username TEXT, */
/*         mtime TIMESTAMP */
/*     ); */

/*     FETCH src_cur INTO src_row; */
/*     FETCH dst_cur INTO dst_row; */
/*     WHILE NOT src_row IS NULL OR NOT dst_row IS NULL LOOP */
/*         IF src_row IS NULL OR src_row.fn > dst_row.fn OR src_row.fn = dst_row.fn AND src_row.parent_path > dst_row.parent_path THEN */
/*             INSERT INTO _compare_directories VALUES ('new', dst_row.parent_path, null, dst_row.fn, null, dst_row.size, dst_row.username, dst_row.mt); */
/*             FETCH dst_cur INTO dst_row; */
/*         ELSIF dst_row IS NULL OR src_row.fn < dst_row.fn OR src_row.fn = dst_row.fn AND src_row.parent_path < dst_row.parent_path THEN */
/*             INSERT INTO _compare_directories VALUES ('removed', src_row.parent_path, src_row.fn, null, src_row.size, null, src_row.username, src_row.mt); */
/*             FETCH src_cur INTO src_row; */
/*         ELSE */
/*             IF src_row.size = dst_row.size AND src_row.mt = dst_row.mt THEN */
/*                 status = 'no_change'; */
/*             ELSE */
/*                 status = 'changed'; */
/*             END IF; */
/*             INSERT INTO _compare_directories VALUES (status, src_row.parent_path, src_row.fn, dst_row.fn, src_row.size, dst_row.size, src_row.username, src_row.mt); */
/*             FETCH dst_cur INTO dst_row; */
/*             FETCH src_cur INTO src_row; */
/*         END IF; */
/*     END LOOP; */
/*     OPEN files_cur FOR SELECT * FROM _compare_directories; */
/*     OPEN stats_cur FOR SELECT c.status, parent, count(*) FROM _compare_directories c GROUP BY parent, c.status; */
/*     SELECT files_cur, stats_cur into res; */
/*     return res; */
/* END; */
/* $$ LANGUAGE plpgsql SECURITY DEFINER VOLATILE PARALLEL UNSAFE; */

