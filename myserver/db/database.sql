
drop table users;
drop table crypto_data;
drop table user_preferences;
create table users
(
    name varchar(64) PRIMARY KEY,
    password varchar(64)
);
create table crypto_data
(
    id varchar(64) PRIMARY KEY,
    name varchar(64),
    symbol varchar(64),
    rank int,
    price_usd float,
    price_btc float,
    volume_24h_usd float,
    market_cap_usd float,
    available_supply int,
    total_supply int,
    percent_change_1h float,
    percent_change_24h float,
    percent_change_7d float,
    last_updated int
);
    create table user_preferences
    (
        name varchar(64) PRIMARY KEY,
        city varchar(64),
        employer varchar(64),
        age int,
        FOREIGN KEY (name) REFERENCES users(name)
    );
