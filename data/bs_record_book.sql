create table record_book
(
    id      int auto_increment
        primary key,
    user_id int       not null,
    book_id int       not null,
    time    timestamp null
);

INSERT INTO bs.record_book (id, user_id, book_id, time)
VALUES (1, 1, 278434, '2023-03-14 00:00:00');
INSERT INTO bs.record_book (id, user_id, book_id, time)
VALUES (2, 1, 257165, '2023-03-14 00:00:00');
INSERT INTO bs.record_book (id, user_id, book_id, time)
VALUES (3, 1, 263108, '2023-03-14 00:00:00');
INSERT INTO bs.record_book (id, user_id, book_id, time)
VALUES (4, 1, 256176, '2023-03-14 00:00:00');
INSERT INTO bs.record_book (id, user_id, book_id, time)
VALUES (5, 1, 270802, '2023-03-14 00:00:00');
INSERT INTO bs.record_book (id, user_id, book_id, time)
VALUES (6, 1, 260993, '2023-03-14 00:00:00');
INSERT INTO bs.record_book (id, user_id, book_id, time)
VALUES (7, 1, 275293, '2023-03-14 00:00:00');
INSERT INTO bs.record_book (id, user_id, book_id, time)
VALUES (8, 1, 258883, '2023-03-14 00:00:00');
