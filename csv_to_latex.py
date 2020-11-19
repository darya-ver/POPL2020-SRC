import csv

HEADER = "\\begin{table*}\n" + \
  "\\tiny\n" + \
  "\\caption{TYGAR vs. Our tool}\n" + \
  "\\label{tab:results}\n" + \
  "\\begin{tabular}{c c c | r | r | r}\n"

FOOTER = "\end{tabular}\n" + \
  "\end{table*}\n"

# def format_time(t):
#     if t < 0:
#         return '-'
#     else:
#         return '{0:0.2f}'.format(t)

# TODO: format percentage and get corret set of tests

def write_latex():
    '''Generate Latex table from the results dictionary'''
        
    with open("results.tex", 'w') as outfile:
      outfile.write(HEADER)
      outfile.write ('\\hline\n')
      outfile.write("N & Name & Query   &  Time (s): TYGAR	& Time (s): Ours & Speedup \\\\ \n")
      outfile.write ('\\hline\n')
      with open('results.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
          line_count += 1
          if(line_count <= 2):
            continue

          name = row[0]
          query = row[1]
          tygar_time = row[2]
          our_time = row[3]
          speedup = row[4]

          table_row = str(line_count - 2) + " & " + name + " & " + \
            query + " & " + \
            tygar_time + " & " + \
            our_time + " & " + \
            speedup + " \\\\ \n"
          
          if(line_count < 23):
            outfile.write(table_row)
      outfile.write ('\\hline\n')
      outfile.write(FOOTER)

write_latex()