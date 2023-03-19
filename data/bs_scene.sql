create table scene
(
    id      int auto_increment
        primary key,
    title   varchar(1000) not null,
    img_url varchar(100)  not null,
    browse  int           not null,
    time    varchar(50)   not null
);

INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (1, '图书馆自习室学习', 'http://www.cqie.edu.cn/upfiles/202207/20220701093535960.jpg', 24484, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (2, '图书馆学习', 'http://www.cqie.edu.cn/upfiles/202207/20220701093508516.jpg', 24390, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (3, '图书馆二部', 'http://www.cqie.edu.cn/upfiles/202207/20220701092332853.jpg', 23750, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (4, '图书馆', 'http://www.cqie.edu.cn/upfiles/202207/20220701092242910.jpg', 23693, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (5, '第四教学楼', 'http://www.cqie.edu.cn/upfiles/202204/20220405075036497.jpg', 25148, '2022/4/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (6, '行政楼', 'http://www.cqie.edu.cn/upfiles/202204/20220405075739997.jpg', 25732, '2022/4/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (7, '俯瞰第五教学楼', 'http://www.cqie.edu.cn/upfiles/202207/20220701091832819.jpg', 23632, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (8, '第五教学楼', 'http://www.cqie.edu.cn/upfiles/202101/20210110134628795.jpg', 27219, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (9, '第七教学楼', 'http://www.cqie.edu.cn/upfiles/202208/20220822105756776.jpg', 19646, '2022/8/22');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (10, '第六教学楼', 'http://www.cqie.edu.cn/upfiles/202206/20220602062625415.jpg', 27137, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (11, '校园俯瞰（双桥校区）', 'http://www.cqie.edu.cn/upfiles/202101/20210110134554884.jpg', 29538, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (12, '教学综合楼（双桥校区）', 'http://www.cqie.edu.cn/upfiles/202101/20210110134759427.jpg', 28330, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (13, '校内风光（双桥校区）', 'http://www.cqie.edu.cn/upfiles/202101/20210110134732494.jpg', 28805, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (14, '中华文化动漫研发传播中心', 'http://www.cqie.edu.cn/upfiles/202206/20220602063233602.jpg', 24940, '2022/6/2');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (15, '学术报告厅', 'http://www.cqie.edu.cn/upfiles/202204/20220405080516559.jpg', 26616, '2022/4/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (16, '校园俯瞰', 'http://www.cqie.edu.cn/upfiles/202207/20220701085715448.jpg', 33438, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (17, '学校正门', 'http://www.cqie.edu.cn/upfiles/202101/20210110134146446.jpg', 33017, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (18, '鸟瞰校园', 'http://www.cqie.edu.cn/upfiles/202209/20220905150200272.jpg', 18975, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (19, '香樟大道', 'http://www.cqie.edu.cn/upfiles/202209/20220905150453457.jpg', 17893, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (20, '智慧课堂', 'http://www.cqie.edu.cn/upfiles/202207/20220701092428327.jpg', 23876, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (21, '党员学习中心', 'http://www.cqie.edu.cn/upfiles/202207/20220701093223655.jpg', 23430, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (22, '奋进雕塑', 'http://www.cqie.edu.cn/upfiles/202204/20220405075329278.jpg', 3663, '2022/4/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (23, '孔子雕塑', 'http://www.cqie.edu.cn/upfiles/202204/20220405075421732.jpg', 3761, '2022/4/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (24, '老人葵林', 'http://www.cqie.edu.cn/upfiles/202204/20220405075522157.jpg', 3823, '2022/4/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (25, '竹筠亭', 'http://www.cqie.edu.cn/upfiles/202207/20220701093616549.jpg', 8721, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (26, '篮球场', 'http://www.cqie.edu.cn/upfiles/202207/20220701092137307.jpg', 1830, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (27, '做实验', 'http://www.cqie.edu.cn/upfiles/202207/20220701093638642.jpg', 8420, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (28, '交流实验心得', 'http://www.cqie.edu.cn/upfiles/202207/20220701093256768.jpg', 6095, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (29, '上实验课', 'http://www.cqie.edu.cn/upfiles/202207/20220701093407570.jpg', 8433, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (30, '重工创谷', 'http://www.cqie.edu.cn/upfiles/202303/20230316100535710.jpg', 5090, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (31, '物联网应用创新中心', 'http://www.cqie.edu.cn/upfiles/202101/20210110135150718.jpg', 4540, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (32, '学生社团活动', 'http://www.cqie.edu.cn/upfiles/202101/20210110135904822.jpg', 3969, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (33, '学生党员活动中心', 'http://www.cqie.edu.cn/upfiles/202101/20210110135835694.jpg', 3961, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (34, '学校后门', 'http://www.cqie.edu.cn/upfiles/202101/20210110135807538.jpg', 5679, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (35, '宿舍内景', 'http://www.cqie.edu.cn/upfiles/202101/20210110135737196.jpg', 7871, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (36, '学生公寓（双桥校区）', 'http://www.cqie.edu.cn/upfiles/202101/20210110135709784.jpg', 3386, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (37, '食堂内景（双桥校区）', 'http://www.cqie.edu.cn/upfiles/202101/20210110135638786.jpg', 3991, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (38, '食堂内景', 'http://www.cqie.edu.cn/upfiles/202101/20210110135610288.jpg', 4014, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (39, '百谷园食堂', 'http://www.cqie.edu.cn/upfiles/202101/20210110135545999.jpg', 3251, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (40, '运动场（双桥校区）', 'http://www.cqie.edu.cn/upfiles/202101/20210110135521272.jpg', 2962, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (41, '国旗护卫队', 'http://www.cqie.edu.cn/upfiles/202101/20210110135453916.jpg', 2875, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (42, '学校操场', 'http://www.cqie.edu.cn/upfiles/202101/20210110135419274.jpg', 3326, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (43, '图书馆自习室', 'http://www.cqie.edu.cn/upfiles/202101/20210110135352797.jpg', 4197, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (44, '彭氏民居', 'http://www.cqie.edu.cn/upfiles/202101/20210110135227263.jpg', 4274, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (45, '彭氏民居', 'http://www.cqie.edu.cn/upfiles/202101/20210110135300821.jpg', 4036, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (46, '学生开展素质拓展活动', 'http://www.cqie.edu.cn/upfiles/202101/20210110140015102.jpg', 4645, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (47, '学生开展素质拓展活动', 'http://www.cqie.edu.cn/upfiles/202101/20210110135933848.jpg', 3763, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (48, '电工技术实验室', 'http://www.cqie.edu.cn/upfiles/201802/20180226143349512.jpg', 4407, '2018/2/26');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (49, '电子技术实验台', 'http://www.cqie.edu.cn/upfiles/201802/20180226143412468.jpg', 3935, '2018/2/26');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (50, '电子科技实验室', 'http://www.cqie.edu.cn/upfiles/201802/20180226143433534.jpg', 4329, '2018/2/26');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (51, '数字媒体技术专业游戏开发实验..', 'http://www.cqie.edu.cn/upfiles/202101/20210110135116890.jpg', 5035, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (52, '土木建筑装饰材料实验室', 'http://www.cqie.edu.cn/upfiles/202101/20210110135049957.jpg', 4439, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (53, '苹果iOS系统实验室', 'http://www.cqie.edu.cn/upfiles/202101/20210110135025100.jpg', 4917, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (54, '计算机组成原理实验室', 'http://www.cqie.edu.cn/upfiles/202101/20210110134953630.jpg', 4554, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (55, '大数据与人工智能研究所', 'http://www.cqie.edu.cn/upfiles/202209/20220907100937141.jpg', 1589, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (56, '工业机器人系统集成与应用实验..', 'http://www.cqie.edu.cn/upfiles/202209/20220907101011891.jpg', 1545, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (57, '工业自动化与过程控制实验室', 'http://www.cqie.edu.cn/upfiles/202209/20220907101035597.jpg', 1548, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (58, '环境设计与施工虚拟仿真实验室..', 'http://www.cqie.edu.cn/upfiles/202209/20220907101103357.jpg', 1564, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (59, '建筑结构虚拟仿真实验室', 'http://www.cqie.edu.cn/upfiles/202209/20220907101126755.jpg', 1598, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (60, '企业经营管理综合实验室', 'http://www.cqie.edu.cn/upfiles/202209/20220907101149138.jpg', 1522, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (61, '商务数据分析与应用实验室', 'http://www.cqie.edu.cn/upfiles/202209/20220907101211276.jpg', 5555, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (62, '统计学实验室', 'http://www.cqie.edu.cn/upfiles/202209/20220907101233532.jpg', 18598, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (63, '土木工程施工与装配式虚拟仿真..', 'http://www.cqie.edu.cn/upfiles/202209/20220907101305873.jpg', 18800, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (64, '新媒体内容设计实验室', 'http://www.cqie.edu.cn/upfiles/202209/20220907101327371.jpg', 18794, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (65, '营销管理实验室', 'http://www.cqie.edu.cn/upfiles/202209/20220907101350136.jpg', 18686, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (66, '智能家居实验室', 'http://www.cqie.edu.cn/upfiles/202209/20220907101410219.jpg', 19472, '2022/9/7');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (67, '林荫道路', 'http://www.cqie.edu.cn/upfiles/202101/20210110134826630.jpg', 5342, '2021/1/10');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (68, '课堂交流', 'http://www.cqie.edu.cn/upfiles/202207/20220701093325982.jpg', 7896, '2022/7/1');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (69, '彭氏民居一角', 'http://www.cqie.edu.cn/upfiles/202209/20220905150647433.jpg', 2010, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (70, '月光下的彭氏民居', 'http://www.cqie.edu.cn/upfiles/202209/20220905150526729.jpg', 1962, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (71, '百谷园食堂', 'http://www.cqie.edu.cn/upfiles/202209/20220905150941594.jpg', 2078, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (72, '课后运动', 'http://www.cqie.edu.cn/upfiles/202209/20220905150227488.jpg', 2014, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (73, '双桥校区教学楼一角', 'http://www.cqie.edu.cn/upfiles/202209/20220905150723954.jpg', 2141, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (74, '六教教室一角', 'http://www.cqie.edu.cn/upfiles/202209/20220905145838928.jpg', 1951, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (75, '六教前广场环道', 'http://www.cqie.edu.cn/upfiles/202209/20220905150126710.jpg', 1891, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (76, '雨后的七教', 'http://www.cqie.edu.cn/upfiles/202209/20220905145708924.jpg', 1934, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (77, '第四教学楼一角', 'http://www.cqie.edu.cn/upfiles/202209/20220905150306448.jpg', 1928, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (78, '夕阳下的校园', 'http://www.cqie.edu.cn/upfiles/202209/20220905150424470.jpeg', 2084, '2022/9/5');
INSERT INTO bs.scene (id, title, img_url, browse, time)
VALUES (79, '校园的早晨', 'http://www.cqie.edu.cn/upfiles/202209/20220905150345888.jpg', 2086, '2022/9/5');
