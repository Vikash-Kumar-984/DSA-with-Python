expenses = { "January":2200, 
             "February":2350,
             "March":2600,
             "April":2130,
             "May":2190
           }

# 1. In Feb, how many dollars you spent extra compare to January?
diff=expenses["February"]-expenses["January"]
print(diff)
print("The amount money is spent more in February than January: ",diff)

# 2. Find out your total expense in first quarter (first three months) of the year.
sumofquarter= expenses["January"] + expenses["February"] + expenses["March"]
print("The sum of quarter expenses: ",sumofquarter)

# 3. Find out if you spent exactly 2000 dollars in any month
if(expenses["January"]== 2000 or expenses["February"]== 2000 or expenses["March"] == 2000 or expenses["April"]== 2000 or expenses["May"] == 2000):
          print("you spent exactly 2000 dollars in any month")
else:
    print("you spent NOT exactly 2000 dollars in any month")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list    
expenses.update({"June":1980})
print(expenses)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
expenses["April"]=expenses["April"]-200
print(expenses)

