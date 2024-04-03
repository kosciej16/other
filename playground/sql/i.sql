DROP TABLE IF EXISTS Movies CASCADE;
CREATE TABLE Movies (
    mID INT,
    title VARCHAR,
    genre VARCHAR,
    year INT,
    director VARCHAR,
    PRIMARY KEY (mID)
);

insert into Movies values (11, 'Star Wars', 'fantasy', 1977, 'George Lucas');
insert into Movies values (22, 'The Mask', 'comedy', 1994, 'Chuck Russell');
insert into Movies values (33, 'Iron Man', 'fantasy', 1994, 'Chuck Russell');

DROP TABLE IF EXISTS Reviewers CASCADE;
create table Reviewers (
    rID int,
    name varchar,
    PRIMARY KEY (rID)
);

insert into Reviewers values (21, 'Sarah Martinez'), (22, 'Daniel Lewis');

DROP TABLE IF EXISTS Ratings CASCADE;
create table Ratings (
    rID int,
    mID int,
    score int,
    ratingDate date,
    FOREIGN KEY (mID) REFERENCES Movies(mID),
    FOREIGN KEY (rID) REFERENCES Reviewers(rID)
);

insert into Ratings values (21, 11, 9, '2011-01-22');
insert into Ratings values (21, 22, 6, '2011-01-22');
insert into Ratings values (21, 33, 4, '2011-01-22');
insert into Ratings values (22, 11, 10, '2011-01-22');
insert into Ratings values (22, 33, 9, '2011-01-22');


create view tmp as select m.*, r.score, re.* from Movies m join Ratings r on m.mID = r.mID join Reviewers re on r.rID = re.rID;

--- 2. Find difference between maximum and minimal score for each movie genre
--- select title, score from Movies m join Ratings r on m.mID = r.mID join Reviewers re on r.rID = re.rID where year >= 2000


/*
mID	title		genre	year	director
-----|--------------|----------|------|-------------
11	Star Wars	fantasy	1977	George Lucas
22	The Mask	comedy 	1994	Chuck Russell


Reviewers
rID	name
-----|----------------
21	Sarah Martinez
22	Daniel Lewis


Ratings
rID	mID	score	ratingDate
-----|-------|--------|-----------
21	11	9	2011-01-22

*/
