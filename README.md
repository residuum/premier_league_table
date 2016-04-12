This is a scraper that runs on [Morph](https://morph.io). To get started [see the documentation](https://morph.io/documentation).

This scraper downloads the current table of the English Football Premier League and stores it in a database. The data is then accessed via a JSON API for [sonification with libPd](https://github.com/residuum/premier-league-sonification).

The table is output as an array with each team being an object with the following format:

    {
      pos: <integer, position 1-20>,
      team: <string, team name>,
      pts: <integer, points>,
      gf: <integer, goals for>,
      ga: <integer, goals against>,
      gd: <integer, goal difference>
    }
