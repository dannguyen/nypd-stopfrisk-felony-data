# NYPD stop-and-frisk and felonies data

This repo contains a selection of the New York Police Department's NYPD stop-and-frisk data and its recently released 7 Major Felony Incidents dataset for the years 2010 through 2015.

## About the data

This repo's [data/](data/) directory contains the bulk files. However, the original data files have been wrangled and trimmed for easier usage. The changes include standardization of the date fields, reprojecting the geospatial data as latitude and longitude, removing redundant or otherwise useless fields, and adding convenience fields -- such as `was_force_used` for the stop-and-frisk data.

The wrangling (and fetching) scripts can be found in the [scripts/ folder](https://github.com/dannguyen/python-notebooks-data-wrangling/tree/master/scripts) in my repo of data-wrangling iPython notebooks: 

[https://github.com/dannguyen/python-notebooks-data-wrangling](https://github.com/dannguyen/python-notebooks-data-wrangling)

##### The original, official datasets can be found at these links:

- [NYPD Stop, Question and Frisk Report Database](http://www.nyc.gov/html/nypd/html/analysis_and_planning/stop_question_and_frisk_report.shtml)
- [7 Major Felony Incidents](https://data.cityofnewyork.us/Public-Safety/NYPD-7-Major-Felony-Incidents/hyij-8hr7)

The data is provided here for the convenience of those who want to examine whether the vast reduction in stop-and-frisk actions has resulted in a corresponding increase in felony incidents.


## About recent years of NYPD's stop and frisks

To review the history, NYPD's stop-and-frisk activity reached a peak of 685,000+ actions in 2011. In 2013, a [federal judge ruled that the NYPD's tactics violated the constitutional rights of minorities](http://www.nytimes.com/2013/08/13/nyregion/stop-and-frisk-practice-violated-rights-judge-rules.html). By the end of 2013, stop-and-frisk actions [fell to 10% of the prior year](http://www.nytimes.com/interactive/2014/09/19/nyregion/stop-and-frisk-is-all-but-gone-from-new-york.html).

[And in the 2015 data](http://www.nyclu.org/content/stop-and-frisk-data), the number of reports fell below __23,000__.


This New York Times story, dated Dec. 11, 2015, [Decline in Stop-and-Frisk Tactic Drives Drop in Police Actions in New York, Study Says](http://www.nytimes.com/2015/12/12/nyregion/end-to-stop-and-frisk-drives-drop-in-police-actions-in-new-york-study-says.html), reports that crime incidents have seemed to gone down, though disenfranchised communities may still deal with a disproportionate amount of enforcement:

> Some are concerned that excessive enforcement has shifted to areas where they are harder to detect — moving violations, for example. About a million moving violations summonses are issued each year, and they made up more than 58 percent of enforcement actions in 2014, according to the study. Researchers said data on moving violations was available only for the four-year period ending in 2014 and could not be broken down based on demographics, leaving questions about how those violations are issued.

However, while the overall crime rate reached a historic low, [the most serious crimes had a small _increase_](http://www.wsj.com/articles/nyc-officials-tout-new-low-in-crime-but-homicide-rape-robbery-rose-1451959203). 
> But while crime in the city continued its historic downward trend, led largely by a drop in burglaries and stolen vehicles, three of the most serious crimes rose in 2015: homicides were up 5.1%, rapes 6.3% and robberies 2.1%. Also, crime increased in two of the city’s five boroughs: Manhattan and the Bronx.

And [former police commissioner Raymond Kelly](http://nypost.com/2015/12/23/ray-kelly-accuses-bratton-of-fudging-record-low-crime-stats/) thinks the numbers are being cooked:

> “I think you’ve got to . . . look at those numbers because I think there are some issues with the numbers that are being put out,” Kelly said on AM 970. “I think there’s some redefinition going on as to what amounts to a shooting, that sort of thing.

> “I mean, look, all administrations want to show that crime is down,” he added.

> “But you have to take a hard look at those numbers, and I can tell you, people don’t feel safer in this city. People say this to me all the time. And perception is reality in many instances. So the city feels unsafe in many people’s minds and unsafe in many neighborhoods in people’s minds.”

And just to make things even more nebulous, [people suspect NYPD officers](http://www.capitalnewyork.com/article/city-hall/2016/02/8591131/court-monitor-faults-nypds-stop-and-frisk-data-collection) aren't consistently recording their stop-and-frisk actions; here's an excerpt from the [94-page report](assets/ccrjustice-floyd-monitor-feb-2016-report.pdf) via the court's appointed monitor:

> As described to us by many officers, the pressure for numbers caused by these
evaluations and performance objectives affected stop-related activity in two ways. First, there were stops of people who should not have been stopped because the officers did not have the required reasonable suspicion for the stop. 

> Second, officers would complete a stop report for encounters that were not stops at all, but voluntary encounters or Level 1 or 2 encounters, or even create fictitious reports purportedly documenting encounters that had not happened.

That sounds like a bucket of fun to deal with when doing the data analysis...


## How to use the data

Just clone this repo and play with the [data/](data/) files as you please. 

I've included a script named [aggfelonies.py](aggfelonies.py) that shows how to load the data into pandas DataFrames and do some filtering and querying. Running the script from your shell will produce roughly the output below.

This is a very blunt, unsophisticated analysis, as the aggregation is only at the precinct and year level. However, it seems like the felony rate has increased when comparing 2015 to 2011:


~~~
Stop and frisks by year
year
2010    601285
2011    685724
2012    532911
2013    191851
2014     45787
2015     22563


Loading and aggregating felonies
Precincts ranked in order of drop in felony rate, 2011-2015:


          2010  2011  2012  2013  2014  2015  delta_2011_2015
precinct                                                     
113       2140  2360  2375  2043  1882  1542            -34.7
49        1676  1757  1548  1184  1080  1217            -30.7
112        822   906   916   847   744   636            -29.8
104       1738  1715  1667  1618  1509  1321            -23.0
88        1142  1116  1230  1093  1099   876            -21.5
73        2022  2135  2240  2093  1873  1704            -20.2
107       1314  1312  1272  1305  1102  1075            -18.1
79        1839  1860  1922  1730  1657  1527            -17.9
67        2167  2492  2446  2364  2334  2057            -17.5
63        1334  1351  1394  1294  1204  1114            -17.5
108       1256  1273  1195  1338  1267  1073            -15.7
22         102   103   101   103    83    87            -15.5
70        1993  1910  1891  1843  1706  1628            -14.8
66        1289  1282  1246  1181  1165  1094            -14.7
123        384   406   397   380   383   347            -14.5
114       2023  2015  2091  1892  1898  1727            -14.3
83        1826  1842  2016  1901  1797  1634            -11.3
33         887   879   908   930   806   781            -11.1
110       1646  1631  1758  1740  1617  1472             -9.7
77        1407  1617  1604  1790  1668  1462             -9.6
30         778   783   882   844   735   709             -9.5
50         961  1014   999   967   982   920             -9.3
100        363   534   641   534   553   485             -9.2
102       1556  1519  1612  1691  1537  1386             -8.8
105       1868  2062  2021  1920  1745  1897             -8.0
111        893   828   880   905   884   765             -7.6
90        1744  1735  1712  1663  1660  1609             -7.3
72        1199  1223  1143  1196  1180  1137             -7.0
5          962   970  1001   995   932   907             -6.5
115       1759  1848  1762  1766  1883  1734             -6.2
81        1433  1476  1563  1494  1545  1392             -5.7
26         680   617   672   708   613   582             -5.7
69        1025  1087  1143  1179  1164  1030             -5.2
14        3058  2872  2920  2857  2743  2728             -5.0
109       1916  1900  1969  2166  2044  1807             -4.9
52        2186  2170  2169  2192  2202  2066             -4.8
45        1432  1280  1181  1133  1146  1220             -4.7
9         1390  1361  1428  1440  1340  1300             -4.5
76         585   637   631   642   625   612             -3.9
10        1046  1056  1091  1121  1031  1022             -3.2
17         991   953  1027  1014   910   927             -2.7
103       1720  1734  1839  1810  1840  1695             -2.2
68         935   950   951   964   947   929             -2.2
1         1438  1413  1434  1385  1240  1383             -2.1
13        2151  2045  2025  2141  2067  2009             -1.8
20         986   864  1028   962   885   851             -1.5
34        1199  1287  1173  1177  1146  1270             -1.3
62        1245  1213  1290  1414  1294  1201             -1.0
6         1531  1513  1601  1714  1566  1498             -1.0
19        1859  1851  2033  2043  1890  1838             -0.7
71        1469  1460  1647  1632  1496  1455             -0.3
75        3122  3420  3764  3873  3754  3417             -0.1
28         897   921   951   920   828   922              0.1
32        1107  1095  1038  1006  1003  1097              0.2
84         993  1058  1041  1071  1065  1065              0.7
47        1970  1996  2138  2144  2033  2022              1.3
43        2329  2380  2435  2477  2455  2431              2.1
106       1445  1493  1608  1661  1561  1532              2.6
60        1327  1323  1447  1411  1454  1374              3.9
18        2356  2198  2315  2284  2391  2283              3.9
24         995   931  1079  1028  1022   979              5.2
78         838   884   940  1007   978   945              6.9
42        1188  1233  1297  1335  1334  1319              7.0
41        1297  1327  1532  1760  1582  1421              7.1
7          707   714   753   714   744   767              7.4
46        1528  1603  1623  1693  1640  1793             11.9
23         902   875  1014  1068  1006   999             14.2
61        1109  1263  1668  1662  1691  1454             15.1
44        1997  2078  2229  2161  2317  2438             17.3
48        1495  1488  1645  1761  1770  1764             18.5
94         913   825   963  1037  1037   988             19.8
25         901   897  1055  1105  1054  1096             22.2
40        1674  1691  1647  1895  1716  2077             22.8
101        625   636   908   838   876   911             43.2


Overall change in felony rate:
2011-2012: -4.0%
2011-2013: -3.5%
2011-2014: 0.5%
2011-2015: 4.5%
~~~



