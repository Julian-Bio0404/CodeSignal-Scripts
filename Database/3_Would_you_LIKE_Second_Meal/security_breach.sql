/*
You are managing a large website that uses a special algorithm
for user identification. In particular, it generates a unique
attribute for each person based only on their first and last
names and some additional metadata.

After analyzing the server logs today you found out that the
website security has been breached and the data of some of
your users might have been compromised.

The users' info is stored in the table users with the following
structure:

    - first_name: user's first name;
    - second_name: user's last name;
    - attribute: a unique attribute string of this user.

It seems that only the users those attribute was generated by the
old version of your special algorithm were affected. Such attributes
have the following format (accurate to letter cases): <one or more
arbitrary character>%<first name>_<second name>%<zero or more
arbitrary characters>. It's your duty now to warn the users that
have these attributes about possible risks.

Given the users table, compose the resulting table consisting only
of the rows that contain affected users' info. The result should be
sorted by the attributes in ascending order.
*/


CREATE PROCEDURE solution()
BEGIN
	SELECT *
    FROM users
    WHERE attribute LIKE BINARY concat('_%\%',first_name,'\_',second_name,'\%%');
END