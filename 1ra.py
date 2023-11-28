import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
edades = data["age"]
edades_np = np.array(edades)
edad_prom = np.mean(edades_np)
print(f"Promedio de edades participantes es: {edad_prom:.2f} años")