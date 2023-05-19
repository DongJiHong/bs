create table feedback
(
    id       int auto_increment
        primary key,
    user_id  int          not null,
    score    int          not null,
    feedback varchar(100) null
);

INSERT INTO bs.feedback (id, user_id, score, feedback)
VALUES (1, 1, 9, '不错');
INSERT INTO bs.feedback (id, user_id, score, feedback)
VALUES (3, 1, 9, '不错');
INSERT INTO bs.feedback (id, user_id, score, feedback)
VALUES (4, 1, 9, '不错');
