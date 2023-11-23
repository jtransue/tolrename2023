# varnames are:
# o or n = old or new
# group
# shd or leg = should or legal
# act
oldnew = ["o","n"]
should_legal = ["shd","leg"]
group = ["ath","rac","com","mil","gay","mslm"]
act = ["spk","coll","lib","rsrch","comedy","facrec","tap","march","cast","socmed"]

# Create the list of all possible names
names = [a+b+c+d for a in oldnew 
         for b in should_legal 
         for c in group 
         for d in act]

# The list of questions
qual_names = [f"Q{x}_{y}" for x in range(24, 48) for y in range(1, 11)]

drop_questions = ["Q36_10", "Q37_10", "Q38_10", "Q39_10", "Q40_10", "Q41_10"]

# Initialize an empty list to store the generated strings
generated_strings = []
code_lines = []

for name in names:
    for qual in qual_names:
        # if qual in drop_questions:
        #     continue
        
        code_lines.append(f"{name} = {qual} \n")

print(code_lines)
   
# Now, 'generated_strings' contains all the desired strings
# and code_lines has the code ready for Stata
