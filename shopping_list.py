import csv

spirits_count = {}
mixers_count = {}
syrups_count = {}
bitters_count = {}
garnishes_count = {}
other_count = {}
with open('recipes.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		if row[0] == "#": continue
		primary = row[3].split(",")
		for spirit in primary:
			spirit_trimmed = spirit.strip()
			if not spirit_trimmed: continue
			spirits_count[spirit_trimmed] = spirits_count.get(spirit_trimmed, 0) + 1

		secondary = row[4].split(",")
		for spirit in secondary:
			spirit_trimmed = spirit.strip()
			if not spirit_trimmed: continue
			spirits_count[spirit_trimmed] = spirits_count.get(spirit_trimmed, 0) + 1

		mixers = row[5].split(",")
		for mixer in mixers:
			mixer_trimmed = mixer.strip()
			if not mixer_trimmed: continue
			mixers_count[mixer_trimmed] = mixers_count.get(mixer_trimmed, 0) + 1

		syrups = row[6].split(",")
		for syrup in syrups:
			syrup_trimmed = syrup.strip()
			if not syrup_trimmed: continue
			syrups_count[syrup_trimmed] = syrups_count.get(syrup_trimmed, 0) + 1

		bitters = row[7].split(",")
		for bitter in bitters:
			bitter_trimmed = bitter.strip()
			if not bitter_trimmed: continue
			bitters_count[bitter_trimmed] = bitters_count.get(bitter_trimmed, 0) + 1

		garnishes = row[8].split(",")
		for garnish in garnishes:
			garnish_trimmed = garnish.strip()
			if not garnish_trimmed: continue
			garnishes_count[garnish_trimmed] = garnishes_count.get(garnish_trimmed, 0) + 1

		others = row[9].split(",")
		for other in others:
			other_trimmed = other.strip()
			if not other_trimmed: continue
			other_count[other_trimmed] = other_count.get(other_trimmed, 0) + 1

print("Spirits")
for spirit, count in sorted(spirits_count.items(), key=lambda item: -item[1]):
	print(f"\t{spirit}: {count}")

print("\n")
print("Mixers")
for mixer, count in sorted(mixers_count.items(), key=lambda item: -item[1]):
	print(f"\t{mixer}: {count}")

print("\n")
print("Syrups")
for syrup, count in sorted(syrups_count.items(), key=lambda item: -item[1]):
	print(f"\t{syrup}: {count}")

print("\n")
print("Bitters")
for bitter, count in sorted(bitters_count.items(), key=lambda item: -item[1]):
	print(f"\t{bitter}: {count}")

print("\n")
print("Garnishes")
for garnish, count in sorted(garnishes_count.items(), key=lambda item: -item[1]):
	print(f"\t{garnish}: {count}")

print("\n")
print("Other")
for other, count in sorted(other_count.items(), key=lambda item: -item[1]):
	print(f"\t{other}: {count}")