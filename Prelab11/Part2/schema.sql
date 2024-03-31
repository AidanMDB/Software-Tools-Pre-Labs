CREATE TABLE users (
    name text,
    age int
);

CREATE TABLE posts (
    contents text,
    title text,
    user_name text
);

CREATE TRIGGER aft_dlt AFTER DELETE ON users
BEGIN
    DELETE FROM posts WHERE posts.user_name == OLD.name;
END;

INSERT INTO users (name, age) VALUES
    ('aidan', 20),
    ('bob', 34),
    ('god', 100000),
    ('emma', 25),
    ('lando', 40);

INSERT INTO posts (contents, title, user_name) VALUES
    ('This is my first posts', 'FIRST', 'aidan'),
    ('I love my job', 'JOB', 'bob'),
    ('ALL HAIL', 'Scipture', 'god'),
    ('lulu lemon', 'Favorite Store', 'emma'),
    ('I own the millenium falcon', 'Star Wars', 'lando');


