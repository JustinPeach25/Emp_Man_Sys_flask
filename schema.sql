create table users(id integer PRIMARY KEY AUTO_INCREMENT, name text not null, password text not null, admin bool not null default 'O');

create table employees(empid integer PRIMARY KEY AUTO_INCREMENT, name text not null, email text not null, phone text not null, address text not null);
