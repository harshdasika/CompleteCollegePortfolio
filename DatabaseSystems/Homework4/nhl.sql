/* Delete the tables if they already exist */
DROP DATABASE IF EXISTS nhl;
CREATE DATABASE nhl;
USE nhl;

DROP TABLE IF EXISTS player CASCADE;
DROP TABLE IF EXISTS team CASCADE;
DROP TABLE IF EXISTS injury_report CASCADE;
DROP TABLE IF EXISTS game CASCADE; 


CREATE TABLE player (
	id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
	position VARCHAR(20) NOT NULL,
	skill_level VARCHAR(30) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE team (
	team_id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
	city CHAR(20) NOT NULL,
	coach VARCHAR(30) NOT NULL,
    captain INT NOT NULL,
    FOREIGN KEY (captain) REFERENCES player(id),
	PRIMARY KEY (team_id)
);

CREATE TABLE injury_report (
	injury_id INT NOT NULL,
    player_id INT NOT NULL,
    description VARCHAR(200),
    FOREIGN KEY (player_id) REFERENCES player(id),
	PRIMARY KEY (injury_id)
);

CREATE TABLE game (
	game_id INT NOT NULL,
    score VARCHAR(5) NOT NULL,
	date VARCHAR(10) NOT NULL,
    hostTeam_id INT NOT NULL,
    guestTeam_id INT NOT NULL,
    FOREIGN KEY (hostTeam_id) REFERENCES team(team_id),
    FOREIGN KEY (guestTeam_id) REFERENCES team(team_id),
	PRIMARY KEY (game_id)
);


INSERT INTO player (id, name, position, skill_level)
VALUES (1, 'Chris Kreider', 'Captain/Winger', 'High'),
	   (2, 'Tony DeAngelo', 'Winger', 'Medium'),
       (3, 'Oliver Ekman-Larsson', 'Defenceman', 'High'),
       (4, 'Lawson Crouse', 'Winger', 'Medium');

INSERT INTO team (team_id, name, city, coach, captain)
VALUES (1, 'New York Rangers', 'New York City', 'David Quinn', 1),
	   (2, 'Arizona Coyotes', 'Glendale', 'Rick Tocchet', 3);
       
INSERT INTO game (game_id, score, date, hostTeam_id, guestTeam_id)
VALUES (1, '4-2', '2019-03-04', 1, 2),
	   (2, '3-4', '2020-10-22', 2, 1);

INSERT INTO injury_report (injury_id, player_id, description)
VALUE (1, 2, 'Pulled hamstring on 10/22/2020. Cannot play for two weeks.');


