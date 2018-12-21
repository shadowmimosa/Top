SELECT
    b.id,
    b.NAME AS '项目名称',
    (
	CASE
			
			WHEN a.STATUS = 0 THEN
			'无数据' 
			WHEN a.STATUS = 1 THEN
			'进行中' 
			WHEN a.STATUS = 2 THEN
			'已完赛' 
			WHEN a.STATUS = 3 THEN
			'未完赛' 
			WHEN a.STATUS = 4 THEN
			'未参跑' 
		END 
		) AS '状态',
    (
		CASE
				
				WHEN source = 0 THEN
				'<问题数据>' 
				WHEN source = 1 THEN
				'实况数据' 
				WHEN source = 2 THEN
				'MQ数据' 
				WHEN source = 3 THEN
				'补数据<非跑表>' 
				WHEN source = 4 THEN
				'补数据<跑表>' 
			END 
			) AS '数据来源',
    count( 1 ) AS '人数'
FROM
    yp_race_live.live_runner a,
    yp_race_live.live_race_item b
WHERE
			a.race_item_id = 36
    AND a.race_item_id = b.id
    AND a.complete_secs > 0
GROUP BY
			a.RACE_ITEM_ID,
		a.STATUS,
	a.source