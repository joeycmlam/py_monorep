-- Table: mydb.t1

DROP TABLE IF EXISTS mydb.t1;

CREATE TABLE IF NOT EXISTS mydb.t1
(
    fnd_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    fnd_ver varchar(5) not null,
    nav_price numeric(20,6) NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS mydb.t1
    OWNER to dbadmin;


insert into mydb.t1 (fnd_id, fnd_ver, nav_price) values ('010', '01', 11);
insert into mydb.t1 (fnd_id, fnd_ver, nav_price) values ('020', '01', 12);
insert into mydb.t1 (fnd_id, fnd_ver, nav_price) values ('030', '01', 13);
insert into mydb.t1 (fnd_id, fnd_ver, nav_price) values ('040', '01', 14);
insert into mydb.t1 (fnd_id, fnd_ver, nav_price) values ('050', '01', 15);
insert into mydb.t1 (fnd_id, fnd_ver, nav_price) values ('060', '01', 15);