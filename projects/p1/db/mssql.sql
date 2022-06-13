create table t2 (
    fnd_id varchar(10) not null,
    fnd_ver varchar(5) not null,
    nav_price numeric(20, 6) not null
);



insert into t2 (fnd_id, fnd_ver, nav_price) values ('010', '01', 11);
insert into t2 (fnd_id, fnd_ver, nav_price) values ('020', '01', 12.5);
insert into t2 (fnd_id, fnd_ver, nav_price) values ('030', '01', 13);
insert into t2 (fnd_id, fnd_ver, nav_price) values ('060', '01', 14);
insert into t2 (fnd_id, fnd_ver, nav_price) values ('070', '01', 15);