-- Lists all ciyies if Califonia
SELECT id, name FROMcities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY cities.id;;
