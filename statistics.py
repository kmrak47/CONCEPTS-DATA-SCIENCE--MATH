
#central tendency

def find_mean(data):
    return sum(data)/len(data)

def find_median(data):
    sorted_data = sorted(data)
    n=len(data)

    if n % 2 ==0:
        return (sorted_data[n//2 -1]+sorted_data[n//2])/2
    else:
        return sorted_data[n//2]
    

def find_mode(data):
    freq = {}
    for num in data:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    return max(freq, key=freq.get)

def find_variance(data):
    mean = sum(data)/len(data)
    squared_diff = []
    for num in data :
        squared_diff.append((num-mean)**2)
    variance = sum(squared_diff)/len(data)
    return variance

def find_standard_variance(data):
    mean = sum(data)/len(data)
    squared_diff = []
    for num in data:
        squared_diff.append((num-mean)**2)
    variance = sum(squared_diff)/len(data)
    standard_deviation = variance**0.5
    return standard_deviation


#Note in case of sample data n becomes n-1

#position measures
def find_percentile_value(data,percentile):
    data = sorted(data)
    n = len(data)
    index = (percentile/100)*(n-1)
    lower = int(index)
    upper = lower+1
    if upper >= n:
        return data[lower]
    fraction = index - lower
    result = data[lower] + (data[upper] -data[lower])*fraction
    return result

def find_percentile_rank(data,value):
    count = 0
    for num in data:
        if num< value:
            count +=1
    percentile = (count/len(data))*100
    return percentile

def quartiles(data):
    data1 = sorted(data)
    n = len(data)
    q1 = find_percentile_value(data1,25)
    q3 = find_percentile_value(data1,75)
    iqr = q3-q1
    lower_fence = q1-(1.5*iqr)
    upper_fence = q3 + (1.5*iqr)
    min = data1[0]
    median = find_median(data1)
    max = data1[-1]
    return min,q1,median,q3,max,iqr,lower_fence,upper_fence

#outliers = [x for x in data if x< lower_fence or x>upper_fence ]

