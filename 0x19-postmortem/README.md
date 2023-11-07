# Post-Mortem Report

## Issue Summary

On November 1, 2023, from 10:00 AM to 2:00 PM GMT, my web application decided to take an unexpected break. I found that about 35% of my users were unable to access the application and were greeted with a "503 Service Unavailable" error. The root cause was a memory leak in one of my backend services.

## Timeline

- **10:00 AM** - My monitoring system alerted me about an unusual spike in memory usage.
- **10:15 AM** - I started investigating, focusing on recent deployments and database issues.
- **10:45 AM** - After initial investigations proved inconclusive, I decided to look into the backend services.
- **11:30 AM** - I identified a potential memory leak in a recently updated service.
- **12:00 PM** - Attempts to patch the service on the fly were unsuccessful.
- **1:00 PM** - I decided to roll back to a previous stable version of the service.
- **2:00 PM** - The application was back online and functioning normally.

## Root Cause and Resolution

The issue was caused by a memory leak in a service that was part of a recent update. This service failed to release memory after processing user requests, leading to an unsustainable increase in memory usage over time. The issue was resolved by rolling back this service to its previous stable version.

## Corrective and Preventative Measures

To prevent such incidents in the future, you plan to:

- Improve my code review process to catch potential memory leaks.
- Implement automated memory leak detection in my CI/CD pipeline.
- Increase my monitoring system's sensitivity to memory usage spikes.
- Enhance my rollback procedures for quicker response times.

## Tasks

- Patch the service to fix the memory leak.
- Update the code review guidelines with a focus on memory management.
- Integrate a memory leak detection tool into my CI/CD pipeline.
- Adjust the alert thresholds in my monitoring system.
- Document and train myself on the enhanced rollback procedures.
