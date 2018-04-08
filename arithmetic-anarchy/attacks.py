from datetime import timedelta, date

#store when all of the attacks happen by year
attacks=dict()
for year in range(2000, 2099+1): attacks[year]=list()

# assuming last attack is Dec 31st, 1999
# doesn't affect results
longestGapStart=longestGapEnd=lastAttack=date(1999, 12, 31)
longestGap=timedelta(days=0)

day=timedelta(days=1)
today=date(1999,12,31)
end=date(2099,12,31)

while today <= end:

    today+=day

    # attackers attack when number of month times day of the month
    # equals the last two digits of the year
    # e.g. January 1st, 2001 and March 6th, 2018

    # if there's not an attack, move along
    if not today.month*today.day==today.year%100: continue

    # Calculation gap between last attack and today's attack
    gap=today-lastAttack
    if longestGap < gap:
        longestGap=gap
        longestGapEnd=today
        longestGapStart=lastAttack

    lastAttack=today

    # Log an attack for this year
    attacks[today.year].append(today)


# calculate results
mostVandalizedVal=len(max(attacks.values(), key=lambda x: len(x)))
mostVandalizedYears=sorted([year for year, attack in attacks.items() if len(attack)==mostVandalizedVal])

leastVandalizedVal=len(min(attacks.values(), key=lambda x: len(x)))
leastVandalizedYears=sorted([year for year, attack in attacks.items() if len(attack)==leastVandalizedVal])

totalAttacks=sum(len(a) for a in attacks.values())


# print results
print("There were {} total attacks.".format(totalAttacks))
print()

print("Years with the least ({}) numbers of attacks:".format(leastVandalizedVal))
print(leastVandalizedYears)
print()

print("Years with the most ({}) numbers of attacks:".format(mostVandalizedVal))
print(mostVandalizedYears)

print()
print("They happened on the following dates:")
for year in mostVandalizedYears:
    for attack in attacks[year]:
        print(attack, end=" ")
print()
print()

print("The longest gap between attacks was {} days. It started on {} and ended on {}.".format(longestGap.days, longestGapStart, longestGapEnd))
