SELECT maker, avg(screen) 
	FROM product 
		JOIN laptop on laptop.model = product.model 
			WHERE laptop.model IS NOT NULL
		GROUP BY maker;
