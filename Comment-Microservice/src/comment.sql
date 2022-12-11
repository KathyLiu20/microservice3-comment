-- auto-generated definition
create table comment
(
    comment_id varchar(225) not null
        primary key,
    user_id    varchar(225) not null,
    post_id    varchar(225) not null,
    poster_id  varchar(225) not null,
    text       varchar(225) not null,
    date       datetime     not null,
    likes      int          not null,
    username   varchar(225) not null
);

