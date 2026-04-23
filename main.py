import pandas as pd
import sqlite3

#PART 1: PLANETS DATABASE

#Step 0
conn1 = sqlite3.connect("planets.db")
pd.read_sql("SELECT * FROM planets;", conn1)

#step 1
df_step1 = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons = 0;
""", conn1)

#step 2
df_step2 = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE LENGTH(name) = 7;
""", conn1)

#step 3
df_step3 = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE mass <= 1.00;
""", conn1)

#step 4
df_step4 = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons >= 1
AND mass < 1.00;
""", conn1)

#step 5
df_step5 = pd.read_sql("""
SELECT name, color
FROM planets
WHERE color LIKE 'blue';
""", conn1)

#PART 2: DOGS DATABASE

# Step 0
conn2 = sqlite3.connect("dogs.db")
pd.read_sql("SELECT * FROM dogs;", conn2)

# Step 6
df_step6 = pd.read_sql("""
SELECT name, age, breed
FROM dogs
WHERE hungry = 1
ORDER BY age ASC;
""", conn2)

# Step 7
df_step7 = pd.read_sql("""
SELECT name, age, hungry
FROM dogs
WHERE hungry = 1
AND age BETWEEN 2 AND 7
ORDER BY name ASC;
""", conn2)

# Step 8
df_step8 = pd.read_sql("""
SELECT name, age, breed
FROM (
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC
    LIMIT 4
)
ORDER BY breed ASC;
""", conn2)

#PART 3: BABE RUTH DATABASE

# Step 0
conn3 = sqlite3.connect("babe_ruth.db")
pd.read_sql("SELECT * FROM babe_ruth_stats;", conn3)

# Step 9
df_step9 = pd.read_sql("""
SELECT COUNT(*) AS total_years
FROM babe_ruth_stats;
""", conn3)

# Step 10
df_step10 = pd.read_sql("""
SELECT SUM(HR) AS total_home_runs
FROM babe_ruth_stats;
""", conn3)

# Step 11
df_step11 = pd.read_sql("""
SELECT team, COUNT(*) AS number_years
FROM babe_ruth_stats
GROUP BY team;
""", conn3)

# Step 12
df_step12 = pd.read_sql("""
SELECT team,
       AVG(at_bats) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(at_bats) > 200;
""", conn3)

