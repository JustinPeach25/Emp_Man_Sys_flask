create table admin(id integer AUTO_INCREMENT PRIMARY key, name text not null, password text not null, admin bool not null default 'O');

create table employees(empid integer AUTO_INCREMENT PRIMARY key, name text not null, surname text not null, DOB date, salary float not null, position text not null, line_manager text not null);
