SELECT continent_name, country_name
FROM continents co
JOIN countries c ON co.continent_id = c.continent_id
;