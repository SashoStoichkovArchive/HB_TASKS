SELECT (SUM(pc.price) + SUM(laptop.price)) / COUNT(*)
    FROM product
    LEFT OUTER JOIN pc ON product.model = pc.model
    LEFT OUTER JOIN laptop ON product.model = laptop.model
    WHERE product.maker ='B';