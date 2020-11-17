import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(columns = ['stat_prop', 'played_prop', 'played_val', 'played_2_prop', 'played_2_val', 'pos', 'dnp', 'peak_year_index'])
        .dropna(subset = ['rank', 'league', 'stat_val', 'team'])
        #.reset_index()
        .reset_index(drop = True)
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
        df1
        .drop(columns = ['year_index', 'stat_val'])
        .assign(rank_percentage = lambda x:  (df1['rank'] / df1['total_players'])*100)
        .loc[:, ['id', 'name', 'league', 'rank', 'rank_percentage']].groupby(by = ['id', 'name', 'league']).mean()
        .sort_values(['rank_percentage'], ascending = True)
        .reset_index()
    )

    # Make sure to return the latest dataframe

    return df2


def top_ten(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(columns = ['stat_prop', 'played_prop', 'played_val', 'played_2_prop', 'played_2_val', 'pos', 'dnp', 'peak_year_index'])
        .dropna(subset = ['rank', 'league', 'stat_val', 'team'])
        #.reset_index()
        .reset_index(drop = True)
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
        df1
        .drop(columns = ['year_index', 'stat_val'])
        .assign(rank_percentage = lambda x:  (df1['rank'] / df1['total_players'])*100)
        .loc[:, ['id', 'name', 'league', 'rank', 'rank_percentage']].groupby(by = ['id', 'name', 'league']).mean()
        .sort_values(['rank_percentage'], ascending = True)
        .reset_index()
    )
    
    df3 = (
        df2.head(10)
    )

    # Make sure to return the latest dataframe

    return df3

# League = mlb
def load_and_process_mlb(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(columns = ['stat_prop', 'played_prop', 'played_val', 'played_2_prop', 'played_2_val', 'pos', 'dnp', 'peak_year_index'])
        .dropna(subset = ['rank', 'league', 'stat_val', 'team'])
        #.reset_index()
        .reset_index(drop = True)
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
        df1[df1['league'] == 'mlb']
        .drop(columns = ['year_index', 'stat_val'])
        .assign(rank_percentage = lambda x:  (df1['rank'] / df1['total_players'])*100)
        .loc[:, ['id', 'name', 'league', 'rank', 'rank_percentage']].groupby(by = ['id', 'name', 'league']).mean()
        .sort_values(['rank_percentage'], ascending = True)
        .reset_index()
    )

    # Make sure to return the latest dataframe

    return df2


# SportName = basketball
def load_and_process_basketball(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(columns = ['stat_prop', 'played_prop', 'played_val', 'played_2_prop', 'played_2_val', 'pos', 'dnp', 'peak_year_index'])
        .dropna(subset = ['rank', 'league', 'stat_val', 'team'])
        #.reset_index()
        .reset_index(drop = True)
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
         df1[df1['sport_name'] == 'basketball']
        .drop(columns = ['year_index', 'stat_val'])
        .assign(rank_percentage = lambda x:  (df1['rank'] / df1['total_players'])*100)
        .loc[:, ['id', 'name', 'league', 'rank', 'rank_percentage']].groupby(by = ['id', 'name', 'league']).mean()
        .sort_values(['rank_percentage'], ascending = True)
        .reset_index()
    )

    # Make sure to return the latest dataframe

    return df2
