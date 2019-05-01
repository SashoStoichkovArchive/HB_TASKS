SELECT product.maker, AVG(hd) as DiskSpaceAvg 
    FROM pc
    INNER JOIN product
       ON pc.model = product.model
    GROUP BY maker
        HAVING product.maker IN (SELECT maker FROM printer 
                                    INNER JOIN product
                                        ON printer.model = product.model);