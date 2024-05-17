DROP TABLE IF cervejas EXISTS

CREATE TABLE cervejas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cervejaria VARCHAR(100) NOT NULL,
    estilo VARCHAR(50),
    teor_alcoolico DECIMAL(4, 2) NOT NULL,
    volume_ml INT NOT NULL,
    preco DECIMAL(8, 2) NOT NULL,
    quantidade_estoque INT NOT NULL,
    data_validade DATE
);

INSERT INTO cervejas (nome, cervejaria, estilo, teor_alcoolico, volume_ml, preco, quantidade_estoque, data_validade)
VALUES 
    ('IPA', 'Stone Brewing', 'India Pale Ale', 6.5, 355, 12.99, 50, '2024-12-31'),
    ('Stout', 'Guinness', 'Stout', 4.2, 500, 10.99, 30, '2024-12-31'),
    ('Pilsen', 'Heineken', 'Pilsen', 4.4, 330, 8.99, 40, '2024-12-31'),
    ('Weiss', 'Erdinger', 'Weissbier', 5.3, 500, 14.99, 20, '2024-12-31'),
    ('Super Bock', 'Unicer', 'Lager', 5.0, 330, 9.99, 60, '2024-12-31');