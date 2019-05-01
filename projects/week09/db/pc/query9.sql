SELECT product.maker, pc.model, MAX(pc.price)
    FROM product
    INNER JOIN pc
        ON product.model = pc.model
    GROUP BY product.model;