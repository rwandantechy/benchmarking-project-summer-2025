#!/usr/bin/env python3
"""
Main benchmarking execution script
"""
from src.benchmark import run_benchmarks
from src.config import load_config
import logging
import argparse

def setup_logging():
    """Configure logging for the benchmark"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('data/processed/benchmark.log'),
            logging.StreamHandler()
        ]
    )

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Run system benchmarks')
    parser.add_argument('--iterations', type=int, default=5,
                       help='Number of benchmark iterations')
    parser.add_argument('--output', type=str, 
                       default='data/processed/results.csv',
                       help='Output file path')
    return parser.parse_args()

if __name__ == "__main__":
    setup_logging()
    args = parse_args()
    config = load_config()
    
    logger = logging.getLogger(__name__)
    logger.info("Starting benchmark suite")
    
    results = run_benchmarks(
        iterations=args.iterations,
        config=config
    )
    
    results.to_csv(args.output, index=False)
    logger.info(f"Benchmark completed. Results saved to {args.output}")
