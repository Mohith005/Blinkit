USE thinkit_demo;

-- Synthetic catalog for the demo. Run once after creating the schema.
INSERT INTO a (code, item, price) VALUES
    (101, 'Mango box', 275.00), (102, 'Bananas', 62.50);
INSERT INTO b (code, item, price) VALUES
    (201, 'Tomatoes', 38.50), (202, 'Carrots', 45.00);
INSERT INTO c (code, item, price) VALUES
    (301, 'Orange juice', 95.00), (302, 'Lemon soda', 35.00);
INSERT INTO d (code, item, price) VALUES
    (401, 'Potato chips', 40.00), (402, 'Roasted chickpeas', 65.00);
INSERT INTO e (code, item, price) VALUES
    (501, 'Dark chocolate', 120.00), (502, 'Coconut cookies', 80.00);
INSERT INTO f (code, item, price) VALUES
    (601, 'Pet shampoo', 220.00), (602, 'Pet brush', 175.00);
INSERT INTO g (code, item, price) VALUES
    (701, 'Basmati rice', 310.00), (702, 'Red lentils', 125.00);
INSERT INTO h (code, item, price) VALUES
    (801, 'Whole milk', 68.00), (802, 'Plain yogurt', 55.00);
INSERT INTO i (code, item, price) VALUES
    (901, 'Adhesive bandages', 90.00), (902, 'Antiseptic wipes', 110.00);
INSERT INTO j (code, item, price) VALUES
    (1001, 'Hand soap', 85.00), (1002, 'Toothpaste', 109.00);
INSERT INTO x (code, item, price) VALUES
    (1101, 'Summer fruit bundle', 199.00), (1102, 'Iced tea multipack', 145.00);
INSERT INTO y (code, item, price) VALUES
    (1201, 'Dog treats', 150.00), (1202, 'Cat food pouch', 78.00);
INSERT INTO z (code, item, price) VALUES
    (1301, 'First-aid kit', 299.00), (1302, 'Digital thermometer', 249.00);
