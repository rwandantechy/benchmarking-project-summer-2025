import time
import psutil
import pandas as pd
from typing import Dict, List
import numpy as np
import os

class Benchmark:
    """Base class for all benchmark tests"""
    
    def __init__(self, name: str):
        self.name = name
        self.results = []
    
    def warmup(self, iterations: int = 3):
        """Run warmup cycles to stabilize measurements"""
        for _ in range(iterations):
            self.run()
    
    def run(self) -> Dict[str, float]:
        """Execute single benchmark iteration"""
        start_time = time.perf_counter()
        start_mem = psutil.Process().memory_info().rss

        # Benchmark-specific logic implemented in child classes
        self.execute()

        end_time = time.perf_counter()
        end_mem = psutil.Process().memory_info().rss

        return {
            'time': end_time - start_time,
            'memory': (end_mem - start_mem) / (1024 * 1024)  # MB
        }
    
    def execute(self):
        """To be implemented by specific benchmarks"""
        raise NotImplementedError

class CPUBenchmark(Benchmark):
    """CPU performance benchmark using matrix operations"""
    
    def __init__(self):
        super().__init__("CPU Matrix Multiplication")
        self.size = 1000  # Matrix size
    
    def execute(self):
        a = np.random.rand(self.size, self.size)
        b = np.random.rand(self.size, self.size)
        np.dot(a, b)

class MemoryBenchmark(Benchmark):
    """Memory bandwidth benchmark"""
    
    def __init__(self, size_mb: int = 100):
        super().__init__("Memory Bandwidth")
        self.size = size_mb * 1024 * 1024  # Convert MB to bytes
    
    def execute(self):
        # Create and process large memory block
        data = bytearray(self.size)
        for i in range(0, self.size, 1024):
            data[i] = i % 256

class DiskIOWorkload(Benchmark):
    """Disk I/O performance benchmark"""
    
    def __init__(self, file_path: str, size_mb: int = 50):
        super().__init__("Disk I/O")
        self.file_path = file_path
        self.size = size_mb * 1024 * 1024
    
    def execute(self):
        # Write test
        with open(self.file_path, 'wb') as f:
            f.write(os.urandom(self.size))
        
        # Read test
        with open(self.file_path, 'rb') as f:
            _ = f.read()

def run_benchmarks(iterations: int, config: Dict) -> pd.DataFrame:
    """
    Execute all benchmarks and collect results
    
    Args:
        iterations: Number of times to repeat each benchmark
        config: Configuration dictionary

    Returns:
        DataFrame containing all benchmark results
    """
    benchmarks = [
        CPUBenchmark(),
        MemoryBenchmark(size_mb=config['memory_test_size']),
        DiskIOWorkload(file_path='data/processed/io_test.bin')
    ]
    
    all_results = []
    
    for benchmark in benchmarks:
        print(f"Running {benchmark.name}...")
        benchmark.warmup()
        for _ in range(iterations):
            result = benchmark.run()
            result['benchmark'] = benchmark.name
            all_results.append(result)
    
    return pd.DataFrame(all_results)
class CPUBenchmark(Benchmark):
    """CPU performance benchmark using matrix operations"""
    
    def __init__(self):
        super().__init__("CPU Matrix Multiplication")
        self.size = 1000  # Matrix size
    
    def execute(self):
        a = np.random.rand(self.size, self.size)
        b = np.random.rand(self.size, self.size)
        np.dot(a, b)

class MemoryBenchmark(Benchmark):
    """Memory bandwidth benchmark"""
    
    def __init__(self, size_mb: int = 100):
        super().__init__("Memory Bandwidth")
        self.size = size_mb * 1024 * 1024  # Convert MB to bytes
    
    def execute(self):
        # Create and process large memory block
        data = bytearray(self.size)
        for i in range(0, self.size, 1024):
            data[i] = i % 256

class DiskIOWorkload(Benchmark):
    """Disk I/O performance benchmark"""
    
    def __init__(self, file_path: str, size_mb: int = 50):
        super().__init__("Disk I/O")
        self.file_path = file_path
        self.size = size_mb * 1024 * 1024
    
    def execute(self):
        # Write test
        with open(self.file_path, 'wb') as f:
            f.write(os.urandom(self.size))
        
        # Read test
        with open(self.file_path, 'rb') as f:
            _ = f.read()
import time
import psutil
import pandas as pd
from typing import Dict, List
import numpy as np
import os 
class Benchmark:
    """Base class for all benchmark tests"""
    
    def __init__(self, name: str):
        self.name = name
        self.results = []
    
    def warmup(self, iterations: int = 3):
        """Run warmup cycles to stabilize measurements"""
        for _ in range(iterations):
            self.run()
    
    def run(self) -> Dict[str, float]:
        """Execute single benchmark iteration"""
        start_time = time.perf_counter()
        start_mem = psutil.Process().memory_info().rss
        
        # Benchmark-specific logic implemented in child classes
        self.execute()
        
        end_time = time.perf_counter()
        end_mem = psutil.Process().memory_info().rss
        
        return {
            'time': end_time - start_time,
            'memory': (end_mem - start_mem) / (1024 * 1024)  # MB
        }
    
    def execute(self):
        """To be implemented by specific benchmarks"""
        raise NotImplementedError

def run_benchmarks(iterations: int, config: Dict) -> pd.DataFrame:
    """
    Execute all benchmarks and collect results
    
    Args:
        iterations: Number of times to repeat each benchmark
        config: Configuration dictionary
        
    Returns:
        DataFrame containing all benchmark results
    """
    benchmarks = [
        CPUBenchmark(),
        MemoryBenchmark(size_mb=config['memory_test_size']),
        DiskIOWorkload(file_path='data/processed/io_test.bin')
    ]
    
    all_results = []
    
    for benchmark in benchmarks:
        print(f"Running {benchmark.name}...")
        benchmark.warmup()
        
        for i in range(iterations):
            result = benchmark.run()
            result.update({
                'benchmark': benchmark.name,
                'iteration': i,
                'timestamp': pd.Timestamp.now()
            })
            all_results.append(result)
    
    return pd.DataFrame(all_results)
