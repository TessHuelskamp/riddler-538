#!/usr/bin/python3

import requests
from html.parser import HTMLParser
import re

class voteStruct():
    yea=0
    nay=0
    senateNo=0
    yearNo=0
    voteNo=0

class VoteParser(HTMLParser):
    # ID for which senate a vote belonged to
    senateNo=None
    yearNo=None

    # A list of all the votes we found
    votes=list()

    def setSenate(self, senate): self.senateNo=senate
    def setYear(self, year): self.yearNo=year


    # the vote content is only ever in the "td" tags.
    # Reduce the search space to vote content only
    whatWeWant=False
    def handle_starttag(self, startTag, attrs):
        if startTag=="td": self.whatWeWant=True
    def handle_endtag(self, startTag):
        if startTag=="td": self.whatWeWant=False

    # The vote entry looks like something like this.
    # '10\xa0(68-27)'
    # The \x comes from the &nbsp;
    # For now, I'll leave the `.*` in the regex even though I could write something more accuate.
    voteRegex=r"(\d+).*\((\d+)-(\d+)\)"
    def handle_data(self, data):
        if not self.whatWeWant: return

        if re.search(self.voteRegex, data):
            match=re.search(self.voteRegex, data)

            #create a new vote entry and store it for later
            newVote=voteStruct()
            newVote.voteNo, newVote.yea, newVote.nay = match.groups()
            newVote.yearNo=self.yearNo
            newVote.senateNo=self.senateNo
            self.votes.append(newVote)


    def displayPalindromes(self):

        printString="Senate number {} in year {} had a palindrome vote ({}-{}) on vote number {}."

        for vote in self.votes:

            if self.isPalindrome(vote.yea, vote.nay):
                print(printString.format( vote.senateNo, vote.yearNo, vote.yea, vote.nay, vote.voteNo))

    def isPalindrome(self, yea, nay):
        both=str(yea)+str(nay)
        rBoth=both[::-1]

        return both == rBoth


#set up parser
parser=VoteParser(convert_charrefs=True)

baseURL="https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_{}_{}.htm"

#gather all data
for senate in range(101,116):
    for year in [1,2]:
        parser.setSenate(senate)
        parser.setYear(year)

        url=baseURL.format(senate, year)

        page=requests.get(url)
        if page.status_code != 200:
            print("Error getting page {}".format(url))
            exit(1)

        print("Processing page {}".format(url))
        parser.feed(str(page.content))

parser.displayPalindromes()
