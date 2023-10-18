def generate_large_dataset():
    # Simulating a large dataset
    for i in range(1000000):
        yield i

# Loop through the large dataset using a generator
for data_point in generate_large_dataset():
    # Perform processing on each data_point
    print(data_point)
