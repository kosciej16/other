/* EXPLAIN ANALYZE SELECT * from t1 join t2 on t1.field = t2.t1_field and t1.id = t2.t1_id */
/* EXPLAIN ANALYZE SELECT * from t1 join t2 on t1.id = t2.t1_id and t1.field = t2.t1_field */
EXPLAIN ANALYZE SELECT o.* from t1 o join t1 c on o.id = c.id join (
	    select
		distinct tmp.name as name,
		tmp.path as path
	    from
		tmp) as anon_1 on
	    o.name = anon_1.name and
	    c.path = anon_1.path
