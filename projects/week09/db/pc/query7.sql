SELECT type, AVG(price) FROM laptop
    INNER JOIN product
        ON laptop.model = product.model
WHERE product.maker = 'B'

UNION

SELECT type, AVG(price) FROM pc
    INNER JOIN product
        ON pc.model = product.model
WHERE product.maker = 'B';