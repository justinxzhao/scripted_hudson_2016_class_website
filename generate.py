classmates = open('classmates.tsv').readlines()

for c in classmates:
  c = c.replace("\t" , " ")
  c = c.replace("\n" , "")
  print "<h3>" + c + "</h3>"
  print "<p>INSERT FUN FACT HERE.</p>"

