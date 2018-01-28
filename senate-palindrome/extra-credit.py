#!/usr/bin/python3

import requests
from html.parser import HTMLParser
import re

class VoteParser(HTMLParser):

    # SenateNumber
    senateNumber=None

    # The vote entry looks like something like this.
    # '10\xa0(68-27)'
    # The \x comes from the &nbsp;
    # For now, I'll leave the `.*` in the regex even though I could write something more accuate.
    voteRegex=r"(\d+.*\(\d+-\d+\))"

    votes=list()

    # the vote content is only ever in the "td" tags.
    # Reduce the search space to vote content only
    whatWeWant=False
    def handle_starttag(self, startTag, attrs):
        if startTag=="td": self.whatWeWant=True
    def handle_endtag(self, startTag):
        if startTag=="td": self.whatWeWant=False

    def handle_data(self, data):
        if not self.whatWeWant: return

        if re.search(self.voteRegex, data):
            match=re.search(self.voteRegex, data)
            vote=self.senateNumber+" "+match.group(0)
            self.votes.append(vote)

    def setYear(self, senateNumber): self.senateNumber=senateNumber

    def displayPalindromes(self):

        printString="Senate number {} in year {} had a palindrome vote ({}-{}) on vote number {}."

        for vote in self.votes:
            match=re.search(r"(\d+)-(\d+) (\d+).*\((\d+)-(\d+)\)", vote)
            congress, year, voteNo, yea, nay=match.groups()

            if self.isPalindrome(yea, nay):
                print(printString.format( congress, year, yea, nay, voteNo))

    def isPalindrome(self, yea, nay):
        both=str(yea)+str(nay)
        rBoth=both[::-1]

        return both == rBoth


#set up parser
parser=VoteParser(convert_charrefs=True)

baseURL="https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_{}_{}.htm"
senateID="{}-{}"
for senate in range(101,116):
    for year in [1,2]:
        parser.setYear(senateID.format(senate,year))
        url=baseURL.format(senate, year)

        page=requests.get(url)
        if page.status_code != 200:
            print("Error getting page {}".format(url))
            exit(1)

        print("Processing page {}".format(url))
        parser.feed(str(page.content))

parser.displayPalindromes()

