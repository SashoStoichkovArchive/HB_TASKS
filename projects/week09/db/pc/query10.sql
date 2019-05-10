SELECT AVG(cd)
    FROM pc
    JOIN product ON product.model=pc.model
    WHERE maker IN (SELECT maker FROM product WHERE type='Printer');