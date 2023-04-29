CREATE TABLE users (
    user_id number identity primary key,
    user_password varchar(15),
    user_name varchar (20),
    is_active bit,
    phone_number bigint,
    email varchar(20),
)

CREATE TABLE chats (
    chat_id number identity primary key,
    chat_users varchar(100),
    chat_content_location varchar(100)
)

CREATE TABLE posts (
    post_id number identity primary key,
    post_content varchar(200),
    post_creator number foreign key references users.user_id,
    post_chat number foreign key references chats.chat_id,
)