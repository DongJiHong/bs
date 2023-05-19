create table questionnaire
(
    id  int auto_increment
        primary key,
    d_1 tinyint(1) default 1 null,
    d_2 tinyint(1) default 1 null,
    d_3 tinyint(1) default 1 null,
    d_4 tinyint(1) default 1 null,
    d_5 text                 null
);

INSERT INTO bs.questionnaire (id, d_1, d_2, d_3, d_4, d_5)
VALUES (1, 1, 1, 1, 1, '1');
INSERT INTO bs.questionnaire (id, d_1, d_2, d_3, d_4, d_5)
VALUES (2, null, null, null, null, '');
