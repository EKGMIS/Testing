# Read a .csv file and manipulate the data
# Input data is:
#		Kit Number (across top of corresponding length)
#		Component Number (left column)
#		Qty of Component (grid)
# Conditions:
#		> If component is bagged or bundled, and sufficient qty needed, adj BOM to allow for bagged/bundled qty
#		> If component is non-plastic mfg set WO flag True, else False
# Output data is .csv with cols:
#		Item Num 	Seq		Mat Num		WO		Qty

# Define Functions
def record_parse(rec):
# Markers
	trip = True
	quote = False
	for fld in rec:
# 'trip' means last character was a non-quoted ',' (field delimiter) or first iteration
		if trip:
			if not f == " ":
				fld = f
			trip = False
		else:
# Check ',' field delimiter
			if f == "," and not quote:
				trip = True
			else:
# Set 'quote' flag
				if f == '"':
					if quote:
						quote = False
					else:
						quote = True
# NEXT COMMENT...
				if quote:
					fld += f
				else:
					trip = False
					
					
					
# NEXT COMMENT...
					fld = []
				else
					fld.append(f)
			else
				fld = [f]
			cnt += 1
			print(f)
			fld.append(f)




# Open file 'Test.csv' in the same folder that script is running from
xcsv_file_name = "Test.csv"
xcsv = open(xcsv_file_name, "r")

# Define variables
# *** Debugging ***
dbg = 0

# Data record In
din = []

dbg = 0

# csv 'Cell' range for data (item nums & qtys)
# cel_rng = [3, 22, 0] # Last item ('0') for future use: 'step'

# ***************** ***************** *****************
# Iterate thru data records in File to build matrix of item/material/qty
# *****************
# Read data records into List
for r in xcsv.readlines():
	rec = record_parse(r)
	din.append(rec)
# Parse record into fields

# *** Debugging ***
	print(din)
	if dbg % 3 == 0:
		input("Enter to continue...")
	dbg += 1

print(din)

'''
# ***************** ***************** *****************
# Iterate thru data records in List to build matrix of item/material/qty
# *****************
for i in range(len(din)):
	if i == 0:
# Process record 0 (#1 - Structure size [width] & Base Desc [reset all matrix vars])
		base_size = din[i][0:2]
		par_itm = []
		seq_num = 0
		mat_itm = ""
		rec_itm = []
		mtx_itm = []
		wo_flg = False
		qty_per = [0]
		print("Base Size:", base_size)
	else:
# Separate record into fields
		for c in din[i]:
			rec_itm.append(c)
			print(c)
	print(str(i), rec_itm)

# Identify specific data (Item Num, starts with third)
#		for m in din :
#			rec_itm.append(c)
'''

'''
		if i == 1:
# Process record 1 (#2 - Item Nums [from 2nd delimiter ","])
        	for j in range(3, 22):
# Move Item nums to matrix
				par_itm.append(din[i][j])
			print("Parent Item:", par_itm[j-3])
		else:
# Separate record into fields
			for c in din[range(cel_rng[0]:cel_rng[1]:cel_rng[2])]:
				rec_itm.append(c)
					print(rec_itm)
# Check for 'Headers' (first & third "," delimited fields are null)
		if din[i][0] and din[i][2]:
			seq_num += 10
			mat_itm = din[i][0]
			prt_line = "Proc: " + str(seq_num) + " " + mat_itm
# Process record (Qtys [from 2nd delimiter ","])
			for j in range(3, 22):
				qty_per.append(din[i][j])
				prt_line += " " + str(qty_per[j-3])
# Print record - 
		print(prt_line)

# Pause display every 15 recs
	if i > 1 and i % 15 == 0:
		input("Enter to Continue...")
'''

xcsv.close()

'''
	elif i == 2:
# Process record 2 (#3 - Lengths [from 2nd delimiter ","])
                mat_itm_out = din[i][:12]
                for j in range(3, 22)
			par_itm_out = din[i][j]
		print("Material Item:", mat_itm_out)
'''
