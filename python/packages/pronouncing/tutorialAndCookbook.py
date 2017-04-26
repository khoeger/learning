import pronouncing

print(pronouncing.phones_for_word("permit"))

pronunciation_list= pronouncing.phones_for_word("programming")
count_sylls = pronouncing.syllable_count(pronunciation_list[0])
print(count_sylls)
