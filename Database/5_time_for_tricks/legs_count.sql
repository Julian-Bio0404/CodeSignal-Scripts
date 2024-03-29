/*
You really love counting stuff. In fact, right now you're sitting on a meadow
and counting all the legs you see there! There are some people, some dogs,
and some cats on the meadow. You're pretty confident that each human has 2
legs and that cats and dogs have 4 legs each.

The information about all the creatures on the meadow is stored in the table
creatures. It has the following structure:

    - id: the unique creature ID;
    - name: the creature's name;
    - type: the creature's type - "human", "cat", or "dog". This column
      has ENUM type.

You want to calculate the total number of legs in the meadow. Given the table
creatures, build a new table that only contains one column summary_legs and
has only one row with the total number of legs that you can see.
*/


DROP PROCEDURE IF EXISTS legsCount;
CREATE PROCEDURE legsCount()
    SELECT (SUM(IF(type = 'human', 2, 4)))  as summary_legs
    FROM creatures
    ORDER BY id;