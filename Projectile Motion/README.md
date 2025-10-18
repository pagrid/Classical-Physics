# 🏹 Projectile Motion Simulation

A **computational simulation of 2D projectile motion** under uniform gravity.

This project illustrates how the **launch angle and initial speed** affect the **trajectory**, **range**, and **maximum height** of a projectile. It demonstrates fundamental concepts of classical mechanics and kinematics.

---

## ⚙️ Features

- 🧮 **Numerical integration of motion:** Computes $x(t)$ and $y(t)$ using small time steps  
- 💡 **Single trajectory visualization:** Launch at a specified angle and speed  
- 🌐 **Multiple trajectories:** Compare different launch angles to observe effects on range and height  
- 🎨 **High-quality plots:** Trajectories clearly show differences in motion parameters  

---

## 🧠 Background

Projectile motion describes the **2D motion of an object under the influence of gravity** only, assuming no air resistance. The kinematic equations are:

$$
x(t) = v_0 \cos(\theta) \, t, \quad
y(t) = v_0 \sin(\theta) \, t - \frac{1}{2} g t^2
$$

where:

- $v_0$ is the initial speed  
- $\theta$ is the launch angle  
- $g$ is the acceleration due to gravity  

Numerical integration allows simulation of the trajectory for arbitrary time steps and visualization of **single or multiple projectiles**.

---

## 📊 Example Outputs

### 🔹 Single Trajectory (45°)
![Single Trajectory](pm_45_trajectory.png)

Trajectory of a projectile launched at 45° with $v_0 = 20$ m/s.

### 🔹 Multiple Trajectories (10°–80°)
![Multiple Trajectories](pm_vr_trajectories.png)

Comparison of trajectories for different launch angles, highlighting how angle affects **range** and **height**.

---

## 📝 License
This project is released under the [MIT License](LICENSE).



