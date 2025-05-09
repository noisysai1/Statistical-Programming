# kMeans.py

print("DATA-51100, FALL-2023")
print("Sai Kumar Murarishetti")
print("PROGRAMMING ASSIGNMENT #2")



# Read data from the specified .txt file and convert to a list of floats
data1 = [float(x.rstrip()) for x in open("prog2-input-data.txt")]

# Define the clustering function
def grouping(data):
    # Input for the number of clusters required (k)
    k = int(input("Enter no of clusters required: "))

    # Initialize clusters, centroids, and other variables
    clusters = dict(zip(range(k), [[] for i in range(k)]))
    centroids = dict(zip(range(k), data1[0:k]))
    n_centroids = dict(zip(range(k), data1[0:k]))
    stop = 1
    pa = dict(zip(data, range(len(data))))
    old_centroids = dict(zip(range(k), data1[0:k]))
    iteration = 1

    # Start the main loop
    while stop == 1:
        print(f"iteration --{iteration}")
        clusters = dict(zip(range(k), [[] for i in range(k)]))

        # Iterate through data points and assign them to clusters
        for i in data:
            dist = []

            for p in centroids:
                dist_i = ((centroids[p] - i) ** 2) ** 1 / 2
                dist.append(dist_i)

            minx = min(dist)
            idx = dist.index(minx)
            clusters[idx].append(i)
            pa[i] = idx

        # Print cluster assignments
        for i, v in clusters.items():
            print(i, v)

        # Calculate new centroids
        for q in clusters:
            if len(clusters[q]) > 0:
                x = float(sum(clusters[q]) / len(clusters[q]))
                n_centroids[q] = x

        iteration += 1

        # Check for convergence and update centroids
        try:
            if n_centroids == old_centroids:
                stop = 0
            else:
                old_centroids = centroids
                centroids = n_centroids
        except Exception as e:
            print("An error occurred:", str(e))

    # Print point assignments to clusters
    for keyy, valuee in pa.items():
        print("Point {} in cluster {}".format(keyy, valuee), sep="\n")

    # Write results to an output file
    with open("prog2-output-data.txt", "w") as f:
        for keyy, valuee in pa.items():
            f.write("Point {} in cluster {}".format(keyy, valuee))
            f.write("\n")

# Call the grouping function with the provided data
grouping(data1)