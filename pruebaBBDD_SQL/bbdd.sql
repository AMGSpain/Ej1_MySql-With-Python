CREATE DATABASE IF NOT EXISTS julioPython;
use julioPython;

CREATE TABLE usuarios(
    id  int(25) auto_increment not null,
    nombre varchar(100),
    apellidos varchar(255),
    email varchar(255) not null,
    password varchar(255) not null,
    fecha date not null,
    CONSTRAINT primarikey_usuarios PRIMARY KEY(id),
    CONSTRAINT unique_email UNIQUE(email)
)ENGINE=InnoDB;

CREATE TABLE notas(
    id int(25) auto_increment not null,
    usuario_id int(25) not null,
    titulo varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha date not null,
    CONSTRAINT primarikey_notas PRIMARY KEY(id),
    CONSTRAINT foreignkey_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDB;