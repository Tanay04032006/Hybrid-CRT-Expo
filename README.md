**HybridCRT-Expo** 

---

## 👨‍💻 Made By  
- **Tanay Gupta** - RA2311030010109  
- **Avinash Shankar** - RA2311030010110  



---

# 🔢 HybridCRT-Expo Algorithm  

A Python implementation of the **Hybrid Chinese Remainder Theorem (CRT) Exponentiation** algorithm to efficiently compute:  

\[
a^b \mod m
\]

This method factorizes \( m \) into two coprime factors, computes modular exponentiation separately, and combines the results using **CRT**.  

---

## 📌 Features  
✅ **Efficient modular exponentiation** (Exponentiation by Squaring)  
✅ **Automatic factorization** of `m` into **two prime numbers**  
✅ **Modular inverse computation** (Extended Euclidean Algorithm)  
✅ **Chinese Remainder Theorem (CRT)** for efficient combination  

---

## 📂 Project Structure  

```
📁 HybridCRT-Expo
├── 📜 hybrid_crt_expo.py    # Python implementation of the algorithm
├── 📜 README.md             # Documentation
```

---

## 🚀 Getting Started  

### 📌 Prerequisites  
- Python 3.x installed  
- Basic understanding of modular arithmetic  

### ▶️ Installation & Usage  

1️⃣ **Clone the repository**  
```sh
git clone https://github.com/YOUR-USERNAME/HybridCRT-Expo.git
cd HybridCRT-Expo
```

2️⃣ **Run the script**  
```sh
python hybrid_crt_expo.py
```

---

## 📜 Code Explanation  

### 🔹 **Modular Exponentiation**  
```python
def mod_expo(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:  # If b is odd
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result
```
🔹 Computes \( a^b \mod m \) using **Exponentiation by Squaring**.  

---

### 🔹 **Extended Euclidean Algorithm & Modular Inverse**  
```python
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m
```
🔹 Computes the **modular inverse** using the **Extended Euclidean Algorithm**.  

---

### 🔹 **Chinese Remainder Theorem (CRT)**  
```python
def chinese_remainder(x_p, x_q, p, q):
    m1, m2 = q, p
    inv1 = mod_inverse(m1, p)
    inv2 = mod_inverse(m2, q)
    
    x = (x_p * m1 * inv1 + x_q * m2 * inv2) % (p * q)
    return x
```
🔹 Combines results from `mod p` and `mod q` using **CRT**.  

---

## 🔥 Example Run  

### **Input:**  
```python
a, b, m = 3, 200, 55
result = hybrid_crt_expo(a, b, m)
print("Result:", result)
```

### **Output:**  
```
Result: 18
```
\[
3^{200} \mod 55 = 18
\]

---

## 🤝 Contributing  

🔹 **Fork** the repository  
🔹 **Create** a new branch (`git checkout -b feature-name`)  
🔹 **Commit** your changes (`git commit -m "Added feature XYZ"`)  
🔹 **Push** to your branch (`git push origin feature-name`)  
🔹 **Submit a Pull Request**  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

### ⭐ Show Some Support!  
If you found this useful, consider **starring** ⭐ the repository! 🚀  

Let me know if you want any modifications! 😊
