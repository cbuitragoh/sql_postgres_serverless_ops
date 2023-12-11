--Create postgres user
CREATE USER dev WITH PASSWORD {} VALID UNTIL {} CREATEDB;

--Create tablespace
CREATE TABLESPACE dev_env LOCATION '/var/lib/postgresql/data';

--Create database with owner
CREATE DATABASE dev_env OWNER dev TABLESPACE pg_default;

--Select connections databata
SELECT count(distinct(numbackends)) FROM pg_stat_database;

--maximum number of connections allowed
SHOW max_connections;

--current connections
SELECT datname, numbackends FROM pg_stat_database;

--details connections for database
SELECT * FROM pg_stat_activity WHERE datname={};

--delete specific connection
SELECT pg_terminate_backend(pid);

--select all data from table
SELECT * FROM {};

--create view from specific data groupby column
CREATE VIEW {} AS SELECT {} FROM {} GROUP BY {};

--create materialized view from specific data groupby 
CREATE MATERIALIZED VIEW {} AS SELECT {} FROM {} GROUP BY {};   

--specific queries to interest
SELECT * FROM creditcard
WHERE "V1">0.5 AND "V2"<0.5;

--select all fraud class values
SELECT COUNT(*) FROM creditcard
WHERE "Class"=1

--select max value for 3 first one PCA columns
SELECT MAX("V1"), MAX("V2"), MAX("V3") FROM creditcard AS principal_pca;

--compare column value to aggregate MIN column value from other columns
SELECT
	"V10",
	LEAST ("V11", "V12", "V13") AS lowest_values
FROM
	creditcard;

--showing groupby data in prettify way
SELECT
	MAX("V28") AS max_28,
	MIN("V25") AS min_25,
	AVG("V15") AS avg_15
FROM
	creditcard
WHERE
	"Class"=1
GROUP BY
	"V20"
ORDER BY
	COUNT("V15") DESC

--apply subquery techniques
SELECT
	"V12" AS PCA_12,
	"V18" AS PCA_18,
	"V22" AS PCA_22,
	"V24" AS PCA_24

FROM
	(
		SELECT * FROM creditcard
		WHERE "Class"=1 AND "Amount">10000
	) AS final_PCAs

LIMIT 50

--aggregation functions

SELECT
	COUNT("Amount") AS Amount_count,
	MAX("V27") AS max_V27,
	MAX("V26") as max_26
FROM
	creditcard
GROUP BY 
	"V13", "V19", "V17"
HAVING
	"V17"<=0
ORDER BY
	"V13" ASC
