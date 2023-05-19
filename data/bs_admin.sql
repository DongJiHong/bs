create table admin
(
    id       int auto_increment
        primary key,
    username varchar(50)          not null,
    password varchar(255)         not null,
    grade    tinyint(1) default 0 null
);

INSERT INTO bs.admin (id, username, password, grade)
VALUES (1, 'admin',
        'pbkdf2:sha256:260000$5Mc4pKLpWbIwd65t$5214ea817d3c0d0ee4e0c69ad56b50175436f3d2e745bc13ca98f83b0ae25b4a', 1);
INSERT INTO bs.admin (id, username, password, grade)
VALUES (2, 'root',
        'pbkdf2:sha256:260000$MaHfF6MqQwlWDW5y$dfb92d660ce94270080ba4c8d797ceed28b0dbc47f7fef9cb077f271c5c7d448', 1);
INSERT INTO bs.admin (id, username, password, grade)
VALUES (3, 'testadmin',
        'pbkdf2:sha256:260000$MKFgN307BrgZ7Nb8$fed1d2846183ee67d89b09e9760c5476a85227e5eb57caea46e49de21e9d6888', 0);
INSERT INTO bs.admin (id, username, password, grade)
VALUES (5, 'testadmin1',
        'pbkdf2:sha256:260000$sVfa6YBvl7ZOiKrU$7bc9452a29f9e078436c189f5cd0d00d7cff83ee6e5176ccd523c6e8462b6d9a', 0);
INSERT INTO bs.admin (id, username, password, grade)
VALUES (6, 'testadmin33',
        'pbkdf2:sha256:260000$WPTH4NSPbv7FDBQ1$4f383e285782052812a1330592cc46fbc126f34cb859ad3fc20dc25e635e9392', 0);
