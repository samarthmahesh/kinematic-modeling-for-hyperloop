# 🚄 Hyperloop Kinematics Modeling & Simulation Suite

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3175A2?style=for-the-badge&logo=matplotlib&logoColor=white)

-Samarth Mahesh

## A rough work on paper showing the v-t graph which represents the 3 phases of the hyperloop

 <img width="1718" height="770" alt="image" src="https://github.com/user-attachments/assets/d08ea5e5-9e3e-4371-9221-39401ac4f270" />
 

When designing futuristic transport systems like the Hyperloop, the core challenge is balancing speed, safety, and comfort. This simulation  helps us break down the pod's journey into three important phases — **Acceleration**, **Cruise**, and **Deceleration** — and understand what’s physically required in each.

By running these Python scripts, we can visualize the crucial links between speed, distance, and acceleration. These insights guide us in deciding:

- How long our acceleration and braking tracks need to be
  **Which inturn affects**
- What power our motors and brakes should deliver
- How to keep passenger experience smooth and safe by controlling g-forces
- How to optimize travel time and conserve energy

  
## 1. Accelerate 

  <img width="637" height="543" alt="image" src="https://github.com/user-attachments/assets/c9b3031c-8513-405c-8291-01261c5c4cc7" />

### This is the how the pod starts. Here, when we want to reach a certain speed in a given distance, **What** should our acceleration be? This answers that

`a = v² / (2s)`

  
- **Variables:**
  - \(v\): Desired cruise velocity (m/s)
  - \(s\): Distance available to accelerate (m)
  - \(a\): Constant acceleration needed (m/s²)
  
- **Why it matters:** This plot shows the interplay between launch track length and acceleration demands, helping balance engineering costs and passenger comfort.


## 2. Cruise

<img width="635" height="537" alt="image" src="https://github.com/user-attachments/assets/7353562f-b9d8-4c04-8828-d591ed7400a9" />

### After attaining the cruise speed, we reach this stage in which the pod stays for the maximum time. This shows **how** much distance can be covered between point A and B when my factors speed and time are varied.

`d = v × t`

- **Variables:**
  - \(v\): Constant cruise velocity (m/s)
  - \(t\): Duration of cruising (seconds)
  - \(d\): Distance covered (meters)
  
- **Why it matters:** Crucial for route planning and scheduling, letting us predict travel distances and durations between stations.


## 3. Deccelerate

<img width="634" height="542" alt="image" src="https://github.com/user-attachments/assets/0b7c36f5-6590-4445-8e17-b0b869df8b8d" />

### Also known as crash equation. Here, when we know a foreign object is at a certain distance and colliding could cause an accident or we near a station, we are already at a certain speed, So, **What** is the optimum decceleration needed so that the pod stops before it without over-braking and making it uncomfortble for the passengers.

`a = -u² / (2s)`

  
- **Variables:**
  - \(u\): Velocity at start of braking (m/s)
  - \(s\): Distance to obstacle (m)
  - \(a\): Required deceleration (m/s²), negative due to slowing
  
- **Why it matters:** Defines emergency braking requirements and safe spacing between pods—impacting system capacity and safety regulations.

## Tools used:

### **Python 3.x**
### **NumPy**: For numerical operations and creating the data arrays.
### **Matplotlib**: For generating the 3D surface plots.


These visual tools aren't just plots—they’re the critical engineering aids that help us avoid costly mistakes and build something truly safe and efficient. By tinkering with  speed, time, and distance in each phase, we learn the limits and possibilities for the Hyperloop design.

