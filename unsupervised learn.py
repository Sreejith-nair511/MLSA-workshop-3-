# Unsupervised Learning Example
# Group students based on marks (no labels)

marks = [25, 30, 45, 50, 70, 75]

low_group = []
high_group = []

# Simple clustering logic
average = sum(marks) / len(marks)

for mark in marks:
    if mark < average:
        low_group.append(mark)
    else:
        high_group.append(mark)

print("Low scoring group:", low_group)
print("High scoring group:", high_group)
