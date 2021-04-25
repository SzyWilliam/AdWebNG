DROP TABLE IF EXISTS qa_user;

CREATE TABLE IF NOT EXISTS qa_user (
 user_id INT(11) NOT NULL AUTO_INCREMENT,
 email VARCHAR(20) NOT NULL UNIQUE,
 full_name VARCHAR(20) NOT NULL,
 password VARCHAR(20) NOT NULL,
 PRIMARY KEY (user_id)
);

INSERT INTO qa_user (email, full_name, password) VALUES ('user@qq.com', '张三', 'abcdef123456');