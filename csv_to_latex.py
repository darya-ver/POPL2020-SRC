import csv

HEADER = "\\begin{table*}\n" + \
  "\\tiny\n" + \
  "\\caption{\\textsc{Tygar} vs. \\textsc{Petsy}}\n" + \
  "\\label{tab:results}\n" + \
  "\\begin{tabular}{|l |l l| r | r |}\n"

FOOTER = "\end{tabular}\n" + \
  "\end{table*}\n"

# def format_time(t):
#     if t < 0:
#         return '-'
#     else:
#         return '{0:0.2f}'.format(t)

def write_latex():
    '''Generate Latex table from the results dictionary'''
        
    with open("results.tex", 'w') as outfile:
      outfile.write(HEADER)
      outfile.write ('\\hline\n')
      # outfile.write("N & Name & Query   &  Time (s): \\textsc{Tygar}	& Time (s): \\textsc{Petsy} & \\textsc{Petsy} speedup over \\textsc{Tygar} \\\\ \n")
      # outfile.write("N & Name & Query   &  Time (s): \\textsc{Tygar}	& Time (s): \\textsc{Petsy} \\\\ \n")
      outfile.write("N & Name & Query   &  \\textsc{Tygar}	& \\textsc{Petsy} \\\\ \n")
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
          tygar_time = row[2] + " s"
          our_time = row[3] + " s"
          # speedup = row[5][:-2] + "\%"

          table_row = str(line_count - 2) + " & " + name + \
            " & " + query + \
            " & " + tygar_time + \
            " & " + our_time + \
            " \\\\ \n"
            # " & " + speedup + \
          
          if(line_count < 23):
            outfile.write(table_row)
      outfile.write ('\\hline\n')
      outfile.write(FOOTER)

write_latex()