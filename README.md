# Postgresql_programs

Notes on data relations

Initially i struggled with understanding the task and data organisation
- I was trying to insert data into a PostgreSql database by separating the info into two tables make and model. However i was unsure of the correct database design and how to link these two tables with a foreign key relationship between make and model

*This is the data i had 

 ```
  make                 model
  -----------------------------
  Import Trade Services  MB 300E
  Import Trade Services  MB 300SL
  Infiniti               EX35
  Mercedes-Benz          E63 AMG S 4matic (wagon)
  Mercedes-Benz          G500
  ```
# Solution
# To solve this one had to create the two tables of which that was provided for by the task..but what is important here is that one table make (will store car makes) and model (will store models)
# the model table will reference the make table via a foreign key 'make_id' to associate each model with the correct make.

CREATE TABLE make (
    id SERIAL,
    name VARCHAR(128) UNIQUE,
    PRIMARY KEY(id)
);

CREATE TABLE model (
  id SERIAL,
  name VARCHAR(128),
  make_id INTEGER REFERENCES make(id) ON DELETE CASCADE,
  PRIMARY KEY(id)
);

2. Foreign key relationship now was the second one as i realised that in order to link models with their make i need a foreign key (make_id) in the model table that referenced the make table...but i was unsure how to do it correctly insert the data in a way that would associate the models with corresponding makes.

# Solution
# The solution here was that in the model creation i needed to include a make_id foreign key that references the make table which is there .
# The insertion into table the model needed to pull the correct make_id from the make table. It was done using subqueries to fetch the make_id for each 

**Insert the make:**

```sql
INSERT INTO make (name)
VALUES 
    ('Import Trade Services'),
    ('Infiniti'),
    ('Mercedes-Benz');
```

**Insert the models with the corresponding foreign key:**

```sql
INSERT INTO model (name, make_id)
VALUES
    ('MB 300E', (SELECT id FROM make WHERE name = 'Import Trade Services')),
    ('MB 300SL', (SELECT id FROM make WHERE name = 'Import Trade Services')),
    ('EX35', (SELECT id FROM make WHERE name = 'Infiniti')),
    ('E63 AMG S 4matic (wagon)', (SELECT id FROM make WHERE name = 'Mercedes-Benz')),
    ('G500', (SELECT id FROM make WHERE name = 'Mercedes-Benz'));



3. Now came the correct syntax for foreign key inserts
The struggle i encounted was because i tried  to use commands \copy (specific to psql command) in sql tool Dbeaver, which ddnt work as expected.

# Solution
# Was to use sql insert statements instead of \copy
# Using subqueries int eh insert into model statements to correctly link each model with its make.
# the insert data into model table 


4.  This was something - Now while i was  trying to work with special characters in data, i encounted issues with encoding, the psql command showed a warning about a mismatch between th e console and windows code page, and i faced errors ERROR: invalid byte sequence for encoding "UTF8": 0xa4`

# Solution
# The thing here to sort this out was related to character encoding
# - I firstly checked the encoding of my Postgresql session by 'SHow client_encoding', which revealed the current was 'Win1252'
# - I the attempted to change the encoding to Utf8, which is more compatible with modern applications and special character
# - i used the following sql
#   SET client_encoding TO 'UTF8';



# WHY
# It acts as a constraint that establishes a relationship between two tables...data intergration
# Prevents orphan records
# simplifies querying
# And Cascades actions - if defines what happens when a record in the parent table is updated or deleted.

# HOW
# Can be useful to ensure referential intergrity - meaning that the values in one table (child table) correspond to valid values in the parent table
 
# WHAT
# II enforces a relationship between two tables
# - Links tables between a column or set of columns in one table(child) and a column or set of columns in another table (parent)
# - Enforces data integrity ensuring data is consistent between related tables.
# Prevents invalid data
# Ensures referential intergrity
# and Handles deletions/updates (cascading)








MANY TO MANY

Here i was writting sql commands to create three tables student course and roster, where roster is a join table that links students to courses and also defines the role of each student in a course

1. Now info about students, is that each student is uniquely identified by an id and their name is unique
- id is a unique identifier for each student (which is Auto incremented using serial)
- name is also unique since its marked unique.

2. As To also the course table



But onto this a  `DROP TABLE course CASCADE;` was included before creating the `course` table. This will drop the table if it exists, including any dependent objects (like foreign keys in other tables). This is useful when you want to reset the table schema

3. Roster table
- **`student_id`**: A foreign key linking to the `student` table. The `ON DELETE CASCADE` clause means if a student is deleted, all related rows in the `roster` table will be deleted as well.
- **`course_id`**: A foreign key linking to the `course` table. The `ON DELETE CASCADE` clause means if a course is deleted, all related rows in the `roster` table will be deleted as well.
- **`role`**: A field to store the student's role in the course (e.g., `1` for instructor, `0` for learner).
- **Primary Key**: The `id` field is the primary key for the `roster` table, ensuring uniqueness for each row.

### Data Insertion Example

After creating these tables, you can insert sample data into each table. Here's an example of how to insert data into the `student`, `course`, and `roster` tables.

#### Inserting into `student` Table:

```sql
INSERT INTO student (name) 
VALUES ('Siouxsie'), 
       ('Nabeeha'), 
       ('Naisha');
```

#### Inserting into `course` Table:

```sql
INSERT INTO course (title) 
VALUES ('si106'), 
       ('si110'), 
       ('si206');
```

#### Inserting into `roster` Table:

In the `roster` table, we associate students with courses and assign roles.

```sql
-- Siouxsie is an instructor for 'si106', others are learners
INSERT INTO roster (student_id, course_id, role)
VALUES
    ((SELECT id FROM student WHERE name = 'Siouxsie'), (SELECT id FROM course WHERE title = 'si106'), 1),  -- Instructor
    ((SELECT id FROM student WHERE name = 'Nabeeha'), (SELECT id FROM course WHERE title = 'si106'), 0),  -- Learner
    ((SELECT id FROM student WHERE name = 'Naisha'), (SELECT id FROM course WHERE title = 'si106'), 0);  -- Learner
```

### Explanation of the Changes:

1. **Normalization**:
   - The `student`, `course`, and `roster` tables are designed to be normalized. There is no redundant data, and relationships between students and courses are maintained through foreign keys.

2. **Foreign Keys**:
   - The `roster` table uses `student_id` and `course_id` as foreign keys, which ensure referential integrity. The `ON DELETE CASCADE` clause ensures that if a student or course is deleted, the corresponding entries in the `roster` table are also deleted.

3. **Unique Constraints**:
   - The `UNIQUE(student_id, course_id)` constraint ensures that no student can be enrolled in the same course multiple times.
