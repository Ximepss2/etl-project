-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "MOVIE_DATA" (
    "index" INT PRIMARY KEY,
    "Title" VARCHAR   NOT NULL,
    "Production_Company" VARCHAR   NOT NULL,
    "Genre" VARCHAR   NOT NULL,
    "Country" VARCHAR   NOT NULL,
    "Language" VARCHAR   NOT NULL,
    "Release_Date" VARCHAR   NOT NULL,
    "Runtime"  VARCHAR NOT NULL,
    "Budget"  VARCHAR NOT NULL,
    "Revenue"  VARCHAR NOT NULL,
    "Vote_Count" VARCHAR NOT NULL,
    "Rating" VARCHAR NOT NULL
);

CREATE TABLE "Credits_Data" (
    "index" INT PRIMARY KEY,
    "Director" VARCHAR,
    "Leading_Role" VARCHAR ,
    "Supporting_Role" VARCHAR ,
    "Supporting_Role_2" VARCHAR ,
    "Producer" VARCHAR ,
    "DP" VARCHAR ,
    "Writer" VARCHAR ,
    "Music_Composer" VARCHAR
);

