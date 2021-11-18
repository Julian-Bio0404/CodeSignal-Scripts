CREATE PROCEDURE websiteHacking()
BEGIN
    SELECT id,login,name
    FROM users
    WHERE type='user'
    OR type IS NOT NULL
    ORDER BY id;
END