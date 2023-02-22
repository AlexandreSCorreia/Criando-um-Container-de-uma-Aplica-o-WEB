CREATE DATABASE FilmesDb;
GO
Use FilmesDb;
GO
CREATE TABLE Filmes
( 
  Id          smallint identity(1,1)
, Nome		  VARCHAR(100) NOT NULL
, Sinopse     VARCHAR(255) NOT NULL
, Imagem      VARCHAR(255) NOT NULL
, CONSTRAINT pkFilme PRIMARY KEY (Id)
);
GO