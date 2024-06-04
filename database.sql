CREATE DATABASE IF NOT EXISTS proyectoPython;
use proyectoPython;

CREATE TABLE usuarios(
    id int(25) auto_increment not null,
    nombre      varchar(30),
    apellido    varchar(30),
    email       varchar(60) not null,
    password    varchar(40) not null,
    fecha       date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uk_email UNIQUE(email)
)ENGINE = InnoDb;

CREATE TABLE notas(
    id          int(25)auto_increment not null,
    usuario_id  int(25) not null,
    titulo      varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha       date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_notas_usuario FOREING KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE = InnoDb;