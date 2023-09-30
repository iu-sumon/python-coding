import time

def generate_dataset():
    # Replace this function with your own logic to generate the dataset
    dataset = [1,2,3]  # Placeholder for the generated dataset
    # Your dataset generation code goes here
    return dataset

def main():
    frequency = 1  # Initial frequency (in seconds)
    
    while True:
        dataset = generate_dataset()
        print("Generated dataset:", dataset)
        
        time.sleep(frequency)  # Wait for the specified frequency

# if __name__ == "_main_":
# main()