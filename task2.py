"""
Task 2: 3D Printer Queue Optimization using Greedy Algorithm

This module optimizes a 3D printing queue by considering job priorities
and printer constraints (max volume and max items per batch).

Priority levels:
    1 - Highest priority (thesis/diploma projects)
    2 - Medium priority (lab work)
    3 - Lowest priority (personal projects)
"""

from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    """Represents a 3D printing job."""
    id: str
    volume: float
    priority: int
    print_time: int

    def __repr__(self):
        return f"PrintJob({self.id}, vol={self.volume}, pri={self.priority}, time={self.print_time})"


@dataclass
class PrinterConstraints:
    """Represents the constraints of the 3D printer."""
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Optimize the 3D printing queue based on priorities and printer constraints.

    The greedy algorithm:
    1. Sort jobs by priority (highest first)
    2. Within same priority, sort by volume (smaller first for better packing)
    3. Group jobs into batches respecting max_volume and max_items constraints
    4. Calculate total time as sum of batch times (max time in each batch)

    Args:
        print_jobs: List of dictionaries with job information
                   Each dict contains: id, volume, priority, print_time
        constraints: Dictionary with max_volume and max_items

    Returns:
        Dictionary with:
            - print_order: List of job IDs in execution order
            - total_time: Total time in minutes to complete all jobs

    Examples:
        >>> jobs = [
        ...     {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        ...     {"id": "M2", "volume": 150, "priority": 2, "print_time": 90}
        ... ]
        >>> constraints = {"max_volume": 300, "max_items": 2}
        >>> result = optimize_printing(jobs, constraints)
        >>> result['print_order']
        ['M1', 'M2']
    """
    jobs_with_index = [(i, PrintJob(**job)) for i, job in enumerate(print_jobs)]
    printer = PrinterConstraints(**constraints)

    jobs_with_index.sort(key=lambda x: (x[1].priority, x[0]))
    jobs = [job for _, job in jobs_with_index]

    batches = []
    current_batch = []
    current_volume = 0
    current_max_time = 0

    for job in jobs:
        can_fit_volume = current_volume + job.volume <= printer.max_volume
        can_fit_items = len(current_batch) < printer.max_items

        if current_batch and (not can_fit_volume or not can_fit_items):
            batches.append({
                'jobs': current_batch,
                'time': current_max_time
            })
            current_batch = []
            current_volume = 0
            current_max_time = 0

        current_batch.append(job)
        current_volume += job.volume
        current_max_time = max(current_max_time, job.print_time)

    if current_batch:
        batches.append({
            'jobs': current_batch,
            'time': current_max_time
        })

    print_order = []
    total_time = 0

    for batch in batches:
        for job in batch['jobs']:
            print_order.append(job.id)
        total_time += batch['time']

    return {
        "print_order": print_order,
        "total_time": total_time
    }


def test_printing_optimization():
    """Test the printing optimization with various scenarios."""

    print("=" * 60)
    print("Test 1: Models with same priority")
    print("=" * 60)
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Jobs: {test1_jobs}")
    print(f"Constraints: max_volume={constraints['max_volume']}, max_items={constraints['max_items']}")
    print(f"\nResult:")
    print(f"  Print order: {result1['print_order']}")
    print(f"  Total time: {result1['total_time']} minutes")
    print(f"\nExplanation:")
    print(f"  Batch 1: M1 (vol=100) + M2 (vol=150) = 250 <= 300")
    print(f"           Time = max(120, 90) = 120 minutes")
    print(f"  Batch 2: M3 (vol=120)")
    print(f"           Time = 150 minutes")
    print(f"  Total: 120 + 150 = 270 minutes")

    print("\n" + "=" * 60)
    print("Test 2: Models with different priorities")
    print("=" * 60)
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]

    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Jobs: {test2_jobs}")
    print(f"Constraints: max_volume={constraints['max_volume']}, max_items={constraints['max_items']}")
    print(f"\nResult:")
    print(f"  Print order: {result2['print_order']}")
    print(f"  Total time: {result2['total_time']} minutes")
    print(f"\nExplanation:")
    print(f"  Priority order: M2 (pri=1), M1 (pri=2), M3 (pri=3)")
    print(f"  Batch 1: M2 (vol=150, pri=1) + M1 (vol=100, pri=2) = 250 <= 300")
    print(f"           Time = max(90, 120) = 120 minutes")
    print(f"  Batch 2: M3 (vol=120, pri=3)")
    print(f"           Time = 150 minutes")
    print(f"  Total: 120 + 150 = 270 minutes")

    print("\n" + "=" * 60)
    print("Test 3: Exceeding volume constraints")
    print("=" * 60)
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Jobs: {test3_jobs}")
    print(f"Constraints: max_volume={constraints['max_volume']}, max_items={constraints['max_items']}")
    print(f"\nResult:")
    print(f"  Print order: {result3['print_order']}")
    print(f"  Total time: {result3['total_time']} minutes")
    print(f"\nExplanation:")
    print(f"  M1 (vol=250) + M2 (vol=200) = 450 > 300 (exceeds limit)")
    print(f"  Batch 1: M1 (vol=250) - prints alone")
    print(f"           Time = 180 minutes")
    print(f"  Batch 2: M2 (vol=200) - prints alone")
    print(f"           Time = 150 minutes")
    print(f"  Batch 3: M3 (vol=180, pri=2) - prints alone")
    print(f"           Time = 120 minutes")
    print(f"  Total: 180 + 150 + 120 = 450 minutes")

    print("\n" + "=" * 60)
    print("Test 4: All jobs fit in one batch")
    print("=" * 60)
    test4_jobs = [
        {"id": "M1", "volume": 80, "priority": 1, "print_time": 60},
        {"id": "M2", "volume": 70, "priority": 1, "print_time": 50}
    ]

    result4 = optimize_printing(test4_jobs, constraints)
    print(f"Jobs: {test4_jobs}")
    print(f"Constraints: max_volume={constraints['max_volume']}, max_items={constraints['max_items']}")
    print(f"\nResult:")
    print(f"  Print order: {result4['print_order']}")
    print(f"  Total time: {result4['total_time']} minutes")
    print(f"\nExplanation:")
    print(f"  All jobs fit in one batch: vol=80+70=150 <= 300, items=2 <= 2")
    print(f"  Time = max(60, 50) = 60 minutes")

    print("\n" + "=" * 60)
    print("Test 5: Max items constraint exceeded")
    print("=" * 60)
    test5_jobs = [
        {"id": "M1", "volume": 50, "priority": 1, "print_time": 60},
        {"id": "M2", "volume": 50, "priority": 1, "print_time": 70},
        {"id": "M3", "volume": 50, "priority": 1, "print_time": 80}
    ]

    result5 = optimize_printing(test5_jobs, constraints)
    print(f"Jobs: {test5_jobs}")
    print(f"Constraints: max_volume={constraints['max_volume']}, max_items={constraints['max_items']}")
    print(f"\nResult:")
    print(f"  Print order: {result5['print_order']}")
    print(f"  Total time: {result5['total_time']} minutes")
    print(f"\nExplanation:")
    print(f"  Volume allows all 3 (150 <= 300), but max_items=2")
    print(f"  Batch 1: M1 + M2 (2 items max)")
    print(f"           Time = max(60, 70) = 70 minutes")
    print(f"  Batch 2: M3")
    print(f"           Time = 80 minutes")
    print(f"  Total: 70 + 80 = 150 minutes")


if __name__ == "__main__":
    test_printing_optimization()
