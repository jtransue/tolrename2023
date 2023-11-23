# varnames are:
# o or n = old or new
# group
# shd or leg = should or legal
# act
import numpy as np

oldnew = ["o","n"]
should_legal = ["shd","leg"]
group = ["ath","rac","com","mil","gay","mslm"]
act = ["spk","coll","lib","rsrch","comedy","facrec","tap","march","cast","socmed"]
qual_names = [
    "Q24_1", "Q24_2", "Q24_3", "Q24_4", "Q24_5", "Q24_6", "Q24_7", "Q24_8", "Q24_9", "Q24_10",
    "Q25_1", "Q25_2", "Q25_3", "Q25_4", "Q25_5", "Q25_6", "Q25_7", "Q25_8", "Q25_9", "Q25_10",
    "Q26_1", "Q26_2", "Q26_3", "Q26_4", "Q26_5", "Q26_6", "Q26_7", "Q26_8", "Q26_9", "Q26_10",
    "Q27_1", "Q27_2", "Q27_3", "Q27_4", "Q27_5", "Q27_6", "Q27_7", "Q27_8", "Q27_9", "Q27_10",
    "Q28_1", "Q28_2", "Q28_3", "Q28_4", "Q28_5", "Q28_6", "Q28_7", "Q28_8", "Q28_9", "Q28_10",
    "Q29_1", "Q29_2", "Q29_3", "Q29_4", "Q29_5", "Q29_6", "Q29_7", "Q29_8", "Q29_9", "Q29_10",
    "Q30_1", "Q30_2", "Q30_3", "Q30_4", "Q30_5", "Q30_6", "Q30_7", "Q30_8", "Q30_9", "Q30_10",
    "Q31_1", "Q31_2", "Q31_3", "Q31_4", "Q31_5", "Q31_6", "Q31_7", "Q31_8", "Q31_9", "Q31_10",
    "Q32_1", "Q32_2", "Q32_3", "Q32_4", "Q32_5", "Q32_6", "Q32_7", "Q32_8", "Q32_9", "Q32_10",
    "Q33_1", "Q33_2", "Q33_3", "Q33_4", "Q33_5", "Q33_6", "Q33_7", "Q33_8", "Q33_9", "Q33_10",
    "Q34_1", "Q34_2", "Q34_3", "Q34_4", "Q34_5", "Q34_6", "Q34_7", "Q34_8", "Q34_9", "Q34_10",
    "Q35_1", "Q35_2", "Q35_3", "Q35_4", "Q35_5", "Q35_6", "Q35_7", "Q35_8", "Q35_9", "Q35_10",
    "Q36_1", "Q36_2", "Q36_3", "Q36_4", "Q36_5", "Q36_6", "Q36_7", "Q36_8", "Q36_9", "Q36_10",
    "Q37_1", "Q37_2", "Q37_3", "Q37_4", "Q37_5", "Q37_6", "Q37_7", "Q37_8", "Q37_9", "Q38_1",
    "Q38_2", "Q38_3", "Q38_4", "Q38_5", "Q38_6", "Q38_7", "Q38_8", "Q38_9", "Q39_1", "Q39_2",
    "Q39_3", "Q39_4", "Q39_5", "Q39_6", "Q39_7", "Q39_8", "Q39_9", "Q40_1", "Q40_2", "Q40_3",
    "Q40_4", "Q40_5", "Q40_6", "Q40_7", "Q40_8", "Q40_9", "Q41_1", "Q41_2", "Q41_3", "Q41_4",
    "Q41_5", "Q41_6", "Q41_7", "Q41_8", "Q41_9", "Q42_1", "Q42_2", "Q42_3", "Q42_4", "Q42_5",
    "Q42_6", "Q42_7", "Q42_8", "Q42_9", "Q42_10", "Q43_1", "Q43_2", "Q43_3", "Q43_4", "Q43_5",
    "Q43_6", "Q43_7", "Q43_8", "Q43_9", "Q43_10", "Q44_1", "Q44_2", "Q44_3", "Q44_4", "Q44_5",
    "Q44_6", "Q44_7", "Q44_8", "Q44_9", "Q44_10", "Q45_1", "Q45_2", "Q45_3", "Q45_4", "Q45_5",
    "Q45_6", "Q45_7", "Q45_8", "Q45_9", "Q45_10", "Q46_1", "Q46_2", "Q46_3", "Q46_4", "Q46_5",
    "Q46_6", "Q46_7", "Q46_8", "Q46_9", "Q46_10", "Q47_1", "Q47_2", "Q47_3", "Q47_4", "Q47_5",
    "Q47_6", "Q47_7", "Q47_8", "Q47_9", "Q47_10"
]

# Provided lists
oldnew = ["o", "n"]
group = ["ath", "rac", "com", "mil", "gay", "mslm"]
should_legal = ["shd", "leg"]
act = ["spk", "coll", "lib", "rsrch", "comedy", "facrec", "tap", "march", "cast", "socmed"]

# Initialize an empty list to store the generated strings
generated_strings = []
code_lines = []

drop_questions = ["Q36_10", "Q37_10", "Q38_10", "Q39_10", "Q40_10", "Q41_10"]
qual_index = -1

# Nested loops to generate strings
for on in oldnew:
    for sl in should_legal:
        for gr in group:
            for ac in act:
                if qual_names[qual_index] in drop_questions:
                    continue

                # Create the varname string by concatenating elements
                varname = on + sl + gr + ac
                
                # Create the full string with "clonevar" and varname
                full_string = "clonevar " + varname
                
                # Append the generated string to the list
                generated_strings.append(full_string)
                
                # Finish the clonevar command (may combine later)
                # for qn in qual_names:
                code_line = full_string + " = " + qual_names[qual_index] + "\n"
                code_lines.append(code_line)
print(code_lines)
                    
                    
# Now, 'generated_strings' contains all the desired strings
# and code_lines has the code ready for Stata
