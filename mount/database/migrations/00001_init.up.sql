create table oauth_clients (
    id int not null auto_increment primary key,
    user_id int not null,
    name text not null,
    secret char(32) not null,
    status text not null default 'active',
    created_at timestamp not null default current_timestamp,
    updated_at timestamp not null default current_timestamp on update current_timestamp,
    deleted_at timestamp null
);

create table oauth_access_tokens (
    id int not null auto_increment primary key,
    user_id int not null,
    client_id int not null,
    token char(1000) not null,
    refresh_token char(1000) null,
    scopes json not null,
    status text not null default 'active',
    created_at timestamp not null default current_timestamp,
    updated_at timestamp not null default current_timestamp on update current_timestamp,
    expires_at timestamp not null,
    deleted_at null
);

create table users (
    id int not null auto_increment primary key,
    username varchar(32) not null,
    email text not null,
    country_acronym char(2) not null,
    bcrypt_password char(60) not null,
    privileges int not null default 3,
    default_mode text not null default 'osu',
    friend_only_dms tinyint(1) not null default 0,
    show_status tinyint(1) not null default 1,
    last_visit timestamp not null default current_timestamp,
    restricted_at timestamp null,
    supporter_until timestamp null,
    userpage_bbcode text null,
    status text not null default 'active',
    default_group int not null default 1,
    created_at timestamp not null default current_timestamp,
    updated_at timestamp not null default current_timestamp on update current_timestamp,
    deleted_at timestamp null
);

create table groups (
    id int not null auto_increment primary key,
    identifier text not null,
    name text not null,
    short_name text not null,
    description_markdown text null,
    playmodes json null,
    colour text null,
    leader_id int not null,
    unique (identifier)
);

create table user_groups (
    user_id int not null,
    group_id int not null,
    primary key (user_id, group_id)
);
