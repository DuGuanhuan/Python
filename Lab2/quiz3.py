# Header row
header = "Faces".rjust(10) + "Name".center(30) + "Vertices".ljust(10)

# Data rows
data = [
    {"Faces": 4, "Name": "Tetrahedron", "Vertices": 4},
    {"Faces": 6, "Name": "Cube", "Vertices": 8},
    {"Faces": 8, "Name": "Octahedron", "Vertices": 6},
    {"Faces": 12, "Name": "Dodecahedron", "Vertices": 20},
    {"Faces": 20, "Name": "Icosahedron", "Vertices": 12}
]

# Print header
print(header)

# Print data rows
for row in data:
    output = f"{row['Faces']:>10}{row['Name']:^30}{row['Vertices']:<10}"
    print(output)
