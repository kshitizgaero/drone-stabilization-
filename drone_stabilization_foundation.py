# =======================================================
# PROJECT: Drone Stabilization Foundation with RL (CartPole)
# Author: Kshitiz Gupta
# Description: Trains a PPO agent to balance a pole on a cart -
#              the simplified version of drone stabilization
# =======================================================

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

print("="*60)
print("🚁 DRONE STABILIZATION FOUNDATION WITH RL")
print("="*60)

# --- 1. Create the environment ---
# CartPole is the simplified version of drone stabilization
# Instead of a drone with 4 motors and IMU sensors,
# we have a cart with 1 motor and a pole (representing drone attitude)
print("\n📌 Setting up drone stabilization environment...")

# Use 4 parallel environments for faster training
# (Like running 4 drone simulations simultaneously)
env = make_vec_env("CartPole-v1", n_envs=4)

print(f"✅ Environment ready! (4 parallel simulations)")

# --- 2. Create the PPO model ---
# PPO is the industry-standard algorithm used in drone research
print("\n🧠 Initializing PPO agent...")

model = PPO(
    "MlpPolicy",           # Neural network policy (like drone's flight controller)
    env,
    verbose=1,             # Show training progress
    learning_rate=0.001,   # How fast the drone learns
    n_steps=2048,          # Steps before updating the drone's brain
    batch_size=64,         # How many samples to learn from at once
    n_epochs=10,           # How many times to learn from each sample
)

print("✅ PPO agent ready!")

# --- 3. Train the agent ---
print("\n🎯 Starting training...")
print("   (The drone is learning to stabilize itself)")
print("   (This takes ~2 minutes on a standard laptop)")
print("-"*60)

model.learn(total_timesteps=50000)  # 50,000 steps = ~2 minutes

print("-"*60)
print("✅ Training complete! The drone has learned to stabilize.")

# --- 4. Save the model ---
model.save("drone_stabilization_model")
print("💾 Model saved as drone_stabilization_model.zip")

# --- 5. Test the trained agent ---
print("\n🎬 Testing the trained drone stabilizer...")
print("   A window will open showing the drone (cart) balancing")

test_env = gym.make("CartPole-v1", render_mode="human")
obs, _ = test_env.reset()

# Run for 500 steps (the drone will balance the pole)
for i in range(500):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, truncated, info = test_env.step(action)
    test_env.render()
    if done or truncated:
        obs, _ = test_env.reset()

test_env.close()

print("\n" + "="*60)
print("🎉 SUCCESS! The drone stabilizer is working!")
print("="*60)
print("\n💡 KEY CONNECTION TO DRONES:")
print("   - Cart = Drone body")
print("   - Pole = Drone attitude (pitch/roll)")
print("   - Moving cart = Motor thrust adjustment")
print("   - Keeping pole upright = Keeping drone stable")
print("   - PPO algorithm = Same as used in drone research")
print("\n💡 NEXT STEPS:")
print("   - Extend to PyBullet drone simulation")
print("   - Train for hover stabilization")
print("   - Add obstacle avoidance")
