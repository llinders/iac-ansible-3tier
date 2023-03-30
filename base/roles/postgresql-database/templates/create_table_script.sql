create table if not exists Task (
    id                  serial      not null,
    task                varchar     not null,
    constraint pk_task primary key(id)
);

insert into Task (task) values ('test');