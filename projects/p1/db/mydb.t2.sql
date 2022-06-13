-- Table: mydb.t1

DROP TABLE IF EXISTS mydb.t2;

CREATE TABLE IF NOT EXISTS mydb.t2
(
    fnd_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    fnd_ver varchar(5) not null,
    nav_price numeric(20,6) NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS mydb.t2
    OWNER to dbadmin;


insert into mydb.t2 (fnd_id, fnd_ver, nav_price) values ('010', '01', 11);
insert into mydb.t2 (fnd_id, fnd_ver, nav_price) values ('020', '01', 12.5);
insert into mydb.t2 (fnd_id, fnd_ver, nav_price) values ('030', '01', 13);
insert into mydb.t2 (fnd_id, fnd_ver, nav_price) values ('060', '01', 14);
insert into mydb.t2 (fnd_id, fnd_ver, nav_price) values ('070', '01', 15);
