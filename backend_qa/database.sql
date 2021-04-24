DROP TABLE IF EXISTS qa_user;

CREATE TABLE IF NOT EXISTS qa_user (
 user_id INT(11) NOT NULL AUTO_INCREMENT,
 username VARCHAR(20) NOT NULL UNIQUE,
 password VARCHAR(20) NOT NULL,
 PRIMARY KEY (user_id)
);

INSERT INTO qa_user (username, password) VALUES ('user', 'abcdef123456');