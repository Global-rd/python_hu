CREATE TABLE TEST(
	ID INT,
	NAME VARCHAR(30),
	ADDRESS VARCHAR(50)
)

SELECT * FROM TEST

INSERT INTO TEST (ID, NAME, ADDRESS) VALUES (2, 'panna', 'y utca')

update test set name = 'Laci' where id = 1

delete from test where id = 1