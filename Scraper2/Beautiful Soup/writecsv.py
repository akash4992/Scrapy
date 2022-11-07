 
import csv 
    
# fields = ['Name', 'Branch', 'Year', 'CGPA'] 
# rows = [ ['Nikhil', 'COE', '2', '9.0'], 
#          ['Sanchit', 'COE', '2', '9.1'], 
#          ['Aditya', 'IT', '2', '9.3'], 
#          ['Sagar', 'SE', '1', '9.5'], 
#          ['Prateek', 'MCE', '3', '7.8'], 
#          ['Sahil', 'EP', '2', '9.1']] 
# filename = "university_records.csv"
# with open(filename, 'w') as csvfile: 
#     csvwriter = csv.writer(csvfile) 
        
    
#     csvwriter.writerow(fields) 
        

#     csvwriter.writerows(rows)

# with open('myfile.csv', 'w',newline='') as f:
#     thewriter = csv.writer(f) 
#     thewriter.writerow(['col','col','col'])
#     list1 = ['one','two','three']
#     list2 = ['four','five','six']
#     thewriter.writerow(list1)
#     thewriter.writerow(list2)
# with open('myfile.csv', 'w',newline='') as f:
#     fieldname = ['colum1','colum2','colum3']
#     list1 = ['one','two','three']
#     thewriter = csv.DictWriter(f,fieldnames=fieldname)
#     thewriter.writeheader()
#     for i in list1:
#         # thewriter.writerow({'colum1':list1})
#         thewriter.writerow({'colum2':'two'})
#         thewriter.writerow({'colum3':'three'})

with open('housing.csv', 'w',encoding="utf8",newline='') as f:
    
    thewriter = csv.writer(f)
    header = ['Title','Price','Images',]
    thewriter.writerow(header)
    list1 = 'one','two','three'
    list2 = 'four','five','six'
    list3 = 'seven','eight','nine'
    info = [list1,list3,list3]
    print(info)
    thewriter.writerow(info)