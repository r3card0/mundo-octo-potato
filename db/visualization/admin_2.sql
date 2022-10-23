SELECT at.admin_type 
, admin2_name
, country_name
, continent_name
FROM continents c
JOIN countries co ON c.continent_id = co.continent_id
JOIN admin2 a2 ON a2.country_id = co.country_id
JOIN admin_types at ON at.admin_type_id = a2.admin_type
;