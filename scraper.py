#!/usr/bin/env python
import requests
import lxml.html
import scraperwiki

html = requests.get('http://www.premierleague.com/tables').content

dom = lxml.html.fromstring(html)

premierLeagueData = []

currentPane = dom.cssselect('.mainTableTab')[0]
for row in currentPane.cssselect('table .tableBodyContainer > tr:not(.expandable)'):
    pos = int(row.cssselect('.pos .value')[0].text_content())
    team = row.cssselect('.team .long')[0].text_content()
    goalsFor = int(row.cssselect('td')[7].text_content())
    goalsAgainst = int(row.cssselect('td')[8].text_content())
    goalDifference = int(row.cssselect('td')[9].text_content())
    points = int(row.cssselect('.points')[0].text_content())
    # print pos, team,"gf", goalsFor, "ga", goalsAgainst, "gd", goalDifference, "pts", points
    teamItem = {
        'pos':pos,
        'team':team,
        'gf':goalsFor,
        'ga':goalsAgainst,
        'gd':goalDifference,
        'pts':points
    }
    premierLeagueData.append(teamItem)

if len(premierLeagueData) > 0:
    #truncate data store
    scraperwiki.sql.execute("DROP TABLE IF EXISTS `swdata`")
    #add each table line to data store
    for teamItem in premierLeagueData:
        scraperwiki.sql.save(['team'], teamItem)
else:
    raise ValueError('Cannot read table, maybe format or URL has changed.')
