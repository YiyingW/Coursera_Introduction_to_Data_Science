SELECT count(*) FROM(
	SELECT docid FROM(Frequency)
		WHERE term='transactions' 
	INTERSECT 
	SELECT docid FROM(Frequency)
		WHERE term='world' 
	
		
	);