  SELECT sum(f1.count*f2.count) 
  FROM frequency f1, frequency f2
  WHERE (f1.term=f2.term)
  AND (f1.docid='10080_txt_crude' and f2.docid='17035_txt_earn')
  ;  