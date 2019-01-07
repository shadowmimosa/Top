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
	
SELECT
	a.uid,
	c.race_name AS '赛事名称',
	b.NAME AS '项目名称',
	a.complete_meters AS '完成里程',
	(
	CASE
			
			WHEN b.`name` = '全程' THEN
			( IF ( a.complete_meters > 40000, '全马完成', '报全马跑半马' ) ) 
			WHEN b.`name` = '半程' THEN
			( IF ( a.complete_meters < 40000, '半马完成', '报半马跑全马' ) ) 
		END 
		) AS '黑白马',
		count( 1 ) AS '人数' 
	FROM
		yp_race_live.live_runner a,
		yp_race_live.live_race_item b,
		yp_race_live.live_race c 
	WHERE
		a.race_id = 22 
-- 		AND a.register_source = 2 
		AND b.id = a.race_item_id 
		AND c.race_id = a.race_id 
		AND a.complete_meters > 19000 
	GROUP BY
	b.`name`,
	a.complete_meters,
	a.uid

select  register_source, count(1) from live_runner where race_item_id = 54 and status in (2, 3) and complete_meters > 19261  and complete_meters < 22098 group by register_source
select  register_source, count(1) from live_runner where race_item_id = 56 and status in (2, 3) and complete_meters > 19261  and complete_meters < 22098 and source = 2 group by register_source
