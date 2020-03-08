# this script will handle the filtering of the websites
# scraped in scrapeAtt

import handleData
import pandas as pd

# note: I only want this dataset to include regular season
# games, so the months of May and June will not be included

df1 = handleData.filterHTML('www.basketball-reference.com-october.html')
df2 = handleData.filterHTML('www.basketball-reference.com-november.html')
df3 = handleData.filterHTML('www.basketball-reference.com-december.html')
df4 = handleData.filterHTML('www.basketball-reference.com-january.html')
df5 = handleData.filterHTML('www.basketball-reference.com-february.html')
df6 = handleData.filterHTML('www.basketball-reference.com-march.html')
df7 = handleData.filterHTML('www.basketball-reference.com-april.html')

frames = [df1, df2, df3, df4, df5, df6, df7]
result = pd.concat(frames)
print(result)


