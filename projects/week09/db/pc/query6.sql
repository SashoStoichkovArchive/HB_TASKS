SELECT maker, avg(price)
	FROM product 
	JOIN pc 
		ON pc.model = product.model 
		WHERE pc.model IS NOT NULL 
	GROUP BY maker;
