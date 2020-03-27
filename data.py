import numpy as np

dates = np.array([  '2020-03-08',
                    '2020-03-09',
                    '2020-03-10',
                    '2020-03-11',
                    '2020-03-12',
                    '2020-03-13',
                    '2020-03-14',
                    '2020-03-15',
                    '2020-03-16',
                    '2020-03-17',
                    '2020-03-18',
                    '2020-03-19',
                    '2020-03-20',
                    '2020-03-21',
                    '2020-03-22',
                    '2020-03-23',
                    '2020-03-24',
                    '2020-03-25',
                    '2020-03-26'
                 ], dtype='datetime64')

total_cases = np.array([0,2,2,6,10,21,26,33,46,49,58,67,75,84,95,116,124,132,146], dtype='intc')
##new cases each day
daily_diff = np.insert(np.diff(total_cases),0,total_cases[0],axis=0)
daily_cases = daily_diff
daily_percentage_increase = np.diff(total_cases) / total_cases[1:] * 100



from_hospitals = np.array([0,
                           0,#  09/3/2020 
                           0,
                           0,
                           0,
                           0,
                           0,
                           0,
                           11, # 16/3/2020
                           0,
                           0,
                           0,
                           3,
                           1,
                           4,
                           3, #23/3/20
                           0,
                           0,
                           1
                          ], 
                          dtype='intc') #includes medical personel working there

days_from_onset = np.array([i for i in range(-1, len(dates)-1)])

from_travel = np.array([ 0,
                        2,#  09/3/2020 
                        0,
                        2,
                        4,
                        4,
                        2,
                        5,
                        2, # 16/3/2020
                        1,
                        3,
                        3,
                        0,
                        5,
                        4,
                        6,   #23/3/20
                        2,
                        2,
                        4
                       ],
                      dtype='intc')


#not accounted from the above
new_cases = np.array([0, #  09/3/2020
                      0,
                      0,
                      2,
                      0,
                      7,
                      3,
                      2,
                      0, # 16/3/2020
                      2,
                      6,
                      6,
                      5,
                      3,
                      3,
                      12, #23/3/20
                      6,
                      6,
                      9
                     ],
                     dtype='intc')


##from quarantine includes people that were put in guarantin due to close contacts with known cases
dates_of_preventive_measures = np.array(['2020-03-14', '2020-03-24'], dtype='datetime64')

social_distancing = np.zeros(len(dates))
social_distancing[dates >= dates_of_preventive_measures[0]] = social_distancing[dates >= dates_of_preventive_measures[0]] + 1

lockdown = np.zeros(len(dates))
lockdown[dates >=dates_of_preventive_measures[1]] = lockdown[dates >= dates_of_preventive_measures[1]] + 2


# MEASURES TAKEN

# 14-3-2020 Cafes, restaurants, pubs etc close 
# 24-3-1010 LOCKDOWN

measures = np.zeros(len(dates))
for d in dates_of_preventive_measures:
    #print(d)
    #print(np.where(dates >= d))
    measures[dates >= d] = measures[dates>=d] + 1
