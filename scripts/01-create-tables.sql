create table tipo_produto(
    id NUMBER PRIMARY KEY,
    nome VARCHAR2(50) not null
);

create table produto(
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_tipo number not null,
    nome VARCHAR2(50) not null,
    CONSTRAINT fk_id_tipo_produto FOREIGN KEY (id_tipo)
    REFERENCES tipo_produto(id)
);

create table registro_produto(
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_produto number,
    estoque numeric(15,3) not null,
    data date not null,
    CONSTRAINT fk_id_produto FOREIGN KEY (id_produto)
    REFERENCES produto(id)
);
