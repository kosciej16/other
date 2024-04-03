CREATE OR REPLACE FUNCTION pair_array_elements(arr INTEGER[])
RETURNS SETOF VARCHAR AS $$
DECLARE
  i INTEGER;
BEGIN
  FOR i IN 1..array_upper(arr, 1) - 1
  LOOP
    RETURN NEXT arr[i] || '-' || arr[i + 1];
  END LOOP;
END;
$$ LANGUAGE plpgsql;
