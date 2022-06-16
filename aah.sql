CREATE DATABASE IF NOT EXISTS aah_python;
USE aah_python;
CREATE TABLE usuarios2(
id int(25) auto_increment not null,
nombre varchar(100),
apellidos varchar(255),
email varchar(255) not null,
password varchar(255) not null,
rol varchar(255) not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id)
CONSTRAINT uq_email UNIQUE(email)

)ENDINE=InnoDb;

CREATE TABLE citas(
id int(25) auto_increment not null,
doctor varchar(255) not null,
consultorio varchar(255) not null,
turno varchar(255) not null,
CONSTRAINT pk_notas PRIMARY KEY(id)
)ENDINE=InnoDb;

CREATE TABLE consultorio(
id int(25) auto_increment not null,
nombre varchar(255) not null,
estado varchar(255) not null,
ubicacion varchar(255) not null,
CONSTRAINT pk_consultorio PRIMARY KEY(id)
)ENDINE=InnoDb;