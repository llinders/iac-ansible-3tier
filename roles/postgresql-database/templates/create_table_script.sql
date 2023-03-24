create table Customer (
    id                  serial          not null,
    customer_number     int             unique not null,
    username            varchar(255)    unique not null,
    constraint pk_customer primary key(id)
);

create table Task (
    id                  serial      not null,
    customer_number     int,
    task                varchar     not null,
    constraint pk_todo primary key(id),
    constraint fk_customer foreign key(customer_number) references Customer(customer_number)
);