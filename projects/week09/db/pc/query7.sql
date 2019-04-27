SELECT (laptop_sum + pc_sum)/2 avarage_sum 
	FROM (
		SELECT SUM(price) laptop_sum 
			FROM product 
			INNER JOIN laptop 
				ON product.model = laptop.model 
			WHERE maker='B'
	) 
	JOIN (
		SELECT SUM(price) pc_sum
			FROM product
			INNER JOIN pc 
				ON product.model = pc.model 
			WHERE maker='B'
	);
