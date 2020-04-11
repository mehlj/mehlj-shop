#!/bin/bash

file="shop.db"

if [ -f $file ]; then
    rm -f $file
fi

sqlite3 $file <<DBINIT
CREATE TABLE IF NOT EXISTS inventory(
   item TEXT PRIMARY KEY NOT NULL,
   price REAL NOT NULL,
   quantity INTEGER NOT NULL
);
INSERT INTO inventory VALUES ('apple', 3.99, 54);
INSERT INTO inventory VALUES ('pear', 4.99, 12);
DBINIT
