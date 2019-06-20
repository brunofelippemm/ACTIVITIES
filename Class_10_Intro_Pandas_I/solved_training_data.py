# Collecting a summary of all numeric data
training_data.describe()

# Finding the names of the trainers
training_data["Trainer"].unique()

# Finding how many students each trainer has
training_data["Trainer"].value_counts()

# Finding the average weight of all students
training_data["Weight"].mean()

# Finding the combined weight of all students
training_data["Weight"].sum()

# Converting the membership days into weeks and then adding a column to the DataFrame
weeks = training_data["Membership (Days)"]/7
training_data["Membership (Weeks)"] = weeks

training_data.head()