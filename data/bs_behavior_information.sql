create table behavior_information
(
    id             int auto_increment
        primary key,
    user_id        int           not null,
    information_id int           not null,
    behavior       int default 0 null comment '0踩 1点赞'
);

INSERT INTO bs.behavior_information (id, user_id, information_id, behavior)
VALUES (1, 1, 10382, 0);
