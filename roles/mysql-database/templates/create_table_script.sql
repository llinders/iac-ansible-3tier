CREATE TABLE IF NOT EXISTS Task (
    id      int         	NOT NULL AUTO_INCREMENT,
    task    varchar(255)    NOT NULL,
    CONSTRAINT pk_task PRIMARY KEY (id)
);