# Election Analysis using Python
## Overview of Election Audit
A Colorado Board of Elections employee has given the following tasks to complete audit of a recent local congressional election.
1.	Calculate the total number of votes cast.
2.	Get the complete list of county name in the precinct and the corresponding count of votes and percentage of votes of each county
3.	Get the county name with the highest vote turnout
4.	Get a complete list of candidates who received votes.
5.	Calculate the total number of votes each candidate received.
6.	Calculate the percentage of votes each candidate won.
7.	Determine the winner of the election based on popular vote.
## Election-Audit Results
The analysis of the election show that:
-	There were 369,711 votes cast in the election.
-	The counties were:
Jefferson with 10.5% of the total votes and 38,855 of votes
Denver with 82.8% of the total votes and 306,055 of votes
Arapahoe with 6.7% of the total votes and 24,801 of votes
-	The candidates were:
Charles Casper Stockham
Diana DeGette
Raymon Anthony Doane
-	The candidate results were:
Charles Casper Stockham received 23.0% of the vote and 85,213 of votes
Diana DeGette received 73.8% of the vote and 272,892 of votes
Raymon Anthony Doane received 3.1% of the vote and 11,606 of votes
-	The winner of the election was:
Diana DeGette, who received 73.8% of the vote and 272,892 of votes
## Election-Audit Summary
The solution provide in the current script can be leveraged largely in any board of election audit which not only provide the accurate details and summary report but, accelerate the process of creating the report with little or no modification.
Following are the two examples where the current script can be used with small modifications:
1.	With small difference in Input (.csv) file): in case the input .csv file is structurally little different; we need to correctly reference the appropriate column index to refer candidate and/or county name to reflect correct result.
2.	Requested different report format: in case the report format needs to modify (e.g., candidate summary), the section at the end of the script (winning_candidate_summary) can be changed to meet the requirement
