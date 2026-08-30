CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES products(id)
);


INSERT INTO products (name, price)
VALUES
    ('Espresso', 120.00),
    ('Americano', 140.00),
    ('Cappuccino', 180.00),
    ('Latte', 160.00),
    ('Mocha', 200.00)
ON CONFLICT DO NOTHING;
