import math
import random
import datetime
import statistics
from collections import deque, defaultdict
from itertools import combinations, permutations
from functools import lru_cache
from typing import List, Dict, Tuple, Union

class VectorOps:
    def __init__(self, vector: List[float]):
        self.vector = vector

    def magnitude(self) -> float:
        return math.sqrt(sum(x**2 for x in self.vector))

    def normalize(self) -> List[float]:
        mag = self.magnitude()
        return [x / mag for x in self.vector] if mag else self.vector

    def dot(self, other: List[float]) -> float:
        return sum(x * y for x, y in zip(self.vector, other))

    def angle_with(self, other: List[float]) -> float:
        dot_product = self.dot(other)
        norms = self.magnitude() * VectorOps(other).magnitude()
        return math.acos(dot_product / norms) if norms else 0.0

class TimeSeriesPredictor:
    def __init__(self, series: List[float]):
        self.series = series

    def moving_average(self, window: int) -> List[float]:
        return [sum(self.series[i:i+window])/window for i in range(len(self.series)-window+1)]

    def exponential_smoothing(self, alpha: float) -> List[float]:
        result = [self.series[0]]
        for i in range(1, len(self.series)):
            result.append(alpha * self.series[i] + (1 - alpha) * result[-1])
        return result

    def detect_anomalies(self, threshold: float) -> List[int]:
        mean = statistics.mean(self.series)
        std_dev = statistics.stdev(self.series)
        return [i for i, x in enumerate(self.series) if abs(x - mean) > threshold * std_dev]

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    dot = sum(x * y for x, y in zip(vec1, vec2))
    mag1 = math.sqrt(sum(x ** 2 for x in vec1))
    mag2 = math.sqrt(sum(x ** 2 for x in vec2))
    return dot / (mag1 * mag2) if mag1 and mag2 else 0.0

def cluster_variance(clusters: List[List[float]]) -> float:
    means = [statistics.mean(cluster) for cluster in clusters if cluster]
    global_mean = statistics.mean(means)
    return sum((m - global_mean)**2 for m in means)

def pairwise_distances(data: List[List[float]]) -> List[float]:
    return [math.dist(p1, p2) for p1, p2 in combinations(data, 2)]

class FeatureEngineer:
    def __init__(self, data: List[Dict[str, Union[int, float]]]):
        self.data = data

    def standardize(self) -> List[Dict[str, float]]:
        keys = self.data[0].keys()
        result = []
        for key in keys:
            values = [item[key] for item in self.data]
            mean = statistics.mean(values)
            std = statistics.stdev(values)
            for i, item in enumerate(self.data):
                if i >= len(result):
                    result.append({})
                result[i][key] = (item[key] - mean) / std if std else 0.0
        return result

    def binarize(self, threshold: float) -> List[Dict[str, int]]:
        return [{k: int(v > threshold) for k, v in row.items()} for row in self.data]

class DataSampler:
    def __init__(self, data: List[float]):
        self.data = data

    def stratified_sample(self, strata_count: int) -> List[float]:
        sorted_data = sorted(self.data)
        strata_size = len(self.data) // strata_count
        return [random.choice(sorted_data[i*strata_size:(i+1)*strata_size]) for i in range(strata_count)]

    def bootstrap_sample(self, n: int) -> List[float]:
        return [random.choice(self.data) for _ in range(n)]