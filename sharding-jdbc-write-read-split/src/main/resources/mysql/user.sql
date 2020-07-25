CREATE TABLE `user` (
  `id` varchar(36) NOT NULL,
  `user_name` varchar(12) DEFAULT NULL,
  `age` tinyint(3) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4