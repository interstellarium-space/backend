CREATE TABLE IF NOT EXISTS users (
	id INTEGER AUTOINCREMENT NOT NULL,
	email VARCHAR(255) NOT NULL,
	password_hash VARCHAR(512) NOT NULL,
	name VARCHAR(255),
	PRIMARY KEY (id),
	UNIQUE (email)
);