DECLARE
    v_id_produto NUMBER;
    v_estoque NUMBER;
    v_data DATE;
BEGIN
    FOR i IN 1..10000 LOOP
            SELECT FLOOR(DBMS_RANDOM.VALUE(1, (SELECT COUNT(*) FROM produto) + 1))
            INTO v_id_produto
            FROM dual;

            v_estoque := ROUND(DBMS_RANDOM.VALUE(-1000, 1000), 3);
            v_data := TRUNC(SYSDATE - DBMS_RANDOM.VALUE(0, 365));

            INSERT INTO registro_produto (id_produto, estoque, data)
            VALUES (v_id_produto, v_estoque, v_data);
        END LOOP;
    COMMIT; 
END;
/