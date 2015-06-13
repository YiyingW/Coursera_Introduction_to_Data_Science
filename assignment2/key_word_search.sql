SELECT MAX(score) FROM(
SELECT sum(f1.count*f2.count) as score
FROM view_name f1, view_name f2
WHERE (f1.term=f2.term)
AND (f2.docid='q')
GROUP BY f1.docid
)
;