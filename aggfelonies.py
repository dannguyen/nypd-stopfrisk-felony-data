"""
Did the drastic drop in NYPD stop and frisks result in a rise in felonies?

This script aggs the stop-and-frisk and felonies data by year and precinct.

Then it subtracts
"""

from pathlib import Path
import pandas as pd
DATA_PATH = Path('data')
MIN_DATE = pd.datetime(2010, 1, 1)
# http://www.nyc.gov/html/nypd/downloads/pdf/analysis_and_planning/seven_major_felony_offenses_by_precinct_2000_2015.pdf
# precinct 121 was created from precincts 120 and 122 on 2013-07-01
X_PRECINCTS = [120, 121, 122]

def load_and_count_stops_by_year():
    ydf = pd.concat([pd.read_csv(_f, usecols=['year'])
                             for _f in DATA_PATH.glob('stops*.csv')])
    return ydf.groupby('year').size()


def load_felonies():
    fn = DATA_PATH.joinpath('bulk-data-nypd-7-major-felonies.csv')
    fdf = pd.read_csv(fn, parse_dates=['occurrence_date'])
    # limit to 2010+; for now, agg all felonies together
    return fdf[fdf.occurrence_date >= MIN_DATE]

def agg_felonies(fdf):
    fdf['year'] = fdf.occurrence_date.dt.year
    gf = fdf[['year', 'precinct']].groupby(['year', 'precinct']).agg(len).reset_index()
    gf.columns = ['year', 'precinct', 'felonies']
    return gf



if __name__ == '__main__':
    from time import sleep

    # we only load the stop and frisk data to see
    # how the numbers of drastically declined over the years
    print("Stop and frisks by year")
    print(load_and_count_stops_by_year().to_string())

    sleep(2) # pause a bit
    # Now load the felonies
    print("\n")
    print("Loading and aggregating felonies")
    felonies = agg_felonies(load_felonies())
    # remove non-usable precincts, then pivot
    pvf = felonies[-felonies.precinct.isin(X_PRECINCTS)].pivot(index='precinct', columns='year', values='felonies')
    pvf['delta_2011_2015'] = (100 * (pvf[2015] - pvf[2011]) / pvf[2011]).round(1)
    print("Precincts ranked in order of drop in felony rate, 2011-2015:")
    print(pvf.sort_values('delta_2011_2015').to_string())


    print("Overall change in felony rate:")
    f2011 = pvf[2011].sum()
    for year in range(2012, 2015 + 1):
        x = round(100 * (f2011 - pvf[year].sum())/ f2011, 1)
        print("2011-{}: {}%".format(year, x))


