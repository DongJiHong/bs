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
        'html,python,安装教程,悬疑,文学,ide,编程,科幻,轻小说,哲学,pycharm,童话,安装配置教程,javascript,互联网,tomcat,servlet,爱情,前端,科学,java');
INSERT INTO bs.user (id, username, password, label)
VALUES (2, 'test222',
        'pbkdf2:sha256:260000$0bj6OCUsJiWhnUWd$5f03cccde8cbf6dec24765656d05357baed13044246107848d5efae2cdd16597',
        '名著,java面试,网络小说,ide,童话,爱情,科学,安装配置教程,java,python,mysql,数据库,面试,文学,java面试总结,安装教程,pycharm');
INSERT INTO bs.user (id, username, password, label)
VALUES (3, 'test333',
        'pbkdf2:sha256:260000$hRcg8A0aeoJHUoFC$f3af20c198172c75e0dfe7b9ba19656e15f7261094303e429130d9e086276e00',
        'Java,Python,文学');
