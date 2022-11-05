/*
 Create table statement.
 */
create table columbia_student
(
    auto_id     int auto_increment
        primary key,
    last_name   varchar(128) not null,
    first_name  varchar(128) not null,
    middle_name varchar(128) null,
    email       varchar(256) not null,
    uni         varchar(12)  not null,
    constraint columbia_student_email_uindex
        unique (email),
    constraint columbia_student_uni_uindex
        unique (uni)
);

/*
 Example insert statement. Note that since auto_id is auto-increment, the insert
 statement does not need to specify it.
 */
 insert into columbia_student (last_name, first_name, middle_name, email, uni)
    values ("Ferguson", "Donald", "Francis", "dff@cs.columbia.edu", "dff9");

