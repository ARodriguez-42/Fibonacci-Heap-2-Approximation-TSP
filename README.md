# Fibonacci-Heap-2-Approximation-TSP

The Traveling Salesman's Problem (TSP) is a classic optimization challenge in computer science and mathematics. It involves finding the shortest possible route that visits a set of given locations exactly once and returns to the starting point, making it a fundamental problem in route optimization and logistics.

In my Algorithms course, our group was tasked with implementing the 2-approximation algorithm to solve the Traveling Salesman problem. Initially, we employed Prim's Algorithm to find the minimum spanning tree, but after completing the course, I successfully implemented a streamlined version of a Fibonacci heap to significantly enhance the algorithm's time complexity. While Prim's Algorithm exhibits a time complexity of O(V^2), a Fibonacci heap boasts a more efficient O(E + V log V) time complexity. While the time difference may not be readily apparent for problems with a small number of cities, as the number of cities in the Traveling Salesman Problem (TSP) increases, the execution speed improvement becomes noticeable.

In the repository, you will find my implementation of a Fibonacci heap, an MST-TSP conversion Python file, as well as the comprehensive report produced by my group for our Algorithms course.
