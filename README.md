# UK Election

This started with anecdotal observation I made during the 2015 UK general election. Many, if not most, of the seats in the south of England were not only safe Conservative seats, but Labour didn't even come in second.  Looking back at 2010, I saw that the Liberal Democrats were usually the second party, but by 2015 they had collapsed and were increasingly being replaced by UKIP. Nonetheless, it was clear that for large swaths of the country, especially in the south, the election was not a direct contest between the two major parties.

Was this a general rule? It was hard to tell just by sampling from the map. Even though most of the electoral map in England is blue, that just means Conservative seats dominate by area. I needed the full data to be sure.

The BBC stil has election results online going back at least to 2001. I used the Scrapy package to write scrapers for 2010 and the combined 2015 and 2017 election results. (See the uk2010 and uk2015 folders.) I was only able to find 2015 and 2017 election maps from Ordinance Survey. Overall, my original assessment was borne out for 2010 and 2015, but the snap election of 2017 saw a return to two party competition.

## 2015
From the images below we see that many districts won by the Conservatives, especially in the south, saw the Liberal Democrats or UKIP come in second. In the midlands and the north, there was a more direct contest between Conservatives and Labour, although some more rural northern seats were Labour/UKIP contests.

In Scotland, the Conservatives were only competative in the south and the east. Most contests in the heartland were Scottish Nationalist/Labour battles, and in the far north SNP/Liberal Democrat.

![Alt Text](https://github.com/DanielMorton/ukElection/blob/master/Winning%202015.png)
![Alt Text](https://github.com/DanielMorton/ukElection/blob/master/Second%202015.png)

Although the map looks like a Conservative sweep, in reality this result was barely enough for a majority. The maps also indirectly show population distribution, a large percentage of the English population live in the densely packed pockets of red on the map. London, home to one out of seven people in the UK is barely visible.

## 2017
In 2017, many more contests were straight-up Conservative/Labour. For the first time in decades, more than 80% of the population voted for one of the two major parties. Surprisingly, the Conservatives also had their best results in Scotland since the 1980s, even as they lost their majority. UKIP vanished from first and second place entirely, while the Liberal Democrats remained strong only in the south west and remote parts of Scotland and Wales.

![Alt Text](https://github.com/DanielMorton/ukElection/blob/master/Winner%202017.png)
![Alt Text](https://github.com/DanielMorton/ukElection/blob/master/Second%202017.png)
