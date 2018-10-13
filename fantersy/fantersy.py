#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import yaml
import requests
import webbrowser
from bs4 import BeautifulSoup
from texttable import Texttable
from color import Color


class OAuth:
    """
    OAuth token.
    """
    token = None


class Fantersy:
    """
    Fantasy Baseball CLI Client.
    """
    # OAuth constants
    AUTH_URL = 'https://api.login.yahoo.com/oauth2/request_auth'
    TOKEN_URL = 'https://api.login.yahoo.com/oauth2/get_token'
    REDIRECT_URI = 'oob'
    RESPONSE_TYPE = 'code'
    GRANT_TYPE = 'authorization_code'
    # Fantasy API URL formats
    TEAM_ID_URL_FORMAT = 'https://fantasysports.yahooapis.com/fantasy/v2/league/{}.l.{}/standings'
    LEAGUE_URL_FORMAT = 'https://fantasysports.yahooapis.com/fantasy/v2/league/{}.l.{}'
    ROSTER_URL_FORMAT = 'https://fantasysports.yahooapis.com/fantasy/v2/team/{}.l.{}.t.{}/players'
    PLAYER_URL_FORMAT = 'https://fantasysports.yahooapis.com/fantasy/v2/league/{}.l.{}/players;'

    def __init__(self, config_path):
        """
        Initialize.

        :param config_path: user config.
        """
        config = yaml.load(
            open(config_path, 'r')
        )
        self.CLIENT_ID = config['CLIENT_ID']
        self.CLIENT_SECRET = config['CLIENT_SECRET']
        self.SPORT_TYP = config['FANTASY']['SPORT_TYP']
        self.LEAGUE_ID = config['FANTASY']['LEAGUE_ID']
        if OAuth.token is None:
            OAuth.token = self.__init_token()

    # ============= private methods =============

    def __init_token(self):
        """
        Get OAuth token.
        """
        # authorization code.
        self.__get_authorization_code()
        # oauth token.
        return self.__get_token()

    def __get_authorization_code(self):
        """
        Get authorization code.
        """
        params = {
            'client_id': self.CLIENT_ID,
            'redirect_uri': self.REDIRECT_URI,
            'response_type': self.RESPONSE_TYPE
        }
        res = requests.get(
            self.AUTH_URL,
            params=params,
            allow_redirects=False
        )
        if res.status_code == 302:
            webbrowser.open(res.url)

    def __get_token(self):
        """
        Get OAuth token.
        """
        code = input('authorization code >> ')
        params = {
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
            'redirect_uri': self.REDIRECT_URI,
            'response_type': self.RESPONSE_TYPE,
            'grant_type': self.GRANT_TYPE,
            'code': code
        }
        return requests.post(
            self.TOKEN_URL,
            data=params
        ).json()['access_token']

    def __get_team_id(self, team_nm):
        """
        Get team id.

        :param team_nm: team name.
        :return: team id.
        """
        bs = self.__request_fantasy(
            self.TEAM_ID_URL_FORMAT.format(self.SPORT_TYP, self.LEAGUE_ID)
        )
        teams = {}
        for team in bs.find_all('team'):
            teams[team.find('name').text.upper()] = team.find('team_id').text
        # partial match
        for key in teams.keys():
            if team_nm.upper() in key:
                return teams[key]

    def __get_player(self, bs, is_sorted=False):
        """
        Get player info from XML.

        :param bs: BeautifulSoup object.
        :param is_sorted: sort flag.
        :return: player table.
        """
        players = []
        for player in bs.find_all('player'):
            info = [
                player.find('display_position').text.upper(),
                player.find('name').find('full').text,
                player.find('editorial_team_abbr').text.upper()
            ]
            players.append(info)
        if is_sorted:
            players.sort()
        return self.__create_table(['POS', 'NAME', 'TEAM'], players)

    @staticmethod
    def __request_fantasy(url):
        """
        HTTP request for Fantasy Sports.

        :param url: request url.
        :return: BeautifulSoup object.
        """
        res = requests.get(
            url,
            headers={'Authorization': 'Bearer ' + OAuth.token}
        )
        return BeautifulSoup(res.text, 'html.parser')

    @staticmethod
    def __create_table(header, rows, is_deco=False):
        """
        Create text table.

        :param header: table header.
        :param rows: table rows.
        :param is_deco: deco flag.
        :return: Texttable object.
        """
        table = Texttable()
        if is_deco:
            table.set_deco(Texttable.HEADER)
        contents = [header]
        contents.extend(rows)
        table.add_rows(contents)
        return table

    @staticmethod
    def __colored_print(text):
        """
        Print green color text.

        :param text: printed text.
        """
        print(Color.GREEN + text + Color.END)

    # ============= Fantersy API =============
    def league(self, args):
        """
        Fantersy API: Get league info.
        # args will not be used.

        :param args: args
        """
        bs = self.__request_fantasy(
            self.LEAGUE_URL_FORMAT.format(self.SPORT_TYP, self.LEAGUE_ID)
        )
        contents = [
            [
                'LEAGUE NAME',
                bs.find('name').text
            ],
            [
                'TEAM NUMBER',
                bs.find('num_teams').text
            ],
            [
                'START',
                bs.find('start_date').text
            ],
            [
                'END',
                bs.find('end_date').text
            ]
        ]
        table = self.__create_table(['NAME', 'CONTENT'], contents)
        self.__colored_print(table.draw())

    def roster(self, args):
        """
        Fantersy API: Get selected team roster.

        :param args: args
        """
        team_nm = args[0]
        bs = self.__request_fantasy(
            self.ROSTER_URL_FORMAT.format(
                self.SPORT_TYP,
                self.LEAGUE_ID,
                self.__get_team_id(team_nm)
            )
        )
        team_nm = bs.find('team').find('name').text
        table = self.__get_player(bs, True)
        self.__colored_print('### {} ###'.format(team_nm))
        self.__colored_print(table.draw())

    def player(self, args):
        """
        Fantersy API: Get players with some filter options.

        :param args: args
        """
        url = self.PLAYER_URL_FORMAT.format(self.SPORT_TYP, self.LEAGUE_ID)
        for arg in args:
            url = url + arg + ';'
        bs = self.__request_fantasy(url)
        table = self.__get_player(bs)
        self.__colored_print(table.draw())
