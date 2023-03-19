create table user
(
    id       int auto_increment
        primary key,
    username varchar(50)  not null,
    password varchar(255) not null,
    label    text         null
);

INSERT INTO bs.user (id, username, password, label)
VALUES (1, '1',
        'pbkdf2:sha256:260000$EfW8dAF9xLVDNwov$71a7967cadc81cf99530b7cebbcaf49eeb64418387300a3f19624d0d3ec91ee2',
        'ide,pycharm,python,童话,安装教程,科幻,悬疑,javascript,java,爱情,轻小说,编程,文学,前端,html,互联网,安装配置教程');
