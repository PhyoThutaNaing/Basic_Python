import matplotlib.pyplot as plt
import random

# Generate marks for 60 students (0–20)
marks = [random.randint(0, 20) for _ in range(60)]

# Plot histogram
plt.hist(marks, bins=10)

# Labels and title
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Histogram of Student Marks")

# Show graph
plt.show()
