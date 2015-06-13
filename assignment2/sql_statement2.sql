SELECT count(*) FROM(
	SELECT term FROM(Frequency)
		WHERE docid='10398_txt_earn' and count=1
		
	);