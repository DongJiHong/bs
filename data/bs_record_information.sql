create table record_information
(
    id             int auto_increment
        primary key,
    user_id        int       not null,
    information_id int       not null,
    time           timestamp null
);

INSERT INTO bs.record_information (id, user_id, information_id, time)
VALUES (1, 1, 10382, '2023-03-12 00:00:00');
INSERT INTO bs.record_information (id, user_id, information_id, time)
VALUES (2, 1, 94204, '2023-03-12 00:00:00');
INSERT INTO bs.record_information (id, user_id, information_id, time)
VALUES (3, 1, 10382, '2023-03-20 00:00:00');
INSERT INTO bs.record_information (id, user_id, information_id, time)
VALUES (4, 2, 10382, '2023-03-24 00:00:00');
INSERT INTO bs.record_information (id, user_id, information_id, time)
VALUES (5, 2, 146616, '2023-03-24 00:00:00');
INSERT INTO bs.record_information (id, user_id, information_id, time)
VALUES (6, 1, 94204, '2023-03-24 00:00:00');
INSERT INTO bs.record_information (id, user_id, information_id, time)
VALUES (7, 1, 146236, '2023-03-24 00:00:00');
