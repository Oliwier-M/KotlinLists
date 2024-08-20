import numpy as np
import matplotlib.pyplot as plt


def generate_height_data(size=1000, mean=170, std_dev=10):
    """
    Generate a dataset of heights from a normal distribution.

    Parameters:
    - size: Number of data points in the dataset (default is 1000).
    - mean: Mean of the normal distribution (default is 170).
    - std_dev: Standard deviation of the normal distribution (default is 10).

    Returns:
    - numpy.ndarray: An array containing the generated heights.
    """

    if not isinstance(size, int) or not isinstance(mean,int) or not isinstance(std_dev, int):
        raise TypeError

    if size <= 0:
        raise ValueError("size must be positive")

    if mean < 0:
        raise ValueError("mean average must be positive or 0")

    if std_dev < 0:
        raise ValueError("std_dev must be positive or 0")

    # Generate heights from a normal distribution
    heights = np.random.normal(loc=mean, scale=std_dev, size=size)
    return heights


data = generate_height_data()
print(data)


def descriptive_statistics(height_data):
    """

    :param height_data:
    :return mean_avg:
    """
    mean_avg = np.mean(height_data)
    median = np.median(height_data)
    standard_dev = np.std(height_data)

    return mean_avg, median, standard_dev


def visualise_histogram(height_data):
    plt.hist(height_data)
    plt.title('Height distribution histogram')
    plt.xlabel('height (cm)')
    plt.ylabel('frequency')
    plt.show()


def calculate_percentiles(height_data):
    percentile_25 = np.percentile(height_data, 25)
    percentile_50 = np.percentile(height_data, 50)
    percentile_75 = np.percentile(height_data, 75)

    print("percentile 25: " + percentile_25)
    print("percentile 50: " + percentile_50)
    print("percentile 75: " + percentile_75)

def identify_outliers(height_data):
    Q1 = np.percentile(height_data, 25)
    Q3 = np.percentile(height_data, 75)

    IQR = Q3 - Q1
    lower_boundary = Q1 - 1.5 * IQR
    upper_boundary = Q3 + 1.5 * IQR

    outliers = []

    # check what lies below upper and lower boundary
    for height in height_data:
        if height < lower_boundary or height > upper_boundary:
            outliers.append(height)

    print("upper boundary: " + str(upper_boundary))
    print("lower boundary: " + str(lower_boundary))
    print("outliers: " + str(outliers))


def random_sampling(height_data):
    heights = np.random.choice(height_data, size=50,replace=False)
    return heights


# don't understand
# def hypothesis_testing(data, null_hypothesis_mean=165):

def calculate_probability(data, threshold_height=180):
    counter = 0
    all = 0

    for height in data:
        all += 1
        if height > threshold_height:
            counter += 1

    probability = counter / all
    print("probability of choosing a height higher than ", threshold_height, "is equal to: ", probability)
    return probability


stats = descriptive_statistics(data)
print(stats)
visualise_histogram(data)
identify_outliers(data)
calculate_probability(data)


    # # calculate mean evg
    # sum = 0
    # counter = 0
    #
    # for height in height_data:
    #     sum += height
    #     counter += 1
    #
    # mean_avg = sum/counter
    #
    # # calculate median
    # height_data.sort()
    # median = 0
    #
    # if counter % 2 == 0:     #if it's even
    #     nr = counter/2
    #
    # else:
    #     c = counter - 1
    #     nr = c/2
    #     median = height_data[nr]









