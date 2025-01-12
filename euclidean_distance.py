
import math

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktalar listesi
points = [(1, 2), (3, 5), (6, 1), (4, 4)]

# Mesafeleri saklamak için liste
distances = []

# Tüm nokta çiftleri için mesafeyi hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print("Tüm nokta çiftleri arasındaki minimum mesafe:", min_distance)
