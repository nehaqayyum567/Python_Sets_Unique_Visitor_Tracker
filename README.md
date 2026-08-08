# Unique Visitor Tracker

A Python mini project that simulates a visitor tracking system using the *Set* data structure.

The project compares visitors from two different days and demonstrates how Python set operations can be used to analyze unique, returning, new, and non-visiting users.

## Features

- Create visitor sets for Day 1 and Day 2
- Count visitors using len()
- Find all unique visitors using union()
- Find returning visitors using intersection()
- Find new visitors using difference()
- Check visitor membership using in
- Find non-visitors using a universal set and difference()

## Concepts Used

- Python Sets
- Tuples
- len()
- union()
- intersection()
- difference()
- Membership operator in
- User input
- Conditional statements

## How It Works

The project stores visitor information as tuples containing details such as a visitor's name, age, and email.

Two sets are created:

- *Day 1 Visitors*
- *Day 2 Visitors*

The program then performs different set operations to analyze the visitor data.

### Example Analysis

- *Unique Visitors:* Combines visitors from both days.
- *Returning Visitors:* Finds visitors who appeared on both days.
- *New Visitors:* Finds visitors who appeared on Day 2 but not Day 1.
- *Non-Visitors:* Finds registered users who did not visit on either day.

## How to Run

Make sure Python 3 is installed.

Run the program:

bash
python unique_visitor_tracker.py


## Purpose

This project was created to practice Python Sets by applying set operations to a practical visitor-tracking problem.

## Author

Neha Qayyum