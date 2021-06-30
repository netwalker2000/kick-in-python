-- product database
create database product_db;
create table product_tab (
  id bigint(20) not null auto_increment comment 'pk',
  name varchar(200) not null default '' comment 'name',
  category varchar(10) not null default '' comment 'category',
  description varchar(2000) not null default '' comment 'description',
  status tinyint default 0 comment '0-enable，1-disable，default 0',
  created_at bigint(20) not null default 0 comment 'create_at',
  updated_at bigint(20) not null default 0 comment 'update_at',
  db_update_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  primary key (id),
  key idx_updated_at(updated_at),
  key idx_name(name, updated_at),
  key idx_category(category, updated_at)
) engine=InnoDB  default charset=utf8mb4 comment 'product info'
-- todo: meet Shopee's standard category system. how to support multi-category of a product

create table photo_tab (
  id bigint(20) not null auto_increment comment 'pk',
  type tinyint default 0 comment '0-shopee photo infra，1-sea photo infra, default 0',
  url varchar(2000) not null default '' comment 'url',
  product_id bigint(20) not null comment 'reference of id column of product table',
  created_at bigint(20) not null default 0 comment 'create_at',
  updated_at bigint(20) not null default 0 comment 'update_at',
  db_update_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  primary key (id),
  key idx_product(product_id)
) engine=InnoDB  default charset=utf8mb4 comment 'photo'
-- photo cloud infra which store photos, and can access photo by url, stored in shorten way

-- comment database
create database comment_db;
create table comment_tab (
  id bigint(20) not null auto_increment comment 'pk',
  content varchar(2000) not null default '' comment 'content',
  status tinyint default 0 comment '0-normal，1-deleted，default 0',
  topic_id bigint(20) not null comment 'reference of id column of product table',
  user_id bigint(20) not null comment 'reference of id column of user table',
  user_name varchar(200) not null default '' comment 'name',
  to_id bigint(20) comment 'reply to which comment',
  created_at bigint(20) not null default 0 comment 'create_at',
  updated_at bigint(20) not null default 0 comment 'update_at',
  db_update_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  primary key (id),
  key idx_topic(topic_id),
  key idx_user(user_id)
) engine=InnoDB  default charset=utf8mb4 comment 'comment'