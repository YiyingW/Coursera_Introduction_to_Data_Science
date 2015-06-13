SELECT count(*) FROM(
	SELECT docid FROM(Frequency)
		GROUP BY docid
		HAVING sum(count)>300 
		
	);