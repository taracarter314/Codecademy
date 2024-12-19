tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

# Write your code below: 
def assign_table(table_number, name, vip_status=False): # adding False here sets a default of False for vip_status so we don't have to add this parameter unless the guest is a vip_tatus needs to be True

# assigning customers to their table_name, name, and vip_status
  tables[table_number] = [name, vip_status]

#use of positional argument
assign_table(6, 'Yoni', False )
#print(tables)

#use of keyword argument
assign_table(table_number=3, name='Martha', vip_status=True)
#print(tables)

#see comment at def assign_tables coupled with default value practice below
assign_table(4, 'Karla')
#print(tables)

#new information at table 6 gets replaced
assign_table(6, 'Tara', True)
#print(tables)

#move Yoni to table 2
assign_table(2, 'Yoni')
print(tables)
